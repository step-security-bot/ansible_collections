#!/usr/bin/python3

class FilterModule(object):
    def filters(self):
        return {
            'dict_flatten': self.dict_flatten,
        }

    def dict_flatten(self, input, keys):
        if isinstance(input, list):
            obj_list = input
        elif isinstance(input, dict):
            obj_list = [input]
        else:
            raise AnsibleFilterError('must be a list of dicts or a nested dict') # type: ignore

        if isinstance(keys, list):
            key_list = keys
        elif isinstance(keys, str):
            key_list = [keys]
        else:
            raise AnsibleFilterTypeError('keys must be a list or a string') # type: ignore

        results = []
        for obj in obj_list:
            for key in key_list:
                if key in obj:
                    child = obj.pop(key)
                    obj |= child
            results.append(obj)

        return results[0] if isinstance(input, dict) else results
