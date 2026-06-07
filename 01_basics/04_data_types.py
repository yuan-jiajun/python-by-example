"""
================================================================================
文件：04_data_types.py
主题：Python 的内置数据类型
================================================================================

本文件横扫 Python 全部内置类型——它们决定了数据能做哪些操作、如何存储。

贯穿始终的一条主线是“可变 vs 不可变”：
  - 不可变(immutable)：int float complex str bool tuple frozenset range None
  - 可变(mutable)：    list dict set
不可变对象“改值”其实是生成新对象、名字改指向；可变对象可原地修改。
这条主线决定了能不能做字典的 key、函数默认值能不能用、要不要拷贝等一系列问题。

Java 对比：
  - Python 没有 int/double 这种“基本类型 vs 包装类”之分，一切皆对象（连整数也是）。
  - Python 的 int 任意精度，不会溢出；Java 的 int/long 有固定位宽，溢出要靠 BigInteger。
  - list ≈ ArrayList，dict ≈ HashMap，set ≈ HashSet，tuple ≈ 不可变的定长记录。
  - == 比“值”(类似 Java 的 equals)，is 比“是不是同一对象”(类似 Java 的 ==)，别搞反。

学这个文件你要拿下的难点 / 高频坑：
  1. 浮点精度：0.1 + 0.2 != 0.3，需要精确小数用 decimal.Decimal('0.1')
  2. {} 是空字典不是空集合；空集合只能 set()
  3. 单元素元组靠逗号：(1,) 才是元组，(1) 只是带括号的整数
  4. 判空用 x is None，不要用 == None
  5. 整数除法：/ 永远返回 float，// 是向下取整的整除
  6. type(x) 精确匹配类型；isinstance(x, ...) 更推荐（认子类、可传类型元组）
================================================================================
"""

# -----------------------------------------------------------------------------
# 1. 数值类型概览
# -----------------------------------------------------------------------------

