"""
================================================================================
文件：02_comments.py
主题：Python 的注释与文档字符串（docstring）
================================================================================

本文件演示如何在 Python 里写注释。注释用于说明代码、提升可读性，帮助别人
（以及未来的自己）看懂代码意图。

要点：Python 只有一种“真注释”——以 # 开头、到行尾结束，解释器在编译阶段就剥离、
运行期完全不存在。它没有 Java 那种 /* ... */ 块注释。所谓“多行注释”有两种做法：
  ① 多写几行 #（推荐，真注释）
  ② 三引号字符串 \"\"\"...\"\"\" —— 但这其实是“字符串字面量”不是注释！
     它会被求值成一个 str 对象（只是没赋值给变量随即丢弃），并非被忽略。

Java 对比：
  - Java 有 //（行）、/* */（块）、/** */（Javadoc）三种；Python 只有 #，
    文档则用 docstring（紧跟定义的三引号字符串）替代 Javadoc。
  - Javadoc 靠工具从 /** */ 提取；Python 的 docstring 是运行期就能读到的真实字符串
    （对象的 __doc__ 属性），help() 直接显示它。

学这个文件你要拿下的难点：
  1. # 注释  vs  \"\"\"字符串字面量\"\"\" 的本质区别（一个被剥离，一个被求值）
  2. docstring：函数/类/模块的第一条字符串，可用 __doc__ 读取
  3. 好注释解释“为什么(Why)”，而不是复述代码“做了什么(What)”
  4. TODO/FIXME/NOTE/HACK 等约定标记，便于团队与 IDE 检索
================================================================================
"""

# -----------------------------------------------------------------------------
# 1. 单行注释（用井号 # 创建）
# -----------------------------------------------------------------------------

print("--- 单行注释 ---")

# 这是一条单独成行的注释
print("Hello, World!")  # 这是一条行尾（内联）注释；Java 对比：等同于 //

# 注释可以解释逻辑（但别复述显而易见的操作）
x = 10
y = 20
result = x + y

# 也可以用注释给代码分区（这是项目里 # ---- 标题 ---- 的由来）
# ---- 配置 ----
debug_mode = True
max_retries = 3

# ---- 主逻辑 ----
print(f"Debug mode is: {debug_mode}")

# -----------------------------------------------------------------------------
# 2. 多行注释（Python 没有真正的块注释，有两种替代做法）
# -----------------------------------------------------------------------------

print("\n--- 多行注释 ---")

# 做法一：堆叠多行单行注释（推荐，这才是真注释）
# 每行都以 # 开头，
# 一行写一句，连起来就是多行说明。

# 做法二：三引号字符串（不推荐当注释用）
# 下面这段三引号文本看着像注释，实则是一个 str 对象：解释器会真的“创建”它，
# 只是没被引用而随即丢弃。和真注释 # 的区别在于——
#   - 真注释 # 在编译阶段就被剥离，运行期完全不存在；
#   - 字符串字面量是真实对象，放错位置（如循环体内）会带来无谓开销。
# ⚠️ 坑：别拿三引号当普通多行注释。它只有作为函数/类/模块“第一条语句”时
#        才有特殊身份（docstring），其它位置只是个被浪费的字符串。
"""
这看起来像多行注释，其实是个字符串字面量。
没赋值给变量时 Python 会忽略它的值，但它仍然被创建过。
这种写法只应该用于 docstring。
"""

print("Multi-line comments explained above!")

# -----------------------------------------------------------------------------
# 3. 文档字符串 docstring（给模块/函数/类写文档的专用字符串）
# -----------------------------------------------------------------------------

print("\n--- Docstrings ---")


# docstring 必须是函数体的“第一条语句”（紧跟 def 那行之后），才会被绑定到
# greet.__doc__，也是 help(greet) 显示的内容。推荐用 Google / NumPy 风格写
# Args / Returns / Raises / Examples 段落。
# Java 对比：这相当于 Javadoc，但 Javadoc 是注释靠工具提取，docstring 是运行期
#            可访问的真实字符串对象。
def greet(name):
    """
    按名字向某人问好。

    参数:
        name (str): 要问候的人名。

    返回:
        str: 一句问候语。

    示例:
        >>> greet("Baraa")
        'Hello, Baraa! Welcome!'
    """
    return f"Hello, {name}! Welcome!"


