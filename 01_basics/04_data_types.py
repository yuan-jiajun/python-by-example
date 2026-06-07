"""
================================================================================
File: 04_data_types.py
Topic: Data Types in Python
================================================================================

This file demonstrates Python's built-in data types. Understanding data types
is fundamental to programming as they determine what operations can be
performed on data and how it's stored in memory.

Key Concepts:
- Numeric types (int, float, complex)
- Text type (str)
- Boolean type (bool)
- Sequence types (list, tuple, range)
- Mapping type (dict)
- Set types (set, frozenset)
- None type
- Type checking and conversion

================================================================================
"""

# ============================================================================
# 【中文导读】内置数据类型全景
# ----------------------------------------------------------------------------
# 这个文件横扫 Python 全部内置类型。贯穿始终的一条主线是“可变 vs 不可变”：
#   - 不可变(immutable)：int float complex str bool tuple frozenset range None
#   - 可变(mutable)：    list dict set
# 不可变对象“改值”其实是生成新对象、名字改指向；可变对象可原地修改。
# 这条主线决定了能不能做字典的 key、函数默认值能不能用、要不要拷贝等一系列问题。
#
# 学这个文件你要拿下的难点 / 高频坑：
#   1. 浮点精度：0.1 + 0.2 != 0.3，需要精确小数用 decimal.Decimal('0.1')
#   2. {} 是空字典不是空集合；空集合只能 set()
#   3. 单元素元组靠逗号：(1,) 才是元组，(1) 只是带括号的整数
#   4. 判空用 x is None，不要用 == None
#   5. 整数除法：/ 永远返回 float，// 是向下取整的整除
#   6. type(x) 精确匹配类型；isinstance(x, ...) 更推荐（认子类、可传类型元组）
# ============================================================================

# -----------------------------------------------------------------------------
# 1. Numeric Types Overview
# -----------------------------------------------------------------------------

print("=" * 60)
print("NUMERIC TYPES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1.1 Integers (int)
# -----------------------------------------------------------------------------

print("\n--- Integers (int) ---")

# Basic integers
positive_int = 42
negative_int = -17
zero = 0

print(f"Positive: {positive_int}")
print(f"Negative: {negative_int}")
print(f"Zero: {zero}")

# Large integers (Python handles arbitrary precision)
# 中文：Python 的 int 是“任意精度”（big integer），没有 32/64 位上限，
#       多大都不会像 C/Java 那样溢出，运算自动扩展。这是 Python 的一大特点。
big_number = 123456789012345678901234567890
print(f"Big number: {big_number}")
print(f"Type: {type(big_number)}")

# Different number bases
binary = 0b1010      # Binary (base 2)
octal = 0o17         # Octal (base 8)
hexadecimal = 0xFF   # Hexadecimal (base 16)

print(f"\nBinary 0b1010 = {binary}")
print(f"Octal 0o17 = {octal}")
print(f"Hex 0xFF = {hexadecimal}")

# Underscores for readability (Python 3.6+)
million = 1_000_000
credit_card = 1234_5678_9012_3456
print(f"\nMillion: {million}")
print(f"Credit card: {credit_card}")

# Integer operations
a, b = 17, 5
print(f"\na = {a}, b = {b}")
print(f"a + b = {a + b}")    # Addition
print(f"a - b = {a - b}")    # Subtraction
print(f"a * b = {a * b}")    # Multiplication
print(f"a / b = {a / b}")    # Division (returns float)
# ⚠️ 坑：单斜杠 / 永远返回 float，17/5=3.4；即使整除 4/2 结果也是 2.0 而非 2。
#        要整数结果用 //。
print(f"a // b = {a // b}")  # Floor division
# ⚠️ 坑：// 是“向下取整”不是“截断向零”。负数时 -17 // 5 == -4（不是 -3）；
#        同理 % 的结果符号跟随除数：-17 % 5 == 3。
print(f"a % b = {a % b}")    # Modulo (remainder)
print(f"a ** b = {a ** b}")  # Exponentiation（幂运算，a 的 b 次方）

# -----------------------------------------------------------------------------
# 1.2 Floating-Point Numbers (float)
# -----------------------------------------------------------------------------

print("\n--- Floating-Point Numbers (float) ---")

# Basic floats
pi = 3.14159
negative_float = -2.5
scientific = 2.5e10  # Scientific notation (2.5 × 10^10)

print(f"Pi: {pi}")
print(f"Negative: {negative_float}")
print(f"Scientific 2.5e10: {scientific}")
print(f"Type: {type(pi)}")

# Float precision limitations
# 中文：float 用 IEEE-754 二进制表示，0.1/0.2 这类十进制小数无法精确存储，
#       于是 0.1+0.2 得到 0.30000000000000004。这是所有语言共有的，不是 Python 的 bug。
# ⚠️ 坑：绝对不要用 == 直接比较浮点数！应判断差值是否足够小，
#        如 abs(a - b) < 1e-9，或用 math.isclose(a, b)。
print(f"\n0.1 + 0.2 = {0.1 + 0.2}")  # Not exactly 0.3!
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False!

# For precise decimal calculations, use the decimal module
# 中文：金额、计费等需要精确十进制的场景用 Decimal。
# ⚠️ 坑：必须用字符串构造 Decimal('0.1')；若写 Decimal(0.1) 会先经过不精确的 float，
#        把误差也带进来，等于白用。
from decimal import Decimal
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(f"Decimal: {d1} + {d2} = {d1 + d2}")

# Special float values
infinity = float('inf')
neg_infinity = float('-inf')
not_a_number = float('nan')

print(f"\nInfinity: {infinity}")
print(f"Negative infinity: {neg_infinity}")
print(f"NaN: {not_a_number}")
print(f"1000 < infinity: {1000 < infinity}")

# Float methods
f = 3.7
print(f"\n{f}.is_integer(): {f.is_integer()}")
print(f"4.0.is_integer(): {(4.0).is_integer()}")

# -----------------------------------------------------------------------------
# 1.3 Complex Numbers (complex)
# -----------------------------------------------------------------------------

print("\n--- Complex Numbers (complex) ---")

# Creating complex numbers
c1 = 3 + 4j
c2 = complex(2, -1)

print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"Type: {type(c1)}")

