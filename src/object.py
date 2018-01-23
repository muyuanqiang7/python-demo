#!/usr/local/bin/python3
# encoding:utf-8

"""
python3 面向对象
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
实例变量：定义在方法中的变量，只作用于当前实例的类。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
方法：类中定义的函数。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
类定义
    class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""


class Person:
    age = 0
    name = ""

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def toString(self):
        return repr("{}'s age is {}".format(self.name, self.age))

    def printSelf(self):
        print(self)
        print(self.__class__)


# person = Person(26, "Bob")
# print(person.toString())
# person.printSelf()

class People:
    name = ""
    age = 0
    __weight = 0.0
    __height = 0.0

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.__weight = weight
        self.__height = height

    def speak(self):
        print("%s 说:我今年 %d 岁" % (self.name, self.age))

    def weight(self):
        return self.__weight

    def height(self):
        return self.__height


people = People("runnoob", 26, 64.5, 160.0)
people.speak()
print(people.height())
print(people.weight())

"""
继承
class DerivedClassName(BaseClassName1):
    <statement-1>
    .
    .
    .
    <statement-N>
"""


# 单例模继承

class Student(People):
    grade = ''

    def __init__(self, name, age, weight, height, grade):
        People.__init__(self, name, age, weight, height)
        self.grade = grade

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# student = Student("Alice", 15, 45, 157, 2)
# student.speak()
# print(student.getWeight())
# print(student.getHeight())


class Speaker:
    topic = ''
    name = ''

    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


class Sample(Speaker, Student):

    def __init__(self, name, age, weight, height, grade, topic):
        Speaker.__init__(self, name, topic)
        Student.__init__(self, name, age, weight, height, grade)


sample = Sample("Alice", 15, 45, 157, 2, "Python")
sample.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法

"""
    方法重写
"""


class Parent:  # 定义父类
    def speak(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def speak(self):
        print('调用子类方法')


child = Child()  # 子类实例
child.speak()  # 子类调用重写方法

"""
类属性与方法
类的私有属性
__private_attr：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attr。

类的方法
在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。

self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。self.__private_methods。
"""