print("=" * 60)
print("NUMERIC TYPES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1.1 整数 int
# -----------------------------------------------------------------------------

print("\n--- Integers (int) ---")

# 基本整数
positive_int = 42
negative_int = -17
zero = 0

print(f"Positive: {positive_int}")
print(f"Negative: {negative_int}")
print(f"Zero: {zero}")

# Python 的 int 是“任意精度”(big integer)，没有 32/64 位上限，多大都不会像 Java 那样
# 溢出，运算自动扩展——这是 Python 的一大特点。
# Java 对比：Java 要用 BigInteger 才能做大整数，且要用方法 add()/multiply() 而非 +/*。
big_number = 123456789012345678901234567890
print(f"Big number: {big_number}")
print(f"Type: {type(big_number)}")

# 不同进制的整数字面量（0b 二进制 / 0o 八进制 / 0x 十六进制，和 Java 写法基本一致）
binary = 0b1010      # 二进制
octal = 0o17         # 八进制
hexadecimal = 0xFF   # 十六进制

print(f"\nBinary 0b1010 = {binary}")
print(f"Octal 0o17 = {octal}")
print(f"Hex 0xFF = {hexadecimal}")

# 数字里可用下划线分组提升可读性（Python 3.6+，和 Java 的 1_000_000 一样）
million = 1_000_000
credit_card = 1234_5678_9012_3456
print(f"\nMillion: {million}")
print(f"Credit card: {credit_card}")

# 整数运算
a, b = 17, 5
print(f"\na = {a}, b = {b}")
print(f"a + b = {a + b}")    # 加
print(f"a - b = {a - b}")    # 减
print(f"a * b = {a * b}")    # 乘
print(f"a / b = {a / b}")    # 除（返回 float）
# ⚠️ 坑：单斜杠 / 永远返回 float，17/5=3.4；即使整除 4/2 结果也是 2.0 而非 2。要整数用 //。
# Java 对比：Java 里 17/5==3（整数除法默认截断）；Python 必须用 // 才能得到整数除法。
print(f"a // b = {a // b}")  # 整除（向下取整）
# ⚠️ 坑：// 是“向下取整”不是“截断向零”。负数时 -17 // 5 == -4（不是 -3）；
#        同理 % 的结果符号跟随除数：-17 % 5 == 3（Java 的 % 跟随被除数，结果会是 -2，这点不同！）。
print(f"a % b = {a % b}")    # 取余
print(f"a ** b = {a ** b}")  # 幂运算 a 的 b 次方（Java 要用 Math.pow，且返回 double）

# -----------------------------------------------------------------------------
# 1.2 浮点数 float
# -----------------------------------------------------------------------------

print("\n--- Floating-Point Numbers (float) ---")

# 基本浮点
pi = 3.14159
negative_float = -2.5
scientific = 2.5e10  # 科学计数法（2.5 × 10^10）

print(f"Pi: {pi}")
print(f"Negative: {negative_float}")
print(f"Scientific 2.5e10: {scientific}")
print(f"Type: {type(pi)}")

# float 用 IEEE-754 二进制表示，0.1/0.2 这类十进制小数无法精确存储，
# 于是 0.1+0.2 得到 0.30000000000000004。这是所有语言共有的(Java 的 double 一样)，不是 bug。
# ⚠️ 坑：绝对不要用 == 直接比较浮点数！应判断差值是否足够小，
#        如 abs(a - b) < 1e-9，或用 math.isclose(a, b)。
print(f"\n0.1 + 0.2 = {0.1 + 0.2}")  # 不是恰好 0.3！
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")  # False！

# 金额、计费等需要精确十进制的场景用 Decimal（Java 对比：相当于 BigDecimal）。
# ⚠️ 坑：必须用字符串构造 Decimal('0.1')；若写 Decimal(0.1) 会先经过不精确的 float，
#        把误差也带进来，等于白用。
from decimal import Decimal
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(f"Decimal: {d1} + {d2} = {d1 + d2}")

# 特殊浮点值：正负无穷与 NaN（非数字）
infinity = float('inf')
neg_infinity = float('-inf')
not_a_number = float('nan')

print(f"\nInfinity: {infinity}")
print(f"Negative infinity: {neg_infinity}")
print(f"NaN: {not_a_number}")
print(f"1000 < infinity: {1000 < infinity}")

# 浮点方法：is_integer() 判断是否为整数值
f = 3.7
print(f"\n{f}.is_integer(): {f.is_integer()}")
print(f"4.0.is_integer(): {(4.0).is_integer()}")

# -----------------------------------------------------------------------------
# 1.3 复数 complex
# -----------------------------------------------------------------------------

print("\n--- Complex Numbers (complex) ---")

# 复数：虚部用 j 表示（Java 标准库没有内置复数类型，这是 Python 的特色）
c1 = 3 + 4j
c2 = complex(2, -1)

print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"Type: {type(c1)}")

# 访问实部/虚部/共轭
print(f"\nc1.real = {c1.real}")
print(f"c1.imag = {c1.imag}")
print(f"Conjugate of c1: {c1.conjugate()}")

# 复数运算
print(f"\nc1 + c2 = {c1 + c2}")
print(f"c1 * c2 = {c1 * c2}")
print(f"abs(c1) = {abs(c1)}")  # 模长

# -----------------------------------------------------------------------------
# 2. 文本类型 str
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("TEXT TYPE - STRINGS")
print("=" * 60)

# 创建字符串：单引号、双引号等价；三引号可跨行
# Java 对比：Java 区分 char(单引号) 和 String(双引号)；Python 没有 char，单/双引号都是 str。
single_quotes = 'Hello, World!'
double_quotes = "Python is awesome"
multi_line = """This is a
multi-line string"""

print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")
print(f"Multi-line:\n{multi_line}")

# 常用字符串操作（Java 对比：方法名很像，但 Python 是 snake/全小写：upper/lower/strip）
s = "Hello, Python!"
print(f"\nString: '{s}'")
print(f"Length: {len(s)}")            # len(s) 而非 s.length()
print(f"Uppercase: {s.upper()}")
print(f"Lowercase: {s.lower()}")
print(f"Title case: {s.title()}")
print(f"Replace: {s.replace('Python', 'World')}")
print(f"Split: {s.split(', ')}")
print(f"Strip: {'  hello  '.strip()}")  # 去首尾空白，相当于 Java 的 trim()/strip()

