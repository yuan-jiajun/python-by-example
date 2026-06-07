"""
================================================================================
File: 01_print.py
Topic: The print() Function in Python
================================================================================

This file demonstrates the print() function, which is used to display output
to the console. It's one of the most fundamental functions in Python and
essential for debugging and displaying information.

Key Concepts:
- Basic printing
- Multiple arguments
- Separators and end characters
- Formatted strings (f-strings)
- Escape characters

================================================================================
"""

# ============================================================================
# 【中文导读】print() 输出函数
# ----------------------------------------------------------------------------
# print 是 Python 最常用的内建函数。完整签名其实是：
#     print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#   - *objects：要打印的任意多个值（用逗号隔开）
#   - sep：多个值之间的分隔符，默认一个空格
#   - end：打印结束后追加的字符，默认换行 '\n'
#   - file：输出到哪里，默认标准输出；可改成文件对象
#   - flush：是否立即刷新缓冲区（做进度条/实时输出时常用 flush=True）
#
# 学这个文件你要拿下的难点：
#   1. sep / end 两个关键字参数怎么改变输出形态
#   2. f-string 的格式说明符：对齐 <^>、保留小数 :.2f、千分位 :,、填充字符
#   3. 转义字符 \n \t \" \\ 与 raw 字符串 r"..." 的区别
#   4. 三种字符串格式化（f-string / .format() / %）的取舍：优先 f-string
# ============================================================================

# -----------------------------------------------------------------------------
# 1. Simple Output
# -----------------------------------------------------------------------------
# The most basic use of print()

print("--- Simple Output ---")

print("Hello, World!")
print("Welcome to Python!")
print("Learning is fun!")

# -----------------------------------------------------------------------------
# 2. Printing Different Data Types
# -----------------------------------------------------------------------------
# print() can output any data type

print("\n--- Different Data Types ---")

# 中文：print 会自动对任意对象调用 str()（更准确说是先尝试对象的 __str__），
#       所以不需要像 C/Java 那样区分 %d %s 等格式占位符就能直接打印任意类型。
print(42)              # Integer
print(3.14159)         # Float
print(True)            # Boolean
print(None)            # NoneType（注意：打印出来是 None，不是空字符串）
print([1, 2, 3])       # List
print({"a": 1})        # Dictionary

# -----------------------------------------------------------------------------
# 3. Printing Multiple Items
# -----------------------------------------------------------------------------
# Pass multiple arguments separated by commas

print("\n--- Multiple Items ---")

print("Hello", "World")
print("Python", "is", "awesome")
print("Name:", "Baraa", "| Age:", 25)
print(1, 2, 3, 4, 5)

# -----------------------------------------------------------------------------
# 4. The sep Parameter
# -----------------------------------------------------------------------------
# sep defines what goes between multiple items (default is space)

print("\n--- Separator Parameter ---")

# 中文：sep 只作用在“多个参数之间”，不会加在开头或结尾。
#       常用来一行拼出日期、IP、CSV 等结构化文本，省去手动拼字符串。
print("Python", "Java", "C++", sep=", ")
print("2025", "01", "15", sep="-")      # Date format
print("192", "168", "1", "1", sep=".")   # IP address
print("apple", "banana", "cherry", sep=" | ")
print("a", "b", "c", sep="")             # No separator

# -----------------------------------------------------------------------------
# 5. The end Parameter
# -----------------------------------------------------------------------------
# end defines what goes at the end (default is newline \n)

print("\n--- End Parameter ---")

# 中文：end 替换默认的换行符。end="" 表示“打印完不换行”，
#       于是下一个 print 会接着同一行输出——这是做进度条/同行刷新的基础。
# ⚠️ 坑：end="" 时输出会停在缓冲区里可能不立即显示，做实时进度时加 flush=True：
#        print("█", end="", flush=True)
print("Loading", end="")
print("...", end="")
print(" Done!")

print("First line", end=" --> ")
print("Second line")

# Creating a progress bar effect
print("\nProgress: ", end="")
for i in range(5):
    print("█", end="")
print(" Complete!")

# -----------------------------------------------------------------------------
# 6. Variables in Print
# -----------------------------------------------------------------------------
# Print variable values

print("\n--- Variables ---")

name = "Baraa"
age = 25
city = "Gaza"
is_student = True

print("Name:", name)
print("Age:", age)
print("City:", city)
print("Student:", is_student)

# Print with variable calculations
x = 10
y = 5
print("Sum:", x + y)
print("Product:", x * y)

# -----------------------------------------------------------------------------
# 7. String Formatting - f-strings (Recommended)
# -----------------------------------------------------------------------------
# Modern way to embed variables in strings (Python 3.6+)

print("\n--- f-strings (Formatted String Literals) ---")

name = "Baraa"
age = 25
height = 1.75

# 中文：f-string（Python 3.6+）在字符串前加 f，{} 里可直接写变量甚至表达式，
#       运行时求值后嵌入。它比 + 拼接和 .format() 都更短、更快、更易读，是首选。
# ⚠️ 坑：忘记写前缀 f，{name} 会被原样打印成 "{name}" 而不会替换。
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"Next year I'll be {age + 1}")  # 中文：{} 内可放表达式，这里直接算 age+1

