class FilterModule(object):
    def filters(self):
        return {
            'sortbysubkey': self.sortbysubkey,
        }

    def sortbysubkey(self, dict_to_sort, sorting_key):
        return sorted(dict_to_sort.items(), key=lambda x: x[1][sorting_key], reverse=True)