# __doc__ 就是上面那段 docstring 字符串；[:50] 取前 50 个字符做截断展示。
# ⚠️ 坑：若函数没写 docstring，__doc__ 是 None，对 None 做切片会抛 TypeError。
print(greet("Baraa"))
print(f"Function docstring: {greet.__doc__[:50]}...")


def calculate_area(length, width):
    """
    计算矩形面积。

    参数:
        length (float): 矩形的长。
        width (float): 矩形的宽。

    返回:
        float: 矩形面积。

    异常:
        ValueError: 当长或宽为负数时抛出。
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width


print(f"Area: {calculate_area(5, 3)}")

# -----------------------------------------------------------------------------
# 4. 类的 docstring
# -----------------------------------------------------------------------------

print("\n--- Class Docstrings ---")


class Rectangle:
    """
    表示一个矩形的类。

    提供计算面积、周长等方法。

    属性:
        length (float): 矩形的长。
        width (float): 矩形的宽。

    方法:
        area(): 返回面积。
        perimeter(): 返回周长。
    """

    # __init__ 是构造方法；Java 对比：相当于构造器，但名字固定叫 __init__，
    # 且第一个参数 self（≈ Java 的 this）必须显式写出来。
    def __init__(self, length, width):
        """初始化一个 Rectangle 实例。"""
        self.length = length
        self.width = width

    def area(self):
        """计算并返回矩形面积。"""
        return self.length * self.width

    def perimeter(self):
        """计算并返回矩形周长。"""
        return 2 * (self.length + self.width)


rect = Rectangle(10, 5)
print(f"Rectangle area: {rect.area()}")
print(f"Rectangle perimeter: {rect.perimeter()}")

# -----------------------------------------------------------------------------
# 5. 注释的最佳实践
# -----------------------------------------------------------------------------

print("\n--- Comment Best Practices ---")

# ✅ 好注释解释“为什么(Why)”：业务规则、性能权衡、坑的来由。
#    代码本身已说清“做了什么(What)”，无须再复述。
# 例：为忠诚会员计算折扣（满 2 年享 15% off）
years_as_member = 3
discount = 0.15 if years_as_member >= 2 else 0  # 三元表达式：A if 条件 else B（注意顺序和 Java 的 ?: 不同）

# ❌ 坏注释把显而易见的代码再翻译一遍，是噪音，应删除：
# x = x + 1  # 给 x 加 1

# ✅ 复杂算法值得注释清楚思路：
# 用二分查找把复杂度从 O(n) 降到 O(log n)

# ✅ 用约定标记待办事项，IDE 能高亮/检索（Java 里也有同样约定）：
# TODO: 加缓存提升性能
# FIXME: 处理输入为空的边界情况
# NOTE: 本函数需要 Python 3.8+
# HACK: 针对某 API 限制的临时绕过

# ✅ 用注释做大分区：
# ============================================
# 数据库连接初始化
# ============================================

print("Best practices demonstrated!")

# -----------------------------------------------------------------------------
# 6. 注释掉代码（临时禁用）
# -----------------------------------------------------------------------------

print("\n--- Commenting Out Code ---")

# 在代码前加 # 即可临时禁用它（调试常用）：
# print("这行不会执行")
# old_function()

value = 100
# value = 200  # 取消注释即可换个值测试
print(f"Current value: {value}")
# 小技巧：IDE 里多行选中后按 Ctrl/Cmd + / 可批量注释，和 Java IDE 一样。

# -----------------------------------------------------------------------------
# 7. 模块级 docstring
# -----------------------------------------------------------------------------

print("\n--- Module-Level Docstrings ---")

# 文件最顶端的那段三引号字符串就是“模块 docstring”（即本文件开头那段），
# 运行期可通过模块的 __doc__ 读到它。
print("This module's docstring starts with:")
print(__doc__[:100] + "...")

# -----------------------------------------------------------------------------
# 8. 类型提示与参数注释
# -----------------------------------------------------------------------------

print("\n--- Type Hints with Comments ---")


# 参数后的 : list / : float 是“类型提示(type hint)”，-> list 是返回值类型。
# 它们只是给人和工具（IDE、mypy）看的“建议”，运行时不会强制检查类型。
# Java 对比：Java 的类型是强制的、编译期检查；Python 的类型提示是可选的、不强制，
#            纯属文档 + 静态检查器的素材，运行时传错类型并不会报错。
# ⚠️ 坑：可变类型（如 list、dict）别用作默认值（def f(x=[])）！默认值只在定义时
#        创建一次，会在多次调用间共享，导致状态污染。需要时用 None 占位再在体内新建。
def process_data(
    data: list,              # 待处理的输入数据
    threshold: float = 0.5,  # 纳入结果的最小阈值（默认 0.5）
    verbose: bool = False    # 为 True 时打印进度
) -> list:
    """处理一组数值，返回所有大于 threshold 的元素。"""
    if verbose:
        print(f"Processing {len(data)} items...")
    return [x for x in data if x > threshold]


result = process_data([0.1, 0.6, 0.3, 0.8, 0.4], threshold=0.5)
print(f"Filtered data: {result}")

# -----------------------------------------------------------------------------
# 9. 实战示例：注释得当的代码
# -----------------------------------------------------------------------------

print("\n--- Practical Example ---")


def calculate_shipping_cost(weight, distance, express=False):
    """
    根据重量和距离计算运费。

    运费 = 基础费 + 重量费 + 距离费；加急(express)会让总额翻倍。

    参数:
        weight (float): 包裹重量（千克）。
        distance (float): 运输距离（千米）。
        express (bool): 是否加急。

    返回:
        float: 运费（美元）。

    示例:
        >>> calculate_shipping_cost(2.5, 100)
        17.0
    """
    # 这几个全大写名字是“常量”约定（Python 没有真正的 final 常量）
    # Java 对比：相当于 final 字段，但 Python 不强制，靠命名约定提醒别改。
    BASE_RATE = 5.00       # 基础费
    WEIGHT_RATE = 2.00     # 每千克费率
    DISTANCE_RATE = 0.05   # 每千米费率

    # 分别算出各部分费用再求和
    weight_cost = weight * WEIGHT_RATE
    distance_cost = distance * DISTANCE_RATE
    total = BASE_RATE + weight_cost + distance_cost

    if express:
        total *= 2  # 加急是普通价的 2 倍

    return round(total, 2)


package_weight = 3.5      # 千克
shipping_distance = 250   # 千米

standard_cost = calculate_shipping_cost(package_weight, shipping_distance)
express_cost = calculate_shipping_cost(package_weight, shipping_distance, express=True)

print(f"Standard shipping: ${standard_cost}")
print(f"Express shipping: ${express_cost}")

# -----------------------------------------------------------------------------
# 小结
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("COMMENTS SUMMARY")
print("=" * 60)
print("""
1. 单行注释：用 # 写简短说明
2. 多行注释：堆叠多行 #
3. 文档：用三引号 docstring（不是普通多行注释）
4. 解释“为什么”，不要复述“做了什么”
5. 改代码时同步更新注释，别留过时注释
6. 用 TODO / FIXME / NOTE 等标记特殊事项
7. 不要给显而易见的代码过度注释
""")

# ============================================================================
# 【避坑总结 · 02_comments.py】
# ----------------------------------------------------------------------------
# 1. Python 没有 /* */ 块注释；多行注释堆叠 #，不要滥用三引号。
# 2. 三引号是“字符串字面量”不是注释：会被求值成对象，放错位置纯属浪费。
# 3. docstring 必须是函数/类/模块的第一条语句，才能进 __doc__、被 help() 读到。
# 4. 没写 docstring 时 __doc__ 为 None，对它切片/拼接会 TypeError。
# 5. 注释要解释 Why 不是 What；复述显而易见代码的注释是噪音。
# 6. 类型提示(: type、-> type)运行期不强制，只供工具检查（不像 Java 强类型）。
# 7. 函数默认值别用可变对象（[]/{}），只创建一次会跨调用共享——用 None 占位。
#
# Java 老手专属提醒：
#   A. // 和 /* */ 在 Python 都没有，只有 #；文档用 docstring 代替 Javadoc。
#   B. docstring 是运行期真实字符串(__doc__)，不是被工具提取的注释。
#   C. 类型提示是“建议”不是“契约”：运行时不校验，别当 Java 强类型依赖。
# ============================================================================
