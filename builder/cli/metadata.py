# rewrite dict
class MetaData:
    # __getattr__(self, item):  # 获取不存在的属性
    # __delattr__(self, item):  # 删除属性
    # __setattr__(self, key, value):

    def __getattr__(self, item):
        pass

    def __delattr__(self, item):
        pass

    def __setattr__(self, key, value):
        pass

    def __iter__(self):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        pass


if __name__ == '__main__':
    m = MetaData()
    m['name'] = "zx"

    print(m.items())

