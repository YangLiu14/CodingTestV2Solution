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

# ===================================================
# 4. 第一个元素作为第一排序依据，第二个元素作为第二排序依据
# ===================================================
lines = [(5, 8), (2, 4), (1, 2), (1, 6), (9, 23), (6, 7)]
lines.sort(key=lambda l: (l[0], -l[1]))
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

# Custom function
# ===============================
# 5. 根据自定义规则来排序
# ===============================
import functools
str_list = ['abc', 'de', 'b', 'ba']

def str_compare(a: str, b: str):
    if a+b > b+a:
        return 1
    elif a+b < b+a:
        return -1
    else:
        return 0

str_list = sorted(str_list, key=functools.cmp_to_key(str_compare))
print(str_list)
# >> ['abc', 'ba', 'b', 'de']


##############################
# 常见排序算法
##############################
# ============================
# Quick Sort
# ============================
def partition(arr, low, high):
    i = low - 1  # i 确定了比pivot小的数的右边界
    pivot = arr[high]

    # 遍历除了pivot之外的数组
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1  # 如果找到了比pivot小的数，那右边界就扩大一个
            arr[j], arr[i] = arr[i], arr[i]  # 把这个小的数字换到右边界所在的位置上

    # 最后pivot应当在的位置，就是右边界的右边一个位置
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)   # before pivot
        quickSort(arr, pi + 1, high)  # after pivot

