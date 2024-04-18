from collections import deque

my_str = list(input('Введите данные для проверки: '))

my_stack = deque(my_str)

# Создаем класс stack и функции в нем
class Stack:
    def is_empty(self, my_list):
        if len(my_list) == 0:
            return True
        else:
            return False

    def push(self, my_list, value):
        my_list.append(value)
        return my_list

    def pop(self, my_list):
        return my_list.pop()

    def peek(self, my_list):
        return my_list[-1]

    def size(self, my_list):
        return len(my_list)

# Создаем экземпяр класса stack
stack = Stack()

# Создаем счетчики значений ")" и "("

counter_1 = 0
counter_2 = 0

# Проводим проверку на сбалансированность с использованием методов класса stack
if stack.is_empty(my_stack):
    print('Ошибка, отсутствуют данные для проверки')

if stack.size(my_stack) % 2 != 0:
    print('Несбалансированно')
else:
    while stack.is_empty(my_stack) is not True:
        if stack.peek(my_stack) == ")":
            counter_1 += 1
        elif stack.peek(my_stack) == "(":
            counter_2 += 1
        stack.pop(my_stack)

    if counter_1 == counter_2:
        print("Сбалансированно")
    else:
        print("Несбалансированно")
