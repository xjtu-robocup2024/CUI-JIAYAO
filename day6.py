class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def personInfo(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}")
class Student(Person):
    def __init__(self, name, age, gender, college, class_name):
        super().__init__(name, age, gender)  # 调用父类的构造函数
        self.college = college
        self.class_name = class_name  # 注意：在Python中，class是关键字，所以变量名不能用class，这里用class_name代替
    def personInfo(self):
        super().personInfo()  # 调用父类的personInfo方法
        print(f"学院: {self.college}, 班级: {self.class_name}")
    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}, 学院: {self.college}, 班级: {self.class_name}"
# 示例用法
student = Student("张三", 20, "男", "信息学院", "计算机科学与技术1班")
student.personInfo()  # 打印学生的个人信息
print(student)  # 使用str方法打印学生的信息