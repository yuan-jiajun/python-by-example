"""
================================================================================
文件：03_variables.py
主题：Python 的变量与赋值
================================================================================

本文件演示如何创建和使用变量。和很多语言不同，Python 没有“声明变量”的语句——
你给一个名字赋值的那一刻，变量就诞生了，也无需写类型。

关键心智模型：Python 的变量不是“盒子”，而是“贴在对象上的标签(名字)”。
赋值 x = 10 做的是：先创建对象 10，再让名字 x 指向它。多个名字可指向同一对象。
这条模型解释了后面所有 is / == / 可变对象共享 的行为。

Java 对比：
  - Java 要先声明类型：int x = 10;（类型属于变量）。Python 写 x = 10 即可，
    类型属于“对象”不属于“名字”，所以同一个名字可以先指向 int 再指向 str。
  - Java 的基本类型变量真的是“装值的盒子”；Python 一切皆对象、变量都是引用(标签)，
    这点更接近 Java 的“引用类型”，但连 int 也是对象。
  - Java 有 final 真常量；Python 没有，只能靠全大写命名约定 + typing.Final 提示。

学这个文件你要拿下的难点：
  1. 动态类型：同一个名字可先后指向不同类型的对象
  2. 解包赋值与星号扩展解包：a, *rest = [...]、first, *mid, last = [...]
  3. is（同一对象，比 id）  vs  ==（值相等）——别混用
  4. 小整数缓存：-5~256 被预先缓存，is 可能“意外”为 True，不可依赖
  5. global：函数内要“重新赋值”全局变量才需要它（只读取不需要）
  6. 常量靠约定（全大写）+ typing.Final，Python 没有真正的常量
================================================================================
"""

# -----------------------------------------------------------------------------
# 1. 创建变量（赋值即创建，无需声明类型）
# -----------------------------------------------------------------------------

print("--- Creating Variables ---")

# 直接赋值即可，无需写类型（Java 对比：相当于全用 var，但更彻底——连 var 都不用写）
name = "Baraa"
age = 25
height = 1.75
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")
print(f"Is student: {is_student}")

# 变量可以随时重新赋成别的值
x = 10
print(f"\nx = {x}")
x = 20
print(f"x = {x} (reassigned)")

# 甚至可以改成完全不同的类型——这就是“动态类型”：类型属于“对象”不属于“名字”。
# 所以同一个名字可先指向 int、再改指向 str。type(value).__name__ 取类型可读名。
# Java 对比：在 Java 里把 int 变量再赋成 String 会编译报错；Python 完全合法。
value = 100
print(f"\nvalue = {value} (type: {type(value).__name__})")
value = "one hundred"
print(f"value = {value} (type: {type(value).__name__})")

# -----------------------------------------------------------------------------
# 2. 变量命名规则
# -----------------------------------------------------------------------------

print("\n--- Variable Naming Rules ---")

# ✅ 合法命名（注释说明各自约定）
my_variable = 1        # snake_case 小写下划线 —— 官方推荐风格
myVariable = 2         # camelCase 合法，但不符合 Python 习惯（那是 Java 的风格）
MyVariable = 3         # PascalCase 通常留给类名
_private_var = 4       # 单下划线开头 —— 约定俗成表示“内部/私有”
__very_private = 5     # 双下划线开头 —— 触发名字改写(name mangling)
# ⚠️ 坑：双下划线开头只在“类内部”才触发名字改写(变成 _类名__名)，用来避免子类覆盖；
#        在模块/普通变量层面没有这个魔力，只是个普通名字。
# Java 对比：Python 没有 private/protected/public 关键字，可见性全靠下划线“君子约定”。
var123 = 6             # 可含数字，但不能以数字开头
CONSTANT = 7           # 全大写 —— 常量的约定

print(f"my_variable = {my_variable}")
print(f"_private_var = {_private_var}")
print(f"CONSTANT = {CONSTANT}")

# ❌ 非法命名（取消注释会报错）：
# 123var = 1       # 不能以数字开头
# my-variable = 1  # 不能含连字符
# my variable = 1  # 不能含空格
# class = 1        # 不能用保留关键字