# Formatting numbers
# 中文：冒号后是“格式说明符”。.2f = 定点小数保留 2 位（会四舍五入，且补零）。
#       注意 :.2f 只影响“显示”，不改变变量本身的值。
pi = 3.14159265359
print(f"Pi to 2 decimals: {pi:.2f}")
print(f"Pi to 4 decimals: {pi:.4f}")

# Padding and alignment
# 中文：对齐三剑客——<左对齐、^居中、>右对齐，后面的数字是“总宽度”。
#       宽度不足用空格补齐，常用于打印对齐的表格。
print(f"{'Left':<10}|{'Center':^10}|{'Right':>10}")
print(f"{1:<10}|{2:^10}|{3:>10}")

# Currency formatting
# 中文：逗号 , 是千分位分隔符；和 .2f 组合写成 :,.2f，即“千分位 + 两位小数”。
price = 1234.567
print(f"Price: ${price:,.2f}")  # → $1,234.57

# -----------------------------------------------------------------------------
# 8. String Formatting - Other Methods
# -----------------------------------------------------------------------------
# Alternative formatting methods

print("\n--- Other Formatting Methods ---")

# .format() method
# 中文：f-string 出现前的主流写法。{} 按位置填、{0}{1} 按索引填、{n} 按名字填。
#       现在多用于“模板字符串先定义、稍后再 .format() 填值”的场景。
name = "Alice"
age = 30
print("Hello, {}! You are {} years old.".format(name, age))
print("Hello, {0}! You are {1} years old.".format(name, age))
print("Hello, {n}! You are {a} years old.".format(n=name, a=age))

# % operator (older style)
# 中文：最老的 C 风格格式化，%s 转字符串、%d 转整数。
# ⚠️ 坑：% 后若只有一个值且它是元组，会被误当成多个参数，易报错；新代码别再用它。
print("Hello, %s! You are %d years old." % (name, age))

# -----------------------------------------------------------------------------
# 9. Escape Characters
# -----------------------------------------------------------------------------
# Special characters using backslash \

print("\n--- Escape Characters ---")

# 中文：反斜杠 \ 是转义引导符，把后面的字符变成特殊含义（换行/制表/引号等）。
print("Line 1\nLine 2\nLine 3")           # \n = newline
print("Column1\tColumn2\tColumn3")         # \t = tab
print("She said: \"Hello!\"")              # \" = quote（也可改用单引号包裹来免转义）
print('It\'s a beautiful day')             # \' = apostrophe
print("Path: C:\\Users\\Documents")        # \\ = 一个反斜杠（要打印 \ 必须写成 \\）
print("Bell sound: \a")                    # \a = bell (may not work)

# Raw strings - ignore escape characters
# 中文：r"..." 原始字符串，里面的 \ 不再转义，原样保留。
#       写 Windows 路径、正则表达式时极常用，免去满屏 \\。
# ⚠️ 坑：raw 字符串不能以单个反斜杠结尾（如 r"C:\" 会语法错误）。
print("\nRaw string:")
print(r"C:\Users\Baraa\Desktop")           # r prefix for raw string

# -----------------------------------------------------------------------------
# 10. Multi-line Printing
# -----------------------------------------------------------------------------

print("\n--- Multi-line Strings ---")

# Using triple quotes
# 中文：三引号 """...""" 可跨行书写字符串，原样保留其中的换行和缩进。
# ⚠️ 坑：这里第一行紧跟 """ 后直接换行，所以 message 开头会带一个空行；
#        若不想要前导/尾随空行，可在赋值后 .strip() 或把文字紧贴三引号写。
message = """
This is a multi-line message.
It spans across several lines.
Very useful for long text!
"""
print(message)

# ASCII art example
print("""
  ╔═══════════════════════════╗
  ║   Welcome to Python!      ║
  ║   Let's learn together!   ║
  ╚═══════════════════════════╝
""")

# -----------------------------------------------------------------------------
# 11. Practical Examples
# -----------------------------------------------------------------------------

print("--- Practical Examples ---")

# Receipt example
print("\n========== RECEIPT ==========")
item1, price1 = "Coffee", 4.99
item2, price2 = "Sandwich", 8.50
item3, price3 = "Cookie", 2.25
total = price1 + price2 + price3

print(f"{item1:.<20}${price1:.2f}")
print(f"{item2:.<20}${price2:.2f}")
print(f"{item3:.<20}${price3:.2f}")
print("=" * 30)
print(f"{'TOTAL':.<20}${total:.2f}")

# Table example
print("\n| Name     | Age | City       |")
print("|----------|-----|------------|")
print(f"| {'Alice':<8} | {25:<3} | {'New York':<10} |")
print(f"| {'Bob':<8} | {30:<3} | {'London':<10} |")
print(f"| {'Charlie':<8} | {35:<3} | {'Tokyo':<10} |")

# ============================================================================
# 【避坑总结 · 01_print.py】
# ----------------------------------------------------------------------------
# 1. f-string 必须带前缀 f，否则 {x} 原样输出不替换。
# 2. :.2f 只改“显示”不改变量值，且会四舍五入并补零。
# 3. sep 只插在参数之间；end 替换行尾换行符，end="" 时实时输出记得 flush=True。
# 4. 要打印一个反斜杠得写 "\\"；raw 字符串 r"..." 免转义但不能以单个 \ 结尾。
# 5. 三引号字符串会原样保留首尾换行/缩进，注意多出来的空行。
# 6. 旧式 % 格式化对单个元组值容易踩坑；新代码统一用 f-string。
# ============================================================================
