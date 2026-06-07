"""
================================================================================
File: 02_comments.py
Topic: Comments in Python
================================================================================

This file demonstrates how to write comments in Python. Comments are essential
for code documentation, making your code readable, and helping others (and
your future self) understand what the code does.

Key Concepts:
- Single-line comments
- Multi-line comments
- Docstrings
- Best practices for commenting

================================================================================
"""

# ============================================================================
# 【中文导读】注释与文档字符串（docstring）
# ----------------------------------------------------------------------------
# Python 只有一种“真注释”：以 # 开头，到行尾结束，解释器完全忽略。
# 它没有 C/Java 那种 /* ... */ 块注释。所谓“多行注释”有两种做法：
#   ① 多写几行 #（推荐，真注释）
#   ② 三引号字符串 """...""" —— 但这其实是“字符串字面量”不是注释！
#      它会被求值成一个 str 对象（只是没赋值给变量就被丢弃），并非被忽略。
#
# 学这个文件你要拿下的难点：
#   1. # 注释  vs  """字符串字面量"" 的本质区别（一个被忽略，一个被求值）
#   2. docstring：函数/类/模块的第一条字符串，可用 __doc__ 读取
#   3. 好注释解释“为什么(Why)”，而不是复述代码“做了什么(What)”
#   4. TODO/FIXME/NOTE/HACK 等约定标记，便于团队与 IDE 检索
# ============================================================================

# -----------------------------------------------------------------------------
# 1. Single-Line Comments
# -----------------------------------------------------------------------------
# Use the hash symbol (#) to create single-line comments

print("--- Single-Line Comments ---")

# This is a single-line comment
print("Hello, World!")  # This is an inline comment

# Comments can explain complex logic
x = 10  # Store the initial value
y = 20  # Store the second value
result = x + y  # Calculate the sum

# Comments can be used to organize sections of code
# ---- Configuration ----
debug_mode = True
max_retries = 3

# ---- Main Logic ----
print(f"Debug mode is: {debug_mode}")

# -----------------------------------------------------------------------------
# 2. Multi-Line Comments
# -----------------------------------------------------------------------------
# Python doesn't have true multi-line comments, but there are two approaches

print("\n--- Multi-Line Comments ---")

# Approach 1: Multiple single-line comments (preferred)
# This is a multi-line comment
# that spans across multiple lines.
# Each line starts with a hash symbol.

# Approach 2: Triple-quoted strings (not recommended for comments)
# These are actually string literals, not true comments
# 中文：下面这段三引号文本看着像注释，实则是一个 str 对象。它会被解释器“创建”
#       出来，只是没被引用而随即丢弃。和真注释 # 的区别在于：
#       - 真注释 # 在编译阶段就被剥离，运行期完全不存在；
#       - 字符串字面量是真实对象，放错位置（如循环体内）会带来无谓开销。
# ⚠️ 坑：别拿三引号当普通多行注释用。它只有作为函数/类/模块“第一条语句”时
#        才有特殊身份（docstring），其它位置只是个被浪费的字符串。
"""
This looks like a multi-line comment, but it's actually
a string literal. If not assigned to a variable,
Python will ignore it, but it's still stored in memory.
Use this approach only for docstrings.
"""

print("Multi-line comments explained above!")

# -----------------------------------------------------------------------------
# 3. Docstrings (Documentation Strings)
# -----------------------------------------------------------------------------
# Docstrings are special strings used to document modules, functions, classes

print("\n--- Docstrings ---")


# 中文：docstring 必须是函数体的“第一条语句”（紧跟 def 那行之后），
#       才会被绑定到 greet.__doc__，也是 help(greet) 显示的内容。
#       推荐遵循 Google / NumPy 风格写 Args / Returns / Raises / Examples 段落。
def greet(name):
    """
    Greet a person by their name.
    
    This function takes a person's name and prints a friendly
    greeting message to the console.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        str: A greeting message.
    
    Examples:
        >>> greet("Baraa")
        'Hello, Baraa! Welcome!'
    """
    return f"Hello, {name}! Welcome!"


# Access the docstring
print(greet("Baraa"))
# 中文：__doc__ 就是那段 docstring 字符串；[:50] 取前 50 个字符做截断展示。
# ⚠️ 坑：若函数没写 docstring，__doc__ 是 None，对 None 做切片会抛 TypeError。
print(f"Function docstring: {greet.__doc__[:50]}...")


def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The area of the rectangle.
    
    Raises:
        ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width


print(f"Area: {calculate_area(5, 3)}")

# -----------------------------------------------------------------------------
# 4. Class Docstrings
# -----------------------------------------------------------------------------

print("\n--- Class Docstrings ---")


class Rectangle:
    """
    A class to represent a rectangle.
    
    This class provides methods to calculate the area and perimeter
    of a rectangle, as well as other utility methods.
    
    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
    """
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width
    
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.length + self.width)


rect = Rectangle(10, 5)
print(f"Rectangle area: {rect.area()}")
print(f"Rectangle perimeter: {rect.perimeter()}")

# -----------------------------------------------------------------------------
# 5. Comment Best Practices
# -----------------------------------------------------------------------------

print("\n--- Comment Best Practices ---")

# ✅ GOOD: Explain WHY, not WHAT
# 中文：好注释回答“为什么这样做”（业务规则、性能权衡、坑的来由），
#       代码本身已经说清“做了什么”，无须再用注释复述。
# Calculate discount for loyalty members (15% off for 2+ years)
years_as_member = 3
discount = 0.15 if years_as_member >= 2 else 0  # 中文：三元表达式 A if 条件 else B

