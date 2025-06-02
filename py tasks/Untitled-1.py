# 0) 2 * 3
a = 2 * 3
print("0) 2 * 3 =", a, "->", type(a))

# 1) (3 * 3 + 8) / 3
b = (3 * 3 + 8) / 3
print("1) (3 * 3 + 8) / 3 =", b, "->", type(b))

# 2) 8 // 3
c = 8 // 3
print("2) 8 // 3 =", c, "->", type(c))

# 3) 8 % 3
d = 8 % 3
print("3) 8 % 3 =", d, "->", type(d))

# 4) 5 ** 2
e = 5 ** 2
print("4) 5 ** 2 =", e, "->", type(e))

# 5) "Hello " + "world"
f = "Hello " + "world"
print("5) 'Hello ' + 'world' =", f, "->", type(f))

# 6) 'Python' * 5
g = 'Python' * 5
print("6) 'Python' * 5 =", g, "->", type(g))

# 7) 5 < 9
h = 5 < 9
print("7) 5 < 9 =", h, "->", type(h))

# 8) Створення змінних з рядками
text_single = 'My name is John Malkovich'
text_apostrophe = "It's a good day"
text_multiline = '''You do not talk about Fight Club. 
You do NOT talk about Fight Club. 
If someone says "Stop" or goes limp, taps out, the fight is over. Only two guys to a fight.
One fight at a time.
No shirts, no shoes.
Fights will go on as long as they have to.
If this is your first time at Fight Club, you have to fight.
'''

print("8.1) text_single:", text_single, "->", type(text_single))
print("8.2) text_apostrophe:", text_apostrophe, "->", type(text_apostrophe))
print("8.3) text_multiline:", text_multiline, "->", type(text_multiline))


# Змінна для завдання
zen = "Simple is better than complex."

# a) Перші 10 символів
print("a)", zen[:10])

# b) 10 символів, починаючи з 3-го (індекс 2)
print("b)", zen[2:12])

# c) Останні 10 символів
print("c)", zen[-10:])

# d) Рядок у зворотному порядку
print("d)", zen[::-1])

# e) Символи з парними індексами
print("e1) парні індекси:", zen[::2])

# e) Символи з непарними індексами
print("e2) непарні індекси:", zen[1::2])


# Створення змінних
var_1 = 75
var_2 = 50

# Порівняння
print("a > b:", var_1 > var_2)
print("a < b:", var_1 < var_2)
print("a == b:", var_1 == var_2)
print("a != b:", var_1 != var_2)

# Логічні операції
# 1. Чи одна змінна більша за іншу і є додатною
print("a > b and a > 0:", var_1 > var_2 and var_1 > 0)

# 2. Чи одна зі змінних менша за 100 або дорівнює 50
print("a < 100 or b == 50:", var_1 < 100 or var_2 == 50)


# Створення змінних
my_list = [1, 2, 3, 4]
my_dict = {'name': 'Jack', 'age': 30}
my_text = "You Do Not Talk About Fight Club!"

# Інспекція об'єктів
# print("dir(my_list):", dir(my_list))
# print("dir(my_dict):", dir(my_dict))
# print("dir(my_text):", dir(my_text))

# help(list)
# help(dict)
# help(str)

# Методи списку
my_list.append(5)
my_list.reverse()
print("Список після методів append і reverse:", my_list)

# Методи словника
my_dict.update({'country': 'USA'})
value = my_dict.get('name')
print("Словник після update і get:", my_dict, "| Значення 'name':", value)

# Методи рядка
upper_text = my_text.upper()
words = my_text.split()
print("Рядок після upper і split:", upper_text, "| Слова:", words)