# 字符串索引与切片：s[start:stop:step]——左闭右开（含 start 不含 stop），
# 负索引从末尾数(-1 是最后一个)。s[::-1] 用步长 -1 实现整串反转，是常见惯用法。
# Java 对比：Java 用 charAt/substring 且没有负索引、没有切片步长，Python 的切片强大得多。
# ⚠️ 坑：字符串不可变，s[0] = 'X' 会报错；“修改”只能生成新字符串（如 replace）。
#        另外索引越界 s[100] 会 IndexError，但切片越界 s[0:100] 不会报错、只取到末尾。
print(f"\nIndexing: s[0] = '{s[0]}', s[-1] = '{s[-1]}'")
print(f"Slicing: s[0:5] = '{s[0:5]}'")
print(f"Step: s[::2] = '{s[::2]}'")
print(f"Reverse: s[::-1] = '{s[::-1]}'")

# 判断类方法
text = "Python3"
print(f"\n'{text}'.isalnum(): {text.isalnum()}")
print(f"'python'.isalpha(): {'python'.isalpha()}")
print(f"'12345'.isdigit(): {'12345'.isdigit()}")
print(f"'hello'.islower(): {'hello'.islower()}")
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")

# 三种格式化（详见 01_print.py），优先 f-string
name = "Baraa"
age = 25
print(f"\nf-string: {name} is {age} years old")
print("format(): {} is {} years old".format(name, age))
# ⚠️ 坑：用 % 格式化时，想原样输出一个百分号必须写成 %%，否则 % 会被当成占位符前缀。
#        原代码这里写的 "%-formatting" 中的 %-f 被解析成了一个 float 占位符(- 是左对齐
#        标志、f 是浮点转换)，导致占位符比参数多、且把字符串塞给 %f → TypeError。
#        下面把开头的字面百分号转义为 %% 修正（这是本文件原有的一个真实 bug）。
print("%%-formatting: %s is %d years old" % (name, age))

# 转义字符（与 Java 一致：\n \t \"）
print(f"\nNewline: Hello\\nWorld → Hello\nWorld")
print(f"Tab: Hello\\tWorld → Hello\tWorld")
print("Quote: She said \"Hi!\"")

# 原始字符串 r"..."：关闭转义（Java 没有，正则里只能写 \\）
print(f"\nRaw string: r'C:\\Users\\Name' → {r'C:\Users\Name'}")

# -----------------------------------------------------------------------------
# 3. 布尔类型 bool
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("BOOLEAN TYPE")
print("=" * 60)

# 布尔值首字母大写：True / False（Java 是小写 true/false，写错大小写是常见笔误）
is_active = True
is_deleted = False

print(f"is_active: {is_active}, type: {type(is_active)}")
print(f"is_deleted: {is_deleted}")

# bool 是 int 的子类！True==1、False==0，所以能直接参与算术。
# 小技巧：sum([True, False, True]) 可统计满足条件的个数。
# ⚠️ 坑：正因 isinstance(True, int) 为 True，做严格类型判断时别把布尔当普通整数。
# Java 对比：Java 的 boolean 完全独立，绝不能和 int 互转；Python 里布尔就是特殊的整数。
print(f"\nTrue as int: {int(True)}")   # 1
print(f"False as int: {int(False)}")  # 0
print(f"True + True = {True + True}") # 2

# 比较运算符返回布尔
x, y = 10, 5
print(f"\nx = {x}, y = {y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x >= y: {x >= y}")

