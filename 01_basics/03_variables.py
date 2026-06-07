"""
================================================================================
File: 03_variables.py
Topic: Variables in Python
================================================================================

This file demonstrates how to create and use variables in Python. Variables
are containers for storing data values. Unlike other programming languages,
Python has no command for declaring a variable - it's created the moment
you assign a value to it.

Key Concepts:
- Variable creation and assignment
- Variable naming conventions
- Multiple assignments
- Variable types and type checking
- Constants
- Variable scope basics

================================================================================
"""

# ============================================================================
# 【中文导读】变量与赋值
# ----------------------------------------------------------------------------
# 关键心智模型：Python 的变量不是“盒子”，而是“贴在对象上的标签(名字)”。
# 赋值 x = 10 做的是：先创建对象 10，再让名字 x 指向它。多个名字可指向同一对象。
# 这解释了后面所有 is / == / 可变对象共享 的行为。
#
# 学这个文件你要拿下的难点：
#   1. 动态类型：同一个名字可先后指向不同类型的对象
#   2. 解包赋值与星号扩展解包：a, *rest = [...]、first, *mid, last = [...]
#   3. is（同一对象，比 id）  vs  ==（值相等）——别混用
#   4. 小整数缓存：-5~256 被预先缓存，is 可能“意外”为 True，不可依赖
#   5. global：函数内要“重新赋值”全局变量才需要它（只读取不需要）
#   6. 常量靠约定（全大写）+ typing.Final，Python 没有真正的常量
# ============================================================================

# -----------------------------------------------------------------------------
# 1. Creating Variables
# -----------------------------------------------------------------------------
# Variables are created when you assign a value to them

print("--- Creating Variables ---")

# Simple variable assignments
name = "Baraa"
age = 25
height = 1.75
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")
print(f"Is student: {is_student}")

# Variables can be reassigned to different values
x = 10
print(f"\nx = {x}")
x = 20
print(f"x = {x} (reassigned)")

# Variables can even change types (dynamic typing)
# 中文：动态类型——类型属于“对象”，不属于“名字”。所以同一个名字可以先指向 int、
#       再改指向 str。type(value).__name__ 取类型的可读名称（'int' / 'str'）。
value = 100
print(f"\nvalue = {value} (type: {type(value).__name__})")
value = "one hundred"
print(f"value = {value} (type: {type(value).__name__})")

# -----------------------------------------------------------------------------
# 2. Variable Naming Rules
# -----------------------------------------------------------------------------
# Rules for Python variable names

print("\n--- Variable Naming Rules ---")

# ✅ Valid variable names
my_variable = 1        # Lowercase with underscores (snake_case) - RECOMMENDED
myVariable = 2         # camelCase - valid but not Pythonic
MyVariable = 3         # PascalCase - usually for classes
_private_var = 4       # Starts with underscore - convention for private
__very_private = 5     # Double underscore - name mangling
# ⚠️ 坑：双下划线开头只在“类内部”才触发名字改写(name mangling，变成 _类名__名)，
#        用来避免子类覆盖；在模块/普通变量层面它没这个魔力，只是个普通名字。
var123 = 6             # Can contain numbers (but not start with them)
CONSTANT = 7           # ALL CAPS - convention for constants

print(f"my_variable = {my_variable}")
print(f"_private_var = {_private_var}")
print(f"CONSTANT = {CONSTANT}")

# ❌ Invalid variable names (would cause errors):
# 123var = 1       # Cannot start with a number
# my-variable = 1  # Hyphens not allowed
# my variable = 1  # Spaces not allowed
# class = 1        # Cannot use reserved keywords

# Reserved keywords in Python (cannot use as variable names):
import keyword
print(f"\nPython reserved keywords: {keyword.kwlist[:10]}...")

# -----------------------------------------------------------------------------
# 3. Naming Conventions (PEP 8)
# -----------------------------------------------------------------------------

print("\n--- Naming Conventions (PEP 8) ---")

# Variables and functions: snake_case
user_name = "john_doe"
max_value = 100
is_active = True

# Constants: UPPER_SNAKE_CASE
PI = 3.14159
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30

# Classes: PascalCase (CapWords)
# class MyClass:
#     pass

# Private variables: leading underscore
_internal_state = "private"

# "Very private" / Name-mangled: double leading underscore
__name_mangled = "mangled"

print(f"user_name: {user_name}")
print(f"PI (constant): {PI}")
print(f"MAX_CONNECTIONS (constant): {MAX_CONNECTIONS}")

# Descriptive names are better than short names
# ✅ Good
total_price = 99.99
customer_name = "Alice"
is_logged_in = True

# ❌ Bad (avoid!)
# tp = 99.99
# cn = "Alice"
# il = True

# -----------------------------------------------------------------------------
# 4. Multiple Variable Assignment
# -----------------------------------------------------------------------------

print("\n--- Multiple Variable Assignment ---")

# Assign the same value to multiple variables
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")

