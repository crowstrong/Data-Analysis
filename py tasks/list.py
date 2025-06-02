from collections import Counter

products = ['Milk', 'Bread', 'Butter']

quantities = [150, 85, 40]

prices = [1.2, 0.8, 2.5]  # ціна відповідно до продуктів

words = ['good', 'tasty', 'good', 'cheap', 'good', 'tasty']

# task 1 
product_info = list(zip(products, quantities, prices, words)) 
print("\nTask 1:", product_info)

# task 2
product_dict = dict(zip(products, quantities))
print("\nTask 2:", product_dict)

# task 3
profit = [price * quantity for price, quantity in zip(prices, quantities)]
total_profit = sum(profit)
print("\nTask 3:")
for product, profit in zip(products, profit):
    print(f"{product}: {profit} грн")

print(f"\nЗагальний дохід: {total_profit} грн")

# task 4
print("\nTask 4:")
for index, products in enumerate(products, start=1):
    print(f"{index}. {products}")

# task 5
print("\nTask 5:")
reviews = [
    "Хороший товар і швидка доставка"
    "Відмінний товар, рекомендую"
    "Погана якість, не рекомендую"
    "Швидка доставка і гарне обслуговування"
]
all_words = " ".join(reviews).lower().split()

word_counts = Counter(all_words)

for word, count in word_counts.items():
    print(f"{word}: {count}")

from_csv = {'Anna', 'Oleh', 'Ivan'}

from_api = {'Oleh', 'Daria', 'Ivan'}


# task 6
print("\nTask 6:")
# 1. Спільні користувачі
common_users = from_csv & from_api
print("Спільні користувачі:", common_users)

# 2. Тільки в CSV
only_csv = from_csv - from_api
print("Тільки у CSV:", only_csv)

# 3. Тільки в API
only_api = from_api - from_csv
print("Тільки в API:", only_api)

# 4. Усі унікальні користувачі
all_users = from_csv | from_api
print("Усі користувачі:", all_users)


regions = ['Kyiv', 'Lviv', 'Odesa']

visits = [305, 210, 155]

# task 7
print("\nTask 7:")
# Середнє значення візитів
average_visits = sum(visits) / len(visits)
print(f"\nСередня кількість візитів: {average_visits:.2f}")

# Регіон з найбільшою кількістю візитів
max_index = visits.index(max(visits))
top_region = regions[max_index]
print(f"Регіон з найбільшою кількістю візитів: {top_region} ({visits[max_index]} visits)")

print("\nTask 8:")
# Побудова списку пар: регіон — візити
region_stats = [f"{region}: {visit} visits" for region, visit in zip(regions, visits)]
print("Список регіонів з візитами:")
for stat in region_stats:
    print(stat)

# task 9
source1 = [800, 1200, 950]
source2 = [850, 1150, 1000]

print("\nTask 9:")
average_salaries = [(s1 + s2) / 2 for s1, s2 in zip(source1, source2)]

for i, avg in enumerate(average_salaries, start=1):
    print(f"Співробітник {i}: середня зарплата {avg:.2f}")

# task 10
names = ['Anna', 'Ivan', 'Daria']
purchases = [5, 3, 7]
expenses = [120, 80, 190]

print("\nTask 10:")
customer_data = {
    name: {'purchases': p, 'expenses': e}
    for name, p, e in zip(names, purchases, expenses)
}

for name, data in customer_data.items():
    print(f"{name}: покупки — {data['purchases']}, витрати — {data['expenses']}")
