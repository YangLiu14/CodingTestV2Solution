"""sort.py: sort algorithms"""
__author__ = "Yang Liu"
__email__ = "lander14@outlook.com"


##############################
# Python Sort tools
##############################
# 字符串list
# ===============================
# 1. 根据字符串长度排序
# ===============================
str_arr = ['ab', 'aabds', 'a', 'csd', 'abs']
str_arr.sort(key=lambda s: len(s))
print(str_arr)

# ===============================
# 2. 根据首字母排序
# ===============================
str_arr = ['apple', 'graph', 'Ace', 'direction', 'loading', 'is']
str_arr.sort(key=lambda s: ord(s[0]))
print(str_arr)

# Tuple
# ===============================
# 3. 线段问题: 根据第一个元素排序
# ===============================
lines = [(5, 8), (2, 4), (1, 2), (1, 6), (9, 23), (6, 7)]
lines.sort(key=lambda l: l[0])
print(lines)

# Class
# ===============================
# 4. 根据class某属性排序
# ===============================
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu1 = Student("Jack", 20)
stu2 = Student("Tim", 16)
stu3 = Student("Bob", 23)
stu4 = Student("Lily", 19)
students = [stu1, stu2, stu3, stu4]
students.sort(key=lambda stu: stu.age)
print([student.name for student in students])



##############################
# 常见排序算法
##############################