# Accessing parts
print(f"\nc1.real = {c1.real}")
print(f"c1.imag = {c1.imag}")
print(f"Conjugate of c1: {c1.conjugate()}")

# Complex arithmetic
print(f"\nc1 + c2 = {c1 + c2}")
print(f"c1 * c2 = {c1 * c2}")
print(f"abs(c1) = {abs(c1)}")  # Magnitude

# -----------------------------------------------------------------------------
# 2. Text Type (str)
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("TEXT TYPE - STRINGS")
print("=" * 60)

# Creating strings
single_quotes = 'Hello, World!'
double_quotes = "Python is awesome"
multi_line = """This is a
multi-line string"""

print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")
print(f"Multi-line:\n{multi_line}")

# String operations
s = "Hello, Python!"
print(f"\nString: '{s}'")
print(f"Length: {len(s)}")
print(f"Uppercase: {s.upper()}")
print(f"Lowercase: {s.lower()}")
print(f"Title case: {s.title()}")
print(f"Replace: {s.replace('Python', 'World')}")
print(f"Split: {s.split(', ')}")
print(f"Strip: {'  hello  '.strip()}")

# String indexing and slicing
# 中文：切片语法 s[start:stop:step]——左闭右开（含 start 不含 stop），
#       负索引从末尾数(-1 是最后一个)。s[::-1] 用步长 -1 实现整串反转，是常见惯用法。
# ⚠️ 坑：字符串不可变，s[0] = 'X' 会报错；“修改”只能生成新字符串（如 replace）。
#        另外索引越界 s[100] 会 IndexError，但切片越界 s[0:100] 不会报错、只取到末尾。
print(f"\nIndexing: s[0] = '{s[0]}', s[-1] = '{s[-1]}'")
print(f"Slicing: s[0:5] = '{s[0:5]}'")
print(f"Step: s[::2] = '{s[::2]}'")
print(f"Reverse: s[::-1] = '{s[::-1]}'")

# String methods for checking
text = "Python3"
print(f"\n'{text}'.isalnum(): {text.isalnum()}")
print(f"'python'.isalpha(): {'python'.isalpha()}")
print(f"'12345'.isdigit(): {'12345'.isdigit()}")
print(f"'hello'.islower(): {'hello'.islower()}")
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")