# Python 的保留关键字（不能拿来当变量名）：
import keyword
print(f"\nPython reserved keywords: {keyword.kwlist[:10]}...")

# -----------------------------------------------------------------------------
# 3. 命名约定（PEP 8）
# -----------------------------------------------------------------------------

print("\n--- Naming Conventions (PEP 8) ---")

# 变量与函数用 snake_case（Java 用 camelCase，这是两边最显眼的风格差异之一）
user_name = "john_doe"
max_value = 100
is_active = True

# 常量用 UPPER_SNAKE_CASE
PI = 3.14159
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30

# 类名用 PascalCase（首字母大写）
# class MyClass:
#     pass

# 私有变量：单下划线开头
_internal_state = "private"

# “更私有”/名字改写：双下划线开头
__name_mangled = "mangled"

print(f"user_name: {user_name}")
print(f"PI (constant): {PI}")
print(f"MAX_CONNECTIONS (constant): {MAX_CONNECTIONS}")

# 描述性的名字优于缩写
total_price = 99.99
customer_name = "Alice"
is_logged_in = True
# ❌ 反例（别这么写）：tp = 99.99；cn = "Alice"；il = True

# -----------------------------------------------------------------------------
# 4. 多重赋值与解包
# -----------------------------------------------------------------------------

print("\n--- Multiple Variable Assignment ---")

# 把同一个值赋给多个变量（链式赋值）
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")

# 一行里给多个变量赋不同的值（右侧打包成元组，再解包给左侧）
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# 一行交换：x, y = y, x。原理是右侧先打包成临时元组 (y, x)，再整体解包给左侧，
# 所以不需要中间变量。这是 Python 惯用法。
# Java 对比：Java 必须借助临时变量 tmp = x; x = y; y = tmp;
print(f"\nBefore swap: x = {x}, y = {y}")
x, y = y, x
print(f"After swap: x = {x}, y = {y}")

# 把列表/元组解包到多个变量
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"\nUnpacked coordinates: x={x}, y={y}, z={z}")

# 带星号的“扩展解包”：星号变量贪婪地收集剩余元素，结果总是 list。
# ⚠️ 坑：一次解包里最多只能有一个带 * 的变量；元素不足以喂给非星号变量会抛 ValueError。
first, *rest = [1, 2, 3, 4, 5]
print(f"first = {first}, rest = {rest}")            # first=1, rest=[2,3,4,5]

*beginning, last = [1, 2, 3, 4, 5]
print(f"beginning = {beginning}, last = {last}")    # beginning=[1,2,3,4], last=5

first, *middle, last = [1, 2, 3, 4, 5]
print(f"first = {first}, middle = {middle}, last = {last}")  # 星号在中间也行

# -----------------------------------------------------------------------------
# 5. 变量类型与类型检查
# -----------------------------------------------------------------------------

print("\n--- Variable Types and Type Checking ---")

# Python 是动态类型，类型在运行时由对象决定
integer_var = 42
float_var = 3.14
string_var = "Hello"
bool_var = True
list_var = [1, 2, 3]
dict_var = {"key": "value"}
none_var = None

# 用 type() 查看类型
print(f"integer_var: {integer_var} -> {type(integer_var)}")
print(f"float_var: {float_var} -> {type(float_var)}")
print(f"string_var: {string_var} -> {type(string_var)}")
print(f"bool_var: {bool_var} -> {type(bool_var)}")
print(f"list_var: {list_var} -> {type(list_var)}")
print(f"dict_var: {dict_var} -> {type(dict_var)}")
print(f"none_var: {none_var} -> {type(none_var)}")

# 判断类型用 isinstance()（比 type()==T 更推荐：认子类，可一次判断多种）
# Java 对比：isinstance 类似 Java 的 instanceof，但可传一个类型元组一次匹配多个。
print(f"\nIs integer_var an int? {isinstance(integer_var, int)}")
print(f"Is string_var a str? {isinstance(string_var, str)}")
print(f"Is list_var a list? {isinstance(list_var, list)}")
print(f"Is integer_var int or float? {isinstance(integer_var, (int, float))}")

