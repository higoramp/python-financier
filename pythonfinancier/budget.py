from financier import Financier


class Budget:

    def __init__(self,data):
        self.data = data

    def __getattr__(self, key):
        if key not in self.data:
            raise AttributeError("'{}' object has no attribute '{}'".format(
                self.__class__.__name__, key))
        return self.data[key]

    def __setattr__(self, key, value):
        self.data[key] = value   