# String formatting
name = "Baraa"
age = 25
print(f"\nf-string: {name} is {age} years old")
print("format(): {} is {} years old".format(name, age))
# ⚠️ 坑：用 % 格式化时，想原样输出一个百分号必须写成 %%，否则 % 会被当成占位符前缀。
#        原代码这里写的 "%-formatting" 中的 %-f 被解析成了一个 float 占位符(- 是左对齐
#        标志、f 是浮点转换)，导致占位符比参数多、且把字符串塞给 %f → TypeError。
#        下面把开头的字面百分号转义为 %% 修正（这是本文件原有的一个真实 bug）。
print("%%-formatting: %s is %d years old" % (name, age))

# Escape characters
print(f"\nNewline: Hello\\nWorld → Hello\nWorld")
print(f"Tab: Hello\\tWorld → Hello\tWorld")
print("Quote: She said \"Hi!\"")

# Raw strings
print(f"\nRaw string: r'C:\\Users\\Name' → {r'C:\Users\Name'}")

# -----------------------------------------------------------------------------
# 3. Boolean Type (bool)
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("BOOLEAN TYPE")
print("=" * 60)

# Boolean values
is_active = True
is_deleted = False

print(f"is_active: {is_active}, type: {type(is_active)}")
print(f"is_deleted: {is_deleted}")

# Boolean as integers
# 中文：bool 是 int 的子类！True==1、False==0，所以能直接参与算术。
#       小技巧：sum([True, False, True]) 可统计满足条件的个数。
# ⚠️ 坑：正因 isinstance(True, int) 为 True，做严格类型判断时要留意别把布尔当普通整数。
print(f"\nTrue as int: {int(True)}")   # 1
print(f"False as int: {int(False)}")  # 0
print(f"True + True = {True + True}") # 2

# Comparison operators return booleans
x, y = 10, 5
print(f"\nx = {x}, y = {y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x >= y: {x >= y}")

# Logical operators
print(f"\nTrue and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# Truthy and Falsy values
# 中文：Python 里任何对象都能当布尔用。“假值(Falsy)”有固定一组：
#       False、0、0.0、空字符串、空容器([] {} set())、None。其余皆为“真值(Truthy)”。
#       所以判断容器非空惯用 if items: 而不是 if len(items) > 0:。
# ⚠️ 坑：当 0 也是合法值时，别用 if x: 判断“是否传了值”，会把 0 误判为“没传”；
#        这种情况要写 if x is not None:。
print("\nFalsy values (evaluate to False):")
falsy_values = [False, 0, 0.0, "", [], {}, set(), None]
for val in falsy_values:
    print(f"  bool({repr(val)}) = {bool(val)}")

print("\nTruthy values (evaluate to True):")
truthy_values = [True, 1, -1, 3.14, "hello", [1, 2], {"a": 1}]
for val in truthy_values:
    print(f"  bool({repr(val)}) = {bool(val)}")

# -----------------------------------------------------------------------------
# 4. Sequence Types
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("SEQUENCE TYPES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 4.1 Lists
# -----------------------------------------------------------------------------

print("\n--- Lists (Mutable Sequences) ---")

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"Nested: {nested}")

# List operations
fruits = ["apple", "banana", "cherry"]
print(f"\nFruits: {fruits}")
print(f"Length: {len(fruits)}")
print(f"First: {fruits[0]}, Last: {fruits[-1]}")
print(f"Slice: {fruits[1:3]}")

# Modifying lists
fruits.append("date")
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")
print(f"After insert at 1: {fruits}")

fruits.remove("banana")
print(f"After remove 'banana': {fruits}")

popped = fruits.pop()
print(f"Popped: {popped}, List: {fruits}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares (comprehension): {squares}")

# -----------------------------------------------------------------------------
# 4.2 Tuples
# -----------------------------------------------------------------------------

print("\n--- Tuples (Immutable Sequences) ---")

# Creating tuples
# ⚠️ 坑：决定“是不是元组”的是逗号，不是括号！(1,) 才是单元素元组，
#        (1) 只是被括号包住的整数 1。空元组才是 ()。
empty_tuple = ()
single = (1,)  # Note the comma
coordinates = (10, 20, 30)
mixed_tuple = (1, "two", 3.0)

print(f"Coordinates: {coordinates}")
print(f"Type: {type(coordinates)}")

# Tuple unpacking
x, y, z = coordinates
print(f"Unpacked: x={x}, y={y}, z={z}")

# Tuples are immutable
# coordinates[0] = 100  # This would raise an error

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"\nNamed tuple: {p}")
print(f"p.x = {p.x}, p.y = {p.y}")