# ❌ BAD: Explains what the code obviously does
# 中文：下面这种把显而易见的代码再翻译一遍的注释是噪音，应删除。
# x = x + 1  # Add 1 to x

# ✅ GOOD: Document complex algorithms
# Using binary search for O(log n) time complexity
# instead of linear search O(n) for performance

# ✅ GOOD: Mark TODO items for future work
# TODO: Implement caching for better performance
# FIXME: Handle edge case when input is empty
# NOTE: This function requires Python 3.8+
# HACK: Temporary workaround for API limitation

# ✅ GOOD: Use comments for code sections
# ============================================
# DATABASE CONNECTION SETUP
# ============================================

# ============================================
# USER AUTHENTICATION
# ============================================

print("Best practices demonstrated!")

# -----------------------------------------------------------------------------
# 6. Commenting Out Code
# -----------------------------------------------------------------------------

print("\n--- Commenting Out Code ---")

# You can temporarily disable code by commenting it out
# print("This line won't execute")
# old_function()
# deprecated_code()

# Useful during debugging
value = 100
# value = 200  # Uncomment to test with different value
print(f"Current value: {value}")

# Multiple lines can be commented at once
# line_1 = "first"
# line_2 = "second"
# line_3 = "third"

# -----------------------------------------------------------------------------
# 7. Module-Level Docstrings
# -----------------------------------------------------------------------------

print("\n--- Module-Level Docstrings ---")

# At the top of a Python file, you can include a module docstring
# (like the one at the top of this file)

# Access a module's docstring
print("This module's docstring starts with:")
print(__doc__[:100] + "...")

# -----------------------------------------------------------------------------
# 8. Type Hints with Comments
# -----------------------------------------------------------------------------

print("\n--- Type Hints with Comments ---")


# 中文：参数后的 : list / : float 是“类型提示(type hint)”，-> list 是返回值类型。
#       它们只是给人和工具（IDE、mypy）看的“建议”，运行时不会强制检查类型。
# ⚠️ 坑：可变类型（如 list、dict）别用作默认值（def f(x=[])），默认值只创建一次、
#        会在多次调用间共享，导致状态污染。需要时用 None 占位再在函数体里新建。
def process_data(
    data: list,      # The input data to process
    threshold: float = 0.5,  # Minimum value to include (default: 0.5)
    verbose: bool = False    # Print progress if True
) -> list:
    """
    Process a list of numerical data.
    
    Args:
        data: List of numbers to process.
        threshold: Minimum value to include in results.
        verbose: Whether to print processing details.
    
    Returns:
        Filtered list containing only values above threshold.
    """
    if verbose:
        print(f"Processing {len(data)} items...")
    return [x for x in data if x > threshold]


result = process_data([0.1, 0.6, 0.3, 0.8, 0.4], threshold=0.5)
print(f"Filtered data: {result}")

# -----------------------------------------------------------------------------
# 9. Practical Example: Well-Commented Code
# -----------------------------------------------------------------------------

print("\n--- Practical Example ---")


def calculate_shipping_cost(weight, distance, express=False):
    """
    Calculate the shipping cost based on weight and distance.
    
    The cost is calculated using a base rate plus additional charges
    for weight and distance. Express shipping doubles the final cost.
    
    Args:
        weight (float): Package weight in kilograms.
        distance (float): Shipping distance in kilometers.
        express (bool): Whether to use express shipping.
    
    Returns:
        float: Total shipping cost in dollars.
    
    Example:
        >>> calculate_shipping_cost(2.5, 100)
        17.0
        >>> calculate_shipping_cost(2.5, 100, express=True)
        34.0
    """
    # Base shipping rate
    BASE_RATE = 5.00
    
    # Rate per kilogram of weight
    WEIGHT_RATE = 2.00
    
    # Rate per 100 kilometers
    DISTANCE_RATE = 0.05
    
    # Calculate component costs
    weight_cost = weight * WEIGHT_RATE
    distance_cost = distance * DISTANCE_RATE
    
    # Sum up total cost
    total = BASE_RATE + weight_cost + distance_cost
    
    # Apply express multiplier if applicable
    if express:
        total *= 2  # Express shipping is 2x the normal rate
    
    return round(total, 2)


# Example usage
package_weight = 3.5  # kg
shipping_distance = 250  # km

standard_cost = calculate_shipping_cost(package_weight, shipping_distance)
express_cost = calculate_shipping_cost(package_weight, shipping_distance, express=True)

print(f"Standard shipping: ${standard_cost}")
print(f"Express shipping: ${express_cost}")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("COMMENTS SUMMARY")
print("=" * 60)
print("""
1. Single-line: Use # for short comments
2. Multi-line: Use multiple # lines
3. Docstrings: Use triple quotes for documentation
4. Explain WHY, not WHAT
5. Keep comments up-to-date with code changes
6. Use TODO, FIXME, NOTE for special markers
7. Don't over-comment obvious code
""")

# ============================================================================
# 【避坑总结 · 02_comments.py】
# ----------------------------------------------------------------------------
# 1. Python 没有 /* */ 块注释；多行注释用多行 #，不要滥用三引号。
# 2. 三引号是“字符串字面量”不是注释：会被求值成对象，放错位置纯属浪费。
# 3. docstring 必须是函数/类/模块的第一条语句，才能进 __doc__、被 help() 读到。
# 4. 没写 docstring 时 __doc__ 为 None，对它切片/拼接会 TypeError。
# 5. 注释要解释 Why 不是 What；复述显而易见代码的注释是噪音。
# 6. 类型提示(: type、-> type)运行期不强制，只供工具检查。
# 7. 函数默认值别用可变对象（[]/{}），只创建一次会跨调用共享——用 None 占位。
# ============================================================================
