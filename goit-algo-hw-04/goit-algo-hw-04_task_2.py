"""
Друге завдання
У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, 
його ім'я та вік, розділені комою.
Наприклад:
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.
Вимоги до завдання:
Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
Функція має повертати список словників, де кожен словник містить інформацію про одного кота.
Рекомендації для виконання:
Використовуйте with для безпечного читання файлу.
Пам'ятайте про встановлення кодування при відкриті файлів
Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
Опрацьовуйте можливі винятки, пов'язані з читанням файлу.
"""
def get_cats_info(path):
    cats_info = []

    with open(path, 'r') as fh:  # Використовуємо аргумент path
        for line in fh:
            # Видаляємо зайві пробіли та символи нового рядка
            line = line.strip()
            # Розділяємо рядок на частини
            cat_id, name, age = line.split(',')
            # Створюємо словник з інформацією про кота
            cat_info = {
                "id": cat_id,
                "name": name,
                "age": int(age)
            }
            # Додаємо словник до списку
            cats_info.append(cat_info)
    
    return cats_info

# Виклик функції для прикладу
cats = get_cats_info('cats.txt')  # Вказуємо шлях до файлу
print(cats)