# 逻辑运算符用英文单词 and / or / not（Java 是 && || !）
print(f"\nTrue and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# 真值/假值：Python 里任何对象都能当布尔用。“假值(Falsy)”有固定一组：
# False、0、0.0、空字符串、空容器([] {} set())、None；其余皆为“真值(Truthy)”。
# 所以判断容器非空惯用 if items: 而不是 if len(items) > 0:。
# Java 对比：Java 的 if 只接受 boolean，写 if (list) 编译不过；Python 容器可直接当条件。
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
# 4. 序列类型
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("SEQUENCE TYPES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 4.1 列表 list（可变序列）
# -----------------------------------------------------------------------------

print("\n--- Lists (Mutable Sequences) ---")

# 创建列表（Java 对比：≈ ArrayList，但可混装不同类型，因为元素都是对象引用）
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True, None]   # 元素类型可以不一致
nested = [[1, 2], [3, 4], [5, 6]]

print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"Nested: {nested}")

# 列表的基本操作
fruits = ["apple", "banana", "cherry"]
print(f"\nFruits: {fruits}")
print(f"Length: {len(fruits)}")
print(f"First: {fruits[0]}, Last: {fruits[-1]}")  # 负索引取倒数，Java 没有
print(f"Slice: {fruits[1:3]}")

# 修改列表（这些方法会“原地”改动列表本身）
fruits.append("date")                  # 末尾追加，≈ add()
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")          # 指定位置插入
print(f"After insert at 1: {fruits}")

fruits.remove("banana")                # 按值删除（删第一个匹配）
print(f"After remove 'banana': {fruits}")

popped = fruits.pop()                  # 弹出并返回末尾元素
print(f"Popped: {popped}, List: {fruits}")

# 列表推导式：一行生成列表（Java 要用 Stream.map().collect()，Python 更简洁）
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares (comprehension): {squares}")

# -----------------------------------------------------------------------------
# 4.2 元组 tuple（不可变序列）
# -----------------------------------------------------------------------------

print("\n--- Tuples (Immutable Sequences) ---")

# 创建元组
# ⚠️ 坑：决定“是不是元组”的是逗号，不是括号！(1,) 才是单元素元组，
#        (1) 只是被括号包住的整数 1。空元组才是 ()。
empty_tuple = ()
single = (1,)              # 注意这个逗号
coordinates = (10, 20, 30)
mixed_tuple = (1, "two", 3.0)

print(f"Coordinates: {coordinates}")
print(f"Type: {type(coordinates)}")

# 元组解包
x, y, z = coordinates
print(f"Unpacked: x={x}, y={y}, z={z}")

# 元组不可变（下面这行会报错）：
# coordinates[0] = 100

# 具名元组：给字段起名字，像个轻量不可变记录
# Java 对比：很像 Java 16 的 record，只读、按字段名访问。
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"\nNamed tuple: {p}")
print(f"p.x = {p.x}, p.y = {p.y}")

# -----------------------------------------------------------------------------
# 4.3 range（数字区间）
# -----------------------------------------------------------------------------

print("\n--- Range ---")

# range(stop) / range(start, stop) / range(start, stop, step)，都是左闭右开
r1 = range(5)          # 0~4
r2 = range(1, 6)       # 1~5
r3 = range(0, 10, 2)   # 0, 2, 4, 6, 8

print(f"range(5): {list(r1)}")
print(f"range(1, 6): {list(r2)}")
print(f"range(0, 10, 2): {list(r3)}")
print(f"Type: {type(r1)}")

# range 不会真的生成所有数字，而是惰性“按需计算”，所以 range(10**9) 也几乎不占内存。
# 它支持 len()、in、索引，但本身不是 list；需要列表时显式 list(r) 转换。
# Java 对比：相当于 for (int i=0; i<n; i++) 的计数循环，但 range 是个可复用的对象。
big_range = range(1000000)
print(f"\nrange(1000000) - Length: {len(big_range)}")
print(f"500000 in big_range: {500000 in big_range}")

# -----------------------------------------------------------------------------
# 5. 映射类型 dict（字典）
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("MAPPING TYPE - DICTIONARY")
print("=" * 60)

# 创建字典（Java 对比：≈ HashMap，但字面量语法 {k: v} 更轻；3.7+ 保持插入顺序）
empty_dict = {}
person = {"name": "Baraa", "age": 25, "city": "Gaza"}
using_dict = dict(a=1, b=2, c=3)