# Assign different values in one line
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# Swap variables easily
# 中文：x, y = y, x 一行交换。原理：右侧先打包成临时元组 (y, x)，再整体解包给左侧，
#       所以不需要中间变量。这是 Python 的惯用法，比传统三步交换更直观。
print(f"\nBefore swap: x = {x}, y = {y}")
x, y = y, x
print(f"After swap: x = {x}, y = {y}")

# Unpack a list/tuple into variables
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"\nUnpacked coordinates: x={x}, y={y}, z={z}")

# Extended unpacking with *
# 中文：带星号的“扩展解包”——星号变量贪婪地收集剩余元素，且结果总是 list。
# ⚠️ 坑：一次解包里最多只能有一个带 * 的变量（否则无法判断各拿多少个）。
#        若元素数量不足以喂给非星号变量，会抛 ValueError。
first, *rest = [1, 2, 3, 4, 5]
print(f"first = {first}, rest = {rest}")            # first=1, rest=[2,3,4,5]

*beginning, last = [1, 2, 3, 4, 5]
print(f"beginning = {beginning}, last = {last}")    # beginning=[1,2,3,4], last=5

first, *middle, last = [1, 2, 3, 4, 5]
print(f"first = {first}, middle = {middle}, last = {last}")  # 星号在中间也行

# -----------------------------------------------------------------------------
# 5. Variable Types and Type Checking
# -----------------------------------------------------------------------------

print("\n--- Variable Types and Type Checking ---")

# Python is dynamically typed - types are determined at runtime
integer_var = 42
float_var = 3.14
string_var = "Hello"
bool_var = True
list_var = [1, 2, 3]
dict_var = {"key": "value"}
none_var = None

# Check types using type()
print(f"integer_var: {integer_var} -> {type(integer_var)}")
print(f"float_var: {float_var} -> {type(float_var)}")
print(f"string_var: {string_var} -> {type(string_var)}")
print(f"bool_var: {bool_var} -> {type(bool_var)}")
print(f"list_var: {list_var} -> {type(list_var)}")
print(f"dict_var: {dict_var} -> {type(dict_var)}")
print(f"none_var: {none_var} -> {type(none_var)}")

# Check if variable is of a specific type using isinstance()
print(f"\nIs integer_var an int? {isinstance(integer_var, int)}")
print(f"Is string_var a str? {isinstance(string_var, str)}")
print(f"Is list_var a list? {isinstance(list_var, list)}")

# Check multiple types
print(f"Is integer_var int or float? {isinstance(integer_var, (int, float))}")

# -----------------------------------------------------------------------------
# 6. Type Casting (Converting Types)
# -----------------------------------------------------------------------------

print("\n--- Type Casting ---")

# String to integer
str_num = "123"
int_num = int(str_num)
print(f"'{str_num}' (str) -> {int_num} (int)")

# String to float
str_float = "3.14"
float_num = float(str_float)
print(f"'{str_float}' (str) -> {float_num} (float)")

# Number to string
number = 42
str_number = str(number)
print(f"{number} (int) -> '{str_number}' (str)")

# Float to integer (truncates, doesn't round)
pi = 3.99
int_pi = int(pi)
print(f"{pi} (float) -> {int_pi} (int) [truncated]")

# Boolean conversions
print(f"\nbool(1) = {bool(1)}")           # True
print(f"bool(0) = {bool(0)}")             # False
print(f"bool('hello') = {bool('hello')}") # True
print(f"bool('') = {bool('')}")           # False
print(f"bool([1, 2]) = {bool([1, 2])}")   # True
print(f"bool([]) = {bool([])}")           # False

# Integer to boolean
print(f"\nint(True) = {int(True)}")   # 1
print(f"int(False) = {int(False)}") # 0

# -----------------------------------------------------------------------------
# 7. Constants
# -----------------------------------------------------------------------------

print("\n--- Constants ---")

# Python doesn't have true constants, but by convention:
# - Use UPPER_SNAKE_CASE for constants
# - Don't modify them after initial assignment

# Mathematical constants
PI = 3.14159265359
E = 2.71828182845
GOLDEN_RATIO = 1.61803398875

# Application constants
MAX_USERS = 1000
API_TIMEOUT = 30
BASE_URL = "https://api.example.com"
DEBUG_MODE = False

print(f"PI = {PI}")
print(f"MAX_USERS = {MAX_USERS}")
print(f"BASE_URL = {BASE_URL}")

# You CAN modify them (Python won't stop you), but you SHOULDN'T
# PI = 3  # Don't do this!

# For true constants, you can use:
# 1. Separate constants module (constants.py)
# 2. typing.Final (Python 3.8+)
from typing import Final

MAX_SIZE: Final = 100
# MAX_SIZE = 200  # Type checker will warn about this

print(f"MAX_SIZE (Final) = {MAX_SIZE}")

# -----------------------------------------------------------------------------
# 8. Variable Scope (Basic)
# -----------------------------------------------------------------------------

print("\n--- Variable Scope ---")

# Global variable
global_var = "I'm global"


def my_function():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - global_var: {global_var}")
    print(f"Inside function - local_var: {local_var}")


