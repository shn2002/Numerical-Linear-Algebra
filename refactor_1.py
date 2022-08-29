import abc
from abc import ABC


class Component:
    @abc.abstractmethod
    def f(self):
        pass


class A(Component):
    def f(self):
        print("A")


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def f(self):
        print(self.component.f())


class B(Decorator):
    def f(self):
        self.component.f()
        print("B")


class C(Decorator):
    def f(self):
        self.component.f()
        print("C")


a = A()
a.f()
b = B(A())
b.f()
c = C(A())
c.f()
bc = C(B(A()))
bc.f()
cb = B(C(A()))
cb.f()