# -----------------------------------------------------------------------------
# 6. 类型转换（强制转换）
# -----------------------------------------------------------------------------

print("\n--- Type Casting ---")

# 字符串转整数（Java 对比：相当于 Integer.parseInt）
str_num = "123"
int_num = int(str_num)
print(f"'{str_num}' (str) -> {int_num} (int)")

# 字符串转浮点
str_float = "3.14"
float_num = float(str_float)
print(f"'{str_float}' (str) -> {float_num} (float)")

# 数字转字符串（Java 对比：相当于 String.valueOf）
number = 42
str_number = str(number)
print(f"{number} (int) -> '{str_number}' (str)")

# 浮点转整数：是“截断”不是四舍五入！
# ⚠️ 坑：int(3.99) == 3（直接砍掉小数）。要四舍五入用 round()。
pi = 3.99
int_pi = int(pi)
print(f"{pi} (float) -> {int_pi} (int) [truncated]")

# 布尔转换：空容器/0/""/None 为 False，其余为 True
print(f"\nbool(1) = {bool(1)}")           # True
print(f"bool(0) = {bool(0)}")             # False
print(f"bool('hello') = {bool('hello')}") # True
print(f"bool('') = {bool('')}")           # False
print(f"bool([1, 2]) = {bool([1, 2])}")   # True
print(f"bool([]) = {bool([])}")           # False

# bool 是 int 的子类：True==1、False==0
print(f"\nint(True) = {int(True)}")   # 1
print(f"int(False) = {int(False)}") # 0

# -----------------------------------------------------------------------------
# 7. 常量
# -----------------------------------------------------------------------------

print("\n--- Constants ---")

# Python 没有真正的常量，只有约定：全大写命名，且约定俗成“赋值后不再改”。
# 数学常量
PI = 3.14159265359
E = 2.71828182845
GOLDEN_RATIO = 1.61803398875

# 应用常量
MAX_USERS = 1000
API_TIMEOUT = 30
BASE_URL = "https://api.example.com"
DEBUG_MODE = False

print(f"PI = {PI}")
print(f"MAX_USERS = {MAX_USERS}")
print(f"BASE_URL = {BASE_URL}")

# 你“能”改它们（Python 不拦你），但“不该”改：
# PI = 3  # 别这么干！

# 想要更接近“常量”的效果可以用 typing.Final（Python 3.8+）。
# ⚠️ 坑：Final 只是给“类型检查器”看的告警标记，运行期照样能改，不是 Java 的 final。
from typing import Final

MAX_SIZE: Final = 100
# MAX_SIZE = 200  # 类型检查器(mypy 等)会对此告警，但运行不报错

print(f"MAX_SIZE (Final) = {MAX_SIZE}")

# -----------------------------------------------------------------------------
# 8. 变量作用域（基础）
# -----------------------------------------------------------------------------

print("\n--- Variable Scope ---")

# 全局变量
global_var = "I'm global"


def my_function():
    # 局部变量：只在函数内存在
    local_var = "I'm local"
    print(f"Inside function - global_var: {global_var}")  # 读全局：可以直接读
    print(f"Inside function - local_var: {local_var}")


my_function()
print(f"Outside function - global_var: {global_var}")
# print(local_var)  # 报错！local_var 在函数外不存在

# 在函数内“修改”全局变量
counter = 0


def increment():
    # counter += 1 是“读 + 写”，写操作会让 Python 默认把 counter 当成局部变量，
    # 于是“读”时它还没赋值 → UnboundLocalError。global 声明解除这个误判。
    # ⚠️ 坑：只“读取”全局变量不需要 global；一旦在函数里对它“赋值”就必须声明。
    #        （嵌套函数里改外层局部变量则用 nonlocal。）
    # Java 对比：Java 没有这种“默认局部”陷阱；这是 Python 作用域规则特有的坑。
    global counter
    counter += 1


print(f"\nBefore increment: counter = {counter}")
increment()
increment()
print(f"After 2 increments: counter = {counter}")

# -----------------------------------------------------------------------------
# 9. 变量的身份与内存
# -----------------------------------------------------------------------------

print("\n--- Variable Identity and Memory ---")

