from omsdk.typemgr.FieldType import FieldType

# private
#
# def __init__(self, mode, fname, alias, parent=None, volatile=False)
# def __eq__, __ne__, __lt__, __le__, __gt__, __ge__
# def __getattr__
# def __delattr__
# def __setattr__
# def _copy(self, other)
# def _commit(self)
# def _reject(self)
# @_changed
#
# def __str__, __repr__
#
# def _duplicate_tree(self, obj, parent)
# def _set_index(self, index=1)
#
# protected:
#
# def my_accept_value(self, value):
#
# public:
# def is_changed(self)
# def fix_changed(self)
# def copy(self, other, commit= False)
# def commit(self)
# def reject(self)
# def freeze(self)
# def unfreeze(self)
# def Properties(self):
#
# def get_root(self)

class ClassType(object):

    def __init__(self, mode, fname, alias, parent = None, volatile=False):
        self.__dict__['_freeze'] = False
        self.__dict__['_removed'] = {}
        self.__dict__['_track'] = False
        self.__dict__['_alias'] = alias
        self.__dict__['_volatile'] = volatile
        self.__dict__['_fname'] = fname
        self.__dict__['_changed'] = False
        self.__dict__['_parent'] = parent
        self.__dict__['_mode'] = mode
        self.__dict__['_super_field'] = False
        if mode == 'create':
            self.my_create()
        elif mode == 'modify':
            self.my_modify()
        elif mode == 'delete':
            self.my_delete()

    def __getattr__(self, name):
        if name in self.__dict__ and name not in ['_track', '_freeze', '_removed']:
            return self.__dict__[name]
        raise AttributeError('Invalid attribute ' + name)

    def __setattr__(self, name, value):
        # Do not allow access to internal variables
        if name in ['_track', '_freeze', '_removed']:
            raise AttributeError('Invalid attribute ' + name)

        # Freeze mode - don't allow any updates
        if '_freeze' in self.__dict__ and self.__dict__['_freeze']:
            raise ValueError('object in freeze mode')

        # Allow updates to internal fields
        if name in [ '_alias', '_parent', '_volatile', '_fname',
                     '_changed', '_mode', '_super_field' ]:
            self.__dict__[name] = value
            return

        # Update the value
        if name in self.__dict__['_removed']:
            if name not in self.__dict__:
                self.__dict__[name] = self.__dict__['_removed'][name]
            del self.__dict__['_removed'][name]

        if name not in self.__dict__:
            if isinstance(value, FieldType) or isinstance(value, ClassType):
                self.__dict__[name] = value
            else:
                raise ValueError('value does not belong to FieldType')
        elif isinstance(self.__dict__[name], FieldType):
            self.__dict__[name]._value = value
        elif isinstance(self.__dict__[name], ClassType):
            not_implemented
        else:
            raise ValueError('value does not belong to FieldType')

        # In tracking mode, update '_removed'
        if self.__dict__['_track'] and name in self.__dict__['_removed']:
            del self.__dict__['_removed'][name]

    def __delattr__(self, name):
        # Do not allow access to internal variables
        if name in ['_track', '_freeze', '_removed', '_child_name']:
            raise AttributeError('Invalid attribute ' + name)

        # Freeze mode - don't allow any updates
        if '_freeze' in self.__dict__ and self.__dict__['_freeze']:
            raise AttributeError('object in freeze mode')


        if name in self.__dict__:
            if self.__dict__['_track']:
                self.__dict__['_removed'][name] = self.__dict__[name]
            del self.__dict__[name]

    def __lt__(self, other):
        counter = 0
        if isinstance(other, type(self)):
            for i in self.Properties:
                if i not in other.__dict__:
                    counter = counter - 1
                elif self.__dict__[i].__lt__(other.__dict__[i]):
                    counter = counter + 1
                elif self.__dict__[i].__ne__(other.__dict__[i]):
                    counter = counter - 1
            for i in other.Properties:
                if i not in self.__dict__:
                    counter = counter + 1
        return (counter > 0)

    def __le__(self, other):
        counter = 0
        if isinstance(other, type(self)):
            for i in self.Properties:
                if i not in other.__dict__:
                    counter = counter - 1
                elif self.__dict__[i].__eq__(other.__dict__[i]):
                    continue
                elif self.__dict__[i].__gt__(other.__dict__[i]):
                    counter = counter - 1
            for i in other.Properties:
                if i not in self.__dict__:
                    counter = counter + 1
        return (counter >= 0)

    def __gt__(self, other):
        counter = 0
        if isinstance(other, type(self)):
            for i in self.Properties:
                if i not in other.__dict__:
                    counter = counter + 1
                elif self.__dict__[i].__gt__(other.__dict__[i]):
                    counter = counter + 1
                elif self.__dict__[i].__ne__(other.__dict__[i]):
                    counter = counter - 1
            for i in other.Properties:
                if i not in self.__dict__:
                    counter = counter - 1
        return (counter > 0)

    def __ge__(self, other):
        counter = 0
        if isinstance(other, type(self)):
            for i in self.Properties:
                if i not in other.__dict__:
                    counter = counter + 1
                elif self.__dict__[i].__eq__(other.__dict__[i]):
                    continue
                elif self.__dict__[i].__lt__(other.__dict__[i]):
                    counter = counter - 1
            for i in other.Properties:
                if i not in self.__dict__:
                    counter = counter - 1
        return (counter >= 0)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            for i in self.Properties:
                if i not in other.__dict__ or \
                   self.__dict__[i].__eq__(other.__dict__[i]) is False:
                    return False
            for i in other.Properties:
                if i not in self.__dict__:
                    return False
            return True
        return False

    def __ne__(self, other):
        return self.__eq__(other) != True

    def copy(self, other, commit = False):
        if not self._copy(other):
            return False
        if commit: self.commit()
        return True

    def _copy(self, other):
        if other is None or not isinstance(other, type(self)):
            return False
        for i in self.Properties:
            if i not in other.__dict__:
                # am I supposed to delete?
                continue
            if not self.__dict__[i]._volatile:
                self.__dict__[i]._copy(other.__dict__[i])
        for i in other.Properties:
            if i not in self.__dict__:
                # am I supposed to add?
                continue
        return True

    def _duplicate_tree(self, obj, parent):
        for i in self.Properties:
            if isinstance(self.__dict__[i], FieldType):
                if not obj.__dict__[i]._super_field:
                    obj.__dict__[i]._value = self.__dict__[i]._value
                obj.__dict__[i]._parent = parent
            else:
                obj.__dict__[i] = self.__dict__[i].duplicate(parent=self)
                obj.__dict__[i]._parent = parent
        return obj

    def _set_index(self, index=1):
        for i in self.Properties:
            self.__dict__[i]._index = index

    def get_root(self):
        if self._parent is None:
            return self
        return self._parent.get_root()

    def commit(self):
        self._commit()
        self.fix_changed()
        return True

    def _commit(self):
        for i in self.Properties:
            self.__dict__[i]._commit()
        return True

    def reject(self):
        self._reject()
        self.fix_changed()
        return True

    def _reject(self):
        for i in self.Properties:
            self.__dict__[i]._reject()
        return True

    def my_accept_value(self, value):
        return True

    def fix_changed(self):
        self._changed = False
        if len(self._removed) > 0:
            self._changed = True
        for i in self.Properties:
            if self.__dict__[i].fix_changed():
                self._changed = True
        return self._changed

    def is_changed(self):
        return self._changed

    def freeze(self):
        self.__dict__['_freeze'] = True
        for i in self.__dict__:
            if not i.startswith('_'):
                self.__dict__[i].freeze()

    def unfreeze(self):
        self.__dict__['_freeze'] = False
        for i in self.__dict__:
            if not i.startswith('_'):
                self.__dict__[i].unfreeze()

    def _duplicate_parent(self):
        parent_list = []
        obj = self
        while obj._parent:
            field_name = None
            for prop_name in obj._parent.Properties:
                if obj._parent.__dict__[prop_name] == obj:
                    field_name = prop_name
                    break
            parent_list.insert(0, (obj._parent, field_name))
            obj = obj._parent
        new_list = [ None ]
        for (parent, field) in parent_list:
            new_list.append(type(parent)('custom', new_list[-1]))
            if new_list[-2]:
                new_list[-2].__dict__[field] = new_list[-1]
        return (new_list[1], parent_list[-1][1])

    def duplicate(self, parent=None):
        if parent is None:
            (parent, field) = self._duplicate_parent()
        obj = type(self)(self._mode, parent)
        self._duplicate_tree(obj, parent)
        if parent:
            parent.__dict__[field] = obj
        return obj

    def my_create(self):
        pass

    def my_modify(self):
        pass

    def my_delete(self):
        pass

    @property
    def Properties(self):
        return sorted([i for i in self.__dict__ if not i.startswith('_')])

    def json_encode(self):
        return str(self)