# -----------------------------------------------------------------------------
# 4.3 Range
# -----------------------------------------------------------------------------

print("\n--- Range ---")

# Creating ranges
r1 = range(5)          # 0-4
r2 = range(1, 6)       # 1-5
r3 = range(0, 10, 2)   # 0, 2, 4, 6, 8

print(f"range(5): {list(r1)}")
print(f"range(1, 6): {list(r2)}")
print(f"range(0, 10, 2): {list(r3)}")
print(f"Type: {type(r1)}")

# Range is memory efficient
# 中文：range 不会真的生成所有数字，而是惰性地“按需计算”，所以 range(10**9) 也几乎不占内存。
#       它支持 len()、in、索引，但本身不是 list；需要列表时显式 list(r) 转换。
big_range = range(1000000)
print(f"\nrange(1000000) - Length: {len(big_range)}")
print(f"500000 in big_range: {500000 in big_range}")

# -----------------------------------------------------------------------------
# 5. Mapping Type (dict)
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("MAPPING TYPE - DICTIONARY")
print("=" * 60)

# Creating dictionaries
empty_dict = {}
person = {"name": "Baraa", "age": 25, "city": "Gaza"}
using_dict = dict(a=1, b=2, c=3)

print(f"Person: {person}")
print(f"Type: {type(person)}")

# Accessing values
# 中文：两种取值——[] 取不到 key 会抛 KeyError；.get() 取不到返回 None（或你给的默认值），
#       不会报错。读取“可能不存在”的键时优先用 .get('key', 默认值)。
print(f"\nName: {person['name']}")
print(f"Age (get): {person.get('age')}")
print(f"Country (get with default): {person.get('country', 'Unknown')}")

# Modifying dictionaries
person["email"] = "baraa@example.com"  # Add
person["age"] = 26                      # Update
print(f"\nAfter modifications: {person}")

# Dictionary methods
print(f"\nKeys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dict: {squares_dict}")

# -----------------------------------------------------------------------------
# 6. Set Types
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("SET TYPES")
print("=" * 60)

# Creating sets (mutable, unordered, unique elements)
# ⚠️ 坑：{} 创建的是“空字典”不是空集合！空集合只能用 set()。
#        有元素时 {1,2,3} 才是集合。
# 中文：集合自动去重、无序、成员判断(in)接近 O(1)，非常适合“去重”和“快速查在不在”。
# ⚠️ 坑：集合元素必须可哈希(不可变)。放 list 会 TypeError，需要时改放 tuple。
empty_set = set()  # Note: {} creates an empty dict, not set
numbers_set = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # Duplicates removed

print(f"Numbers set: {numbers_set}")
print(f"From list with duplicates: {from_list}")
print(f"Type: {type(numbers_set)}")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"\nSet A: {a}")
print(f"Set B: {b}")
print(f"Union (A | B): {a | b}")
print(f"Intersection (A & B): {a & b}")
print(f"Difference (A - B): {a - b}")
print(f"Symmetric difference (A ^ B): {a ^ b}")

# Set methods
s = {1, 2, 3}
s.add(4)
print(f"\nAfter add(4): {s}")
s.discard(2)
print(f"After discard(2): {s}")

# Frozenset (immutable set)
frozen = frozenset([1, 2, 3])
print(f"\nFrozenset: {frozen}")
# frozen.add(4)  # This would raise an error

# Sets are useful for membership testing
valid_statuses = {"active", "pending", "completed"}
user_status = "active"
print(f"\n'{user_status}' is valid: {user_status in valid_statuses}")

# -----------------------------------------------------------------------------
# 7. None Type
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("NONE TYPE")
print("=" * 60)

# None represents absence of a value
result = None

print(f"result = {result}")
print(f"Type: {type(result)}")
# 中文：None 是单例(全程只有一个 None 对象)，所以判空用 is/is not 最准也最快。
# ⚠️ 坑：别用 == None。某些自定义类可能重写 __eq__ 改变 == 行为，is None 不受影响。
print(f"result is None: {result is None}")  # Use 'is' not '=='

# Common uses of None
def greet(name=None):
    """Function with optional parameter"""
    if name is None:
        return "Hello, Guest!"
    return f"Hello, {name}!"

print(f"\ngreet(): {greet()}")
print(f"greet('Baraa'): {greet('Baraa')}")

# None as placeholder
data = None
# ... later in code ...
data = fetch_data() if False else []  # Simulated
print(f"Data initialized: {data}")