print(f"Person: {person}")
print(f"Type: {type(person)}")

# 两种取值：[] 取不到 key 会抛 KeyError；.get() 取不到返回 None（或你给的默认值），
# 不会报错。读取“可能不存在”的键时优先用 .get('key', 默认值)。
# Java 对比：person['name'] ≈ get 但缺键会抛异常；.get('k', default) ≈ getOrDefault。
print(f"\nName: {person['name']}")
print(f"Age (get): {person.get('age')}")
print(f"Country (get with default): {person.get('country', 'Unknown')}")

# 修改字典：键不存在则新增，存在则更新（统一用 d[key] = value）
person["email"] = "baraa@example.com"  # 新增
person["age"] = 26                      # 更新
print(f"\nAfter modifications: {person}")

# 遍历用的视图
print(f"\nKeys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")  # 键值对，常配合 for k, v in d.items()

# 字典推导式
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dict: {squares_dict}")

# -----------------------------------------------------------------------------
# 6. 集合类型 set
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("SET TYPES")
print("=" * 60)

# 集合：可变、无序、元素唯一（Java 对比：≈ HashSet）
# ⚠️ 坑：{} 创建的是“空字典”不是空集合！空集合只能用 set()；有元素时 {1,2,3} 才是集合。
# 集合自动去重、成员判断(in)接近 O(1)，非常适合“去重”和“快速查在不在”。
# ⚠️ 坑：集合元素必须可哈希(不可变)。放 list 会 TypeError，需要时改放 tuple。
empty_set = set()
numbers_set = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # 重复元素自动去掉

print(f"Numbers set: {numbers_set}")
print(f"From list with duplicates: {from_list}")
print(f"Type: {type(numbers_set)}")

# 集合运算：并 | 交 & 差 - 对称差 ^（Java 要调 addAll/retainAll/removeAll，Python 用运算符）
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"\nSet A: {a}")
print(f"Set B: {b}")
print(f"Union (A | B): {a | b}")
print(f"Intersection (A & B): {a & b}")
print(f"Difference (A - B): {a - b}")
print(f"Symmetric difference (A ^ B): {a ^ b}")

# 集合方法
s = {1, 2, 3}
s.add(4)
print(f"\nAfter add(4): {s}")
s.discard(2)  # discard 删不存在的元素不报错；remove 则会 KeyError
print(f"After discard(2): {s}")

# frozenset：不可变集合，可作为字典 key 或放进别的集合
frozen = frozenset([1, 2, 3])
print(f"\nFrozenset: {frozen}")
# frozen.add(4)  # 会报错

# 集合非常适合成员判断
valid_statuses = {"active", "pending", "completed"}
user_status = "active"
print(f"\n'{user_status}' is valid: {user_status in valid_statuses}")

# -----------------------------------------------------------------------------
# 7. 空值类型 None
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("NONE TYPE")
print("=" * 60)

# None 表示“没有值”（Java 对比：≈ null，但 None 是个真正的单例对象，类型是 NoneType）
result = None

print(f"result = {result}")
print(f"Type: {type(result)}")
# None 是单例(全程只有一个 None 对象)，所以判空用 is/is not 最准也最快。
# ⚠️ 坑：别用 == None。某些自定义类可能重写 __eq__ 改变 == 行为，is None 不受影响。
print(f"result is None: {result is None}")  # 用 is 而不是 ==

# None 常用作可选参数的默认值
def greet(name=None):
    """带可选参数的函数：name 缺省时走默认问候。"""
    if name is None:
        return "Hello, Guest!"
    return f"Hello, {name}!"

print(f"\ngreet(): {greet()}")
print(f"greet('Baraa'): {greet('Baraa')}")

# None 也常用作占位（先声明，稍后赋真值）
data = None
# ... 之后的代码里 ...
data = fetch_data() if False else []  # 此处仅作演示（条件为 False，不会真的调用 fetch_data）
print(f"Data initialized: {data}")

