class LinearSearch:

    def __init__(self, alist):

        assert isinstance(alist, (list, tuple, dict, set, str)), "Not a valid data type!!"

        self.alist = alist

    def search(self, target):

        if isinstance(self.alist, (dict)):
            self.alist = self.alist.values

        for i in self.alist:
            if i == target:
                return True
            
        return False