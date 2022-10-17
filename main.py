# Переменные предназначены для хранения данных
name = 'Светлана'
print(name)

# Список (list) представляет тип данных, который хранит набор или последовательность элементов.
# Для создания списка применяются квадратные скобки [], внутри которых через запятую перечисляются элементы списка.
# Например, определим список чисел:

numbers = [1, 2, 3, 4, 5]
print(numbers)

# Для обращения к элементам списка надо использовать индексы, которые представляют номер элемента в списка.
# Индексы начинаются с нуля.
# То есть первый элемент будет иметь индекс 0, второй элемент - индекс 1 и так далее.
# Для обращения к элементам с конца можно использовать отрицательные индексы, начиная с -1.
# То есть у последнего элемента будет индекс -1, у предпоследнего - -2 и так далее.


# получение элементов с начала списка
people = ["Tom", "Sam", "Bob"]
print(people[0])   # Tom
print(people[1])   # Sam
print(people[2])   # Bob

# получение элементов с конца списка
people = ["Tom", "Sam", "Bob"]
print(people[-2])   # Sam
print(people[-1])   # Bob
print(people[-3])   # Tom

# Кортеж представляет последовательность элементов, которая во многом похожа на список за тем исключением, что кортеж является неизменяемым типом.
# Поэтому мы не можем добавлять или удалять элементы в кортеже, изменять его.
# Для создания кортежа используются круглые скобки, в которые помещаются его значения, разделенные запятыми:
tom = ("Tom", 23)
print(tom)  # ("Tom", 23)

# Также для определения кортежа мы можем просто перечислить значения через запятую без применения скобок:
tom = "Tom", 23
print(tom)     # ("Tom", 23)

# Если вдруг кортеж состоит из одного элемента, то после единственного элемента кортежа необходимо поставить запятую:
tom = ("Tom",)

# Обращение к элементам в кортеже происходит также, как и в списке, по индексу.
# Индексация начинается также с нуля при получении элементов с начала списка и с -1 при получении элементов с конца списка:
tom = ("Tom", 37, "Google", "software developer")
print(tom[0])  # Tom
print(tom[1])  # 37
print(tom[-1])  # software developer

# Словарь в языке Python хранит коллекцию элементов, 
# где каждый элемент имеет уникальный ключ и ассоциированое с ним некоторое значение.

# пример словаря:
users = {1: "Tom", 2: "Bob", 3: "Bill"}

# Для обращения к элементам словаря после его названия в квадратных скобках указывается ключ элемента:
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
# получаем элемент с ключом "+11111111"
print(users["+11111111"])      # Tom
 
# установка значения элемента с ключом "+33333333"
users["+33333333"] = "Bob Smith"
print(users["+33333333"])   # Bob Smith

# Проверка на наличие ключа в словаре с помощью if:
key = "+4444444"
if key in users:
    user = users[key]
    print(user)
else:
    print("Элемент не найден")

# Для удаления элемента по ключу применяется оператор del:
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
del users["+55555555"]
print(users)    # { "+11111111": "Tom", "+33333333": "Bob"}

# Для перебора словаря можно воспользоваться циклом for:
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(users[key])

# Списки и кортежи можно преобразовывать в словарь с помощью встроенной функции dict()

# Пример со списком:
users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)
print(users_dict)      # {"+111123455": "Tom", "+384767557": "Bob", "+958758767": "Alice"}

# Пример с кортежем:
users_tuple = (
    ("+111123455", "Tom"),
    ("+384767557", "Bob"),
    ("+958758767", "Alice")
)
users_dict = dict(users_tuple)
print(users_dict)

# Множество (set) представляют еще один вид набора, который хранит только уникальные элементы. 
# Для определения множества используются фигурные скобки, в которых перечисляются элементы:
users = {"Tom", "Bob", "Alice", "Tom"}
print(users)    # {"Alice", "Bob", "Tom"}

# Условные конструкции используют условные выражения и в зависимости от их значения 
# направляют выполнение программы по одному из путей.
language = "german"
if language == "english":
    print("Hello")
    print("World")
elif language == "german":
    print("Hallo")
    print("Welt")
else:
    print("Привет")
    print("мир")

# Циклы позволяют выполнять некоторое действие в зависимости от соблюдения некоторого условия.
# Цикл while проверяет истинность некоторого условия, и если условие истинно, то выполняет инструкции цикла.
# Рассмотрим код, использующий цикл while, который распечатает 10 раз слово Привет:
i = 0
while i < 10:
    print('Привет')
    i += 1
    
# Другой тип циклов представляет конструкция for. 
# Этот цикл пробегается по набору значений, помещает каждое значение в переменную, 
# и затем в цикле мы можем с этой переменной производить различные действия
# Цикл for, которые делает так же выводит слово Привет 10 раз:
for i in range(10):
    print('Привет')


# Функции представляют блок кода, 
# который выполняет определенную задачу и который можно повторно использовать в других частях программы.

# Могу написать функцию, принимающую именованные аргументы и показать её вызов
def div(a, b):
    print(a / b)

div(a=4, b=2)

# Могу написать функцию, принимающую переменное число аргументов и показать её вызов.

# Получение аргументов в виде кортежа
def my_sum(*args):
    print(sum(args))

my_sum(4, 2, 3, 1, 5, 6, 6, 4)

# Получение аргументов в виде словаря
def my_func(**kwargs):
    print(kwargs)

my_func(name='Sveta', age=23)