# id() 返回对象的身份（CPython 里约等于内存地址）
a = 10
b = 10
c = a

print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"c = {c}, id(c) = {id(c)}")

# CPython 预先缓存了 -5~256 这些小整数对象，全程复用同一个，所以 a is b 为 True。
# ⚠️ 坑：这是实现细节，不可依赖！别用 is 比较数值是否相等——比较值永远用 ==。
print(f"\na is b: {a is b}")  # True（同一个缓存对象）
print(f"a is c: {a is c}")    # True

# 超出缓存范围的大整数，每次字面量通常是新对象，is 很可能为 False，正印证上面的坑。
x = 1000
y = 1000
print(f"\nx = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

# == 比“值是否相等”，is 比“是不是同一个对象”(等价于 id 相同)。
# list3 = list1 没有拷贝，只是多贴一个标签，所以 is 为 True；改 list3 会连带改 list1。
# 需要副本用 list1.copy() 或 list1[:]。
# Java 对比：== 像 Java 的 equals（比内容），is 像 Java 的 ==（比引用）——恰好反过来，
#            这是 Java 程序员最容易混的点！
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"\nlist1 == list2: {list1 == list2}")  # True（值相同）
print(f"list1 is list2: {list1 is list2}")    # False（不同对象）
print(f"list1 is list3: {list1 is list3}")    # True（同一对象）

# -----------------------------------------------------------------------------
# 10. 删除变量
# -----------------------------------------------------------------------------

print("\n--- Deleting Variables ---")

temp_var = "I will be deleted"
print(f"temp_var exists: {temp_var}")

# del 解除“名字”与对象的绑定（删的是标签，不是直接删对象；对象在无人引用后才被回收）
del temp_var
# print(temp_var)  # 报错！NameError: name 'temp_var' is not defined

print("temp_var has been deleted")

# dir() 返回当前作用域的名字列表，可借此判断变量是否还在
if 'temp_var' not in dir():
    print("temp_var no longer exists in current scope")

# -----------------------------------------------------------------------------
# 11. 实战示例
# -----------------------------------------------------------------------------

print("\n--- Practical Examples ---")

# 示例 1：用户资料
first_name = "Baraa"
last_name = "Shaer"
full_name = f"{first_name} {last_name}"
email = f"{first_name.lower()}.{last_name.lower()}@example.com"

print(f"Full Name: {full_name}")
print(f"Email: {email}")

# 示例 2：购物车
item_price = 29.99
quantity = 3
discount_percent = 10

subtotal = item_price * quantity
discount_amount = subtotal * (discount_percent / 100)
total = subtotal - discount_amount

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Discount ({discount_percent}%): -${discount_amount:.2f}")
print(f"Total: ${total:.2f}")

# 示例 3：温度换算
celsius = 25
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"\n{celsius}°C = {fahrenheit}°F = {kelvin}K")

# -----------------------------------------------------------------------------
# 小结
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("VARIABLES SUMMARY")
print("=" * 60)
print("""
1. 变量通过赋值 (=) 创建，无需声明类型
2. Python 是动态类型
3. 变量/函数用 snake_case（PEP 8）
4. 常量用 UPPER_CASE
5. 多重赋值：x, y, z = 1, 2, 3
6. 用 type() 或 isinstance() 检查类型
7. 用 int() / str() / float() / bool() 做类型转换
8. 变量有作用域（局部 vs 全局）
9. 用 is 比身份、== 比值
10. 用 del 删除变量
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
#
# Java 老手专属提醒（最容易栽的几处）：
#   A. == 和 is 的语义跟 Java 正好“反直觉”：Python 的 == ≈ Java 的 equals(比值)，
#      Python 的 is ≈ Java 的 ==(比引用)。判断相等用 ==，判断是否同一对象/判 None 用 is。
#   B. 没有 final 真常量；全大写 + Final 都不强制，运行期照样能改。
#   C. 函数里给全局变量赋值要先 global，否则 UnboundLocalError——Java 无此坑。
#   D. 把可变对象(list/dict)赋给新名字不是拷贝，是共享引用，改一个动全部。
# ============================================================================
