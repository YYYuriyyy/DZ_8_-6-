                                  ## Завдання 1
## Напишіть функцію, що обчислює добуток елементів списку цілих. Список передається як параметр.
## Отриманий результат повертається з функції

def multiply_elements(a):
    result = 1
    for num in a:
        result *= num
    return result

my_list = [5, 3, 7, 6, 4]
product = multiply_elements(my_list)
print(product)

                                  ## Завдання 2
## Напишіть функцію для знаходження мінімуму в списку цілих. Список передається як параметр.
## Отриманий результат повертається з функції

def find_minimum(nums):
    min_num = nums[0] # припускаємо, що перший елемент є мінімальним
    for num in nums:
        if num < min_num: # якщо знайдено менше число, оновлюємо мінімум
            min_num = num
    return min_num

numbers = [51, 60, 93, 27, 48]
minimum = find_minimum(numbers)
print(minimum)

                                 ## Завдання 3
## Напишіть функцію, що визначає кількість простих чисел у списку цілих.
## Список передається як параметр. Отриманий результат повертається з функції

def count_prime_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if (num % i) == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
    return count

number = [2, 3, 4, 5, 6, 7, 11, 15, 17, 19, 24]
is_prime = count_prime_numbers(number)
print(is_prime)

                                   ## Завдання 4
## Напишіть функцію, що видаляє зі списку цілих деяке задане число.
## З функції потрібно повернути кількість видалених елементів.

def delete_number(lst, num):
    count = 0
    while num in lst:
        lst.remove(num)
        count += 1
    return count

numbers = [1, 4, 3, 4, 5, 4, 7, 4, 9, 4]
removed_count = delete_number(numbers, 4)
print(numbers)
print(removed_count)

                                 ## Завдання 5
## Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків

def a (l1, l2):
    b = l1, l2
    return b
l1 = [1, 2, 3, "привіт"]
l2 = [4, 5, 6, "hai"]

b = a(l1, l2)
print(b)

                              ## Завдання 6
## Напишіть функцію, що обчислює ступінь кожного елемента списку цілих.
## Значення для ступеня передається як параметр, список теж передається як параметр.
## Функція повертає новий список, що містить отримані результати

def A(B, C):
    result = []
    for number in C:
        result.append(number ** B)
    return result

numbers = [5, 10, 100, 50, 0]
B = 3
result = A(B, numbers)
print(result)