# -----------------------------------------------------------------------------
# 8. Type Checking and Conversion
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("TYPE CHECKING AND CONVERSION")
print("=" * 60)

# Using type()
values = [42, 3.14, "hello", True, [1, 2], {"a": 1}, None]
print("Type checking with type():")
for val in values:
    print(f"  {repr(val):15} -> {type(val).__name__}")

# Using isinstance() (preferred for type checking)
# 中文：isinstance 优于 type(x) == T，因为它认子类，且可传一个“类型元组”一次判断多种。
#       type(x) 是“精确类型”，isinstance 是“是不是这类(含子类)”。
print("\nType checking with isinstance():")
x = 42
print(f"isinstance(42, int): {isinstance(x, int)}")
print(f"isinstance(42, (int, float)): {isinstance(x, (int, float))}")  # 任一匹配即 True

# Type conversion summary
print("\nType Conversion Examples:")
print(f"int('42') = {int('42')}")
print(f"float('3.14') = {float('3.14')}")
print(f"str(42) = {str(42)}")
print(f"bool(1) = {bool(1)}")
print(f"list('abc') = {list('abc')}")
print(f"tuple([1,2,3]) = {tuple([1, 2, 3])}")
print(f"set([1,2,2,3]) = {set([1, 2, 2, 3])}")
print(f"dict([('a',1),('b',2)]) = {dict([('a', 1), ('b', 2)])}")

# -----------------------------------------------------------------------------
# 9. Data Type Comparison Table
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("DATA TYPE COMPARISON TABLE")
print("=" * 60)
print("""
| Type      | Mutable | Ordered | Duplicates | Example              |
|-----------|---------|---------|------------|----------------------|
| int       | No      | N/A     | N/A        | 42                   |
| float     | No      | N/A     | N/A        | 3.14                 |
| complex   | No      | N/A     | N/A        | 3+4j                 |
| str       | No      | Yes     | Yes        | "hello"              |
| bool      | No      | N/A     | N/A        | True                 |
| list      | Yes     | Yes     | Yes        | [1, 2, 3]            |
| tuple     | No      | Yes     | Yes        | (1, 2, 3)            |
| range     | No      | Yes     | No         | range(5)             |
| dict      | Yes     | Yes*    | Keys: No   | {"a": 1}             |
| set       | Yes     | No      | No         | {1, 2, 3}            |
| frozenset | No      | No      | No         | frozenset({1, 2, 3}) |
| NoneType  | No      | N/A     | N/A        | None                 |

* Dicts preserve insertion order in Python 3.7+
""")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------

print("=" * 60)
print("DATA TYPES SUMMARY")
print("=" * 60)
print("""
Numeric: int, float, complex
Text: str (immutable)
Boolean: bool (True/False)
Sequences: list (mutable), tuple (immutable), range
Mapping: dict (key-value pairs)
Sets: set (mutable), frozenset (immutable)
Special: None (absence of value)

Key Points:
1. Python is dynamically typed
2. Use type() or isinstance() to check types
3. Use appropriate type for your data
4. Mutable types can be changed, immutable cannot
5. Choose between list/tuple based on mutability needs
6. Use dict for key-value mappings
7. Use set for unique elements and fast membership tests
""")

# ============================================================================
# 【避坑总结 · 04_data_types.py】
# ----------------------------------------------------------------------------
# 1. 浮点不精确：0.1+0.2≠0.3。比较浮点用 math.isclose，精确小数用 Decimal('0.1')。
# 2. {} 是空字典不是空集合；空集合只能 set()。集合元素必须可哈希(不可变)。
# 3. 单元素元组靠逗号：(1,) 是元组，(1) 是整数。
# 4. 判空用 x is None / is not None，不要用 == None。
# 5. / 永远返回 float；// 是向下取整(负数 -17//5=-4)，% 结果符号跟随除数。
# 6. bool 是 int 子类：True==1、False==0，可参与算术，也会被 isinstance(_, int) 命中。
# 7. 字符串/元组不可变，不能按索引赋值；切片越界不报错，索引越界 IndexError。
# 8. dict 取值：[] 缺键抛 KeyError，.get() 缺键返回默认值(默认 None)。
# 9. 真值测试：空容器/0/""/None 都是假值；当 0 是合法值时用 is not None 而非 if x。
# 10. 类型判断优先 isinstance（认子类、可传类型元组），少用 type(x) == T。
# ============================================================================
