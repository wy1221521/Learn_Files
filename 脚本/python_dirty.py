#coding=utf-8
import requests
class dirty():
    __slots__ = ('a', 'b','score')
    name="weqw"

    def __init__(self):
        self.a=2
        self.b=3
        self.score=9

    @property
    def get_value(self):
        return (self.score)

    def __str__(self):
        return 'asd:%s'% self.a

    __repr__ = __str__

if __name__ == '__main__':

    def set_score(self, score):
        self.score = score
        print("设置分数",self.score)

    dirty.set_score = set_score

    my_test1=dirty()
    my_test1.set_score('89')
    print(my_test1.get_value)

    print(dirty())
    print(type("a"))
