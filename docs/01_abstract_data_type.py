# -*- coding:utf-8 -*-
# @Description: code for abstract data type and OOP
# @Author:
# @Copyright
# @Version:0.0.1
class Bag(object):

    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self._items = list()

    def add(self, item):
        # print(len(self))
        if len(self) >= self.maxsize:
            raise Exception('Full')
        self._items.append(item)

    def remove(self, item):
        # print(len(self))
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag()

    bag.add(1)
    bag.add(2)
    bag.add(3)
    bag.add(5)

    assert len(bag) == 4

    bag.remove(3)
    bag.remove(5)
    assert len(bag) == 2

    for i in bag:
        print(i)


if __name__ == '__main__':
    test_bag()