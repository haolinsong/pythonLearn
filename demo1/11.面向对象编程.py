# 面向对象编程：把一组数据和处理数据的方法组成对象，把行为相同的对象归纳为类，
# 通过封装隐藏对象的内部细节，通过继承实现类的特化和泛化，通过多态实现基于对象类型的动态分派。
class Student:
    #在我们调用Student类的构造器创建对象时，首先会在内存中获得保存学生对象所需的内存空间，
    # 然后通过自动执行__init__方法，完成对内存的初始化操作
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        print(f'{self.name}正在玩游戏.')

stu1 = Student('浩霖', 30)
# 通过“类.方法”调用方法 第一个参数是接收消息的对象  第二个是函数的参数
Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法
stu1.study('Python程序设计')             # 学生正在学习Python程序设计.