my_function()
print(f"Outside function - global_var: {global_var}")
# print(local_var)  # Error! local_var doesn't exist here


# Modifying global variables inside functions
counter = 0


def increment():
    # 中文：counter += 1 是“读 + 写”，写操作会让 Python 默认把 counter 当成局部变量，
    #       于是“读”时它还没赋值 → UnboundLocalError。global 声明解除这个误判。
    # ⚠️ 坑：只“读取”全局变量不需要 global；一旦在函数里对它“赋值”就必须声明。
    #        （嵌套函数里改外层局部变量则用 nonlocal。）
    global counter  # Declare we want to use global counter
    counter += 1


print(f"\nBefore increment: counter = {counter}")
increment()
increment()
print(f"After 2 increments: counter = {counter}")

# -----------------------------------------------------------------------------
# 9. Variable Identity and Memory
# -----------------------------------------------------------------------------

print("\n--- Variable Identity and Memory ---")

# id() returns the memory address of a variable
a = 10
b = 10
c = a

print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"c = {c}, id(c) = {id(c)}")

# Small integers (-5 to 256) are cached in Python
# 中文：CPython 预先缓存了 -5~256 这些小整数对象，全程复用同一个，所以 a is b 为 True。
# ⚠️ 坑：这是实现细节，不可依赖！别用 is 来比较数值是否相等——比较值永远用 ==。
print(f"\na is b: {a is b}")  # True (same memory location)
print(f"a is c: {a is c}")    # True

# Larger numbers may have different ids
# 中文：超出缓存范围的大整数，每次字面量通常是新对象，is 很可能为 False，正印证上面的坑。
x = 1000
y = 1000
print(f"\nx = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

# 'is' vs '=='
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# 中文：== 比“值是否相等”，is 比“是不是同一个对象”(等价于 id 相同)。
#       list3 = list1 没有拷贝，只是多贴一个标签，所以 is 为 True；
#       改 list3 也会影响 list1（同一对象）。需要副本用 list1.copy() 或 list1[:]。
print(f"\nlist1 == list2: {list1 == list2}")  # True (same values)
print(f"list1 is list2: {list1 is list2}")    # False (different objects)
print(f"list1 is list3: {list1 is list3}")    # True (same object)

# -----------------------------------------------------------------------------
# 10. Deleting Variables
# -----------------------------------------------------------------------------

print("\n--- Deleting Variables ---")

temp_var = "I will be deleted"
print(f"temp_var exists: {temp_var}")

del temp_var
# print(temp_var)  # Error! NameError: name 'temp_var' is not defined

print("temp_var has been deleted")

# Check if variable exists
if 'temp_var' not in dir():
    print("temp_var no longer exists in current scope")

# -----------------------------------------------------------------------------
# 11. Practical Examples
# -----------------------------------------------------------------------------

print("\n--- Practical Examples ---")

# Example 1: User profile
first_name = "Baraa"
last_name = "Shaer"
full_name = f"{first_name} {last_name}"
email = f"{first_name.lower()}.{last_name.lower()}@example.com"

print(f"Full Name: {full_name}")
print(f"Email: {email}")

# Example 2: Shopping cart
item_price = 29.99
quantity = 3
discount_percent = 10

subtotal = item_price * quantity
discount_amount = subtotal * (discount_percent / 100)
total = subtotal - discount_amount

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Discount ({discount_percent}%): -${discount_amount:.2f}")
print(f"Total: ${total:.2f}")

# Example 3: Temperature conversion
celsius = 25
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"\n{celsius}°C = {fahrenheit}°F = {kelvin}K")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("VARIABLES SUMMARY")
print("=" * 60)
print("""
1. Variables are created by assignment (=)
2. Python is dynamically typed
3. Use snake_case for variables (PEP 8)
4. Use UPPER_CASE for constants
5. Multiple assignments: x, y, z = 1, 2, 3
6. Check types with type() or isinstance()
7. Convert types with int(), str(), float(), bool()
8. Variables have scope (local vs global)
9. Use 'is' for identity, '==' for equality
10. Delete variables with 'del'
""")

# ============================================================================
# 【避坑总结 · 03_variables.py】
# ----------------------------------------------------------------------------
# 1. 变量是“名字/标签”，赋值只是让名字指向对象；多个名字可指向同一对象。
# 2. is 比身份(同一对象)、== 比值；比较数值/普通相等永远用 ==，别用 is。
# 3. 小整数(-5~256)被缓存，is 可能意外为 True——实现细节，不可依赖。
# 4. b = a 不复制对象；对可变对象(list/dict)改 b 会连带改 a，需副本用 .copy()。
# 5. 函数内对全局变量“赋值”必须先 global，否则触发 UnboundLocalError；只读不用。
# 6. 扩展解包最多一个 *；元素不够喂给非星号变量会 ValueError。
# 7. int() 转 float 是“截断”不是四舍五入：int(3.99) == 3。
# 8. Python 无真常量；全大写只是约定，typing.Final 仅供类型检查器告警。
# ============================================================================