# -----------------------------------------------------------------------------
# 8. 类型检查与转换
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("TYPE CHECKING AND CONVERSION")
print("=" * 60)

# 用 type() 看精确类型
values = [42, 3.14, "hello", True, [1, 2], {"a": 1}, None]
print("Type checking with type():")
for val in values:
    print(f"  {repr(val):15} -> {type(val).__name__}")

# isinstance 优于 type(x) == T：它认子类，且可传一个“类型元组”一次判断多种。
# type(x) 是“精确类型”，isinstance 是“是不是这类(含子类)”。
# Java 对比：isinstance ≈ instanceof，但可一次匹配多个类型。
print("\nType checking with isinstance():")
x = 42
print(f"isinstance(42, int): {isinstance(x, int)}")
print(f"isinstance(42, (int, float)): {isinstance(x, (int, float))}")  # 任一匹配即 True

# 类型转换汇总（Java 对比：相当于 Integer.parseInt / String.valueOf 等，但写法统一为 T(x)）
print("\nType Conversion Examples:")
print(f"int('42') = {int('42')}")
print(f"float('3.14') = {float('3.14')}")
print(f"str(42) = {str(42)}")
print(f"bool(1) = {bool(1)}")
print(f"list('abc') = {list('abc')}")           # 字符串可拆成字符列表
print(f"tuple([1,2,3]) = {tuple([1, 2, 3])}")
print(f"set([1,2,2,3]) = {set([1, 2, 2, 3])}")  # 顺带去重
print(f"dict([('a',1),('b',2)]) = {dict([('a', 1), ('b', 2)])}")

# -----------------------------------------------------------------------------
# 9. 数据类型对照表
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("DATA TYPE COMPARISON TABLE")
print("=" * 60)
print("""
| 类型      | 可变 | 有序 | 可重复 | 示例                 |
|-----------|------|------|--------|----------------------|
| int       | 否   | -    | -      | 42                   |
| float     | 否   | -    | -      | 3.14                 |
| complex   | 否   | -    | -      | 3+4j                 |
| str       | 否   | 是   | 是     | "hello"              |
| bool      | 否   | -    | -      | True                 |
| list      | 是   | 是   | 是     | [1, 2, 3]            |
| tuple     | 否   | 是   | 是     | (1, 2, 3)            |
| range     | 否   | 是   | 否     | range(5)             |
| dict      | 是   | 是*  | 键: 否 | {"a": 1}             |
| set       | 是   | 否   | 否     | {1, 2, 3}            |
| frozenset | 否   | 否   | 否     | frozenset({1, 2, 3}) |
| NoneType  | 否   | -    | -      | None                 |

* 字典在 Python 3.7+ 保持插入顺序
""")

# -----------------------------------------------------------------------------
# 小结
# -----------------------------------------------------------------------------

print("=" * 60)
print("DATA TYPES SUMMARY")
print("=" * 60)
print("""
数值: int, float, complex
文本: str（不可变）
布尔: bool（True/False）
序列: list（可变）, tuple（不可变）, range
映射: dict（键值对）
集合: set（可变）, frozenset（不可变）
特殊: None（表示没有值）

关键要点:
1. Python 是动态类型
2. 用 type() 或 isinstance() 检查类型
3. 为数据选择合适的类型
4. 可变类型能原地改，不可变类型不能
5. 在 list / tuple 间按“是否需要可变”来选
6. 键值映射用 dict
7. 去重和快速成员判断用 set
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
#
# Java 老手专属提醒：
#   A. int 任意精度不溢出；整数除法要用 //（/ 永远给 float），% 对负数的符号规则和 Java 不同。
#   B. == 比值(≈equals)、is 比对象(≈Java 的 ==)；判 None 用 is，这是最易踩反的点。
#   C. bool 是 int 子类、布尔字面量大写 True/False；容器可直接当 if 条件（空即假）。
#   D. 没有 char；list≈ArrayList、dict≈HashMap、set≈HashSet、namedtuple≈record。
# ============================================================================
