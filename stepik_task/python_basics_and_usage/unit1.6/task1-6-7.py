"""
https://stepik.org/lesson/24462/step/7?unit=6768

Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass

Класс A является прямым предком класса B, если B отнаследован от A:

class B(A):
    pass

Класс A является предком класса B, если

    A = B;
    A - прямой предок B
    существует такой класс C, что C - прямой предок B и A - предок C

Например:

class B(A):
    pass

class C(B):
    pass

# A -- предок С

Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных

В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов
наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться.
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
Формат выходных данных

Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком
класса 2, и "No", если не является.

Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A

Sample Output:

Yes
Yes
Yes
No


"""
# list_test = ['A : C B', 'B : D E']
# list_test = ['A', 'B : A', 'C : A', 'D : B C']
# list_test = ['classA : classB classC classD classG classH', 'classB : classC classE classG classH classK classL', 'classC : classE classD classH classK classL', 'classE : classD classF classK classL', 'classD : classG classH', 'classF : classK', 'classG : classF', 'classH : classL', 'classK : classH classL', 'classL']#10 входов

# list_find = ['E A']
# list_find = ['A B', 'B D', 'C D', 'D A']
# list_find=['classK classD', 'classD classA', 'classG classD', 'classH classA', 'classE classE', 'classH classG', 'classE classL', 'classB classD', 'classD classL', 'classD classG', 'classD classE', 'classA classF', 'classA classC', 'classK classA', 'classA classH', 'classK classD', 'classH classB', 'classK classB', 'classD classL', 'classG classG', 'classA classH', 'classK classL', 'classG classE', 'classB classA', 'classC classK', 'classK classL', 'classC classL', 'classG classC', 'classD classD', 'classC classG', 'classE classA', 'classF classK', 'classB classG', 'classH classL', 'classL classF', 'classH classG', 'classD classA', 'classH classL']#38 запросов

# answers = ['Yes']
# answers = ['Yes', 'Yes', 'Yes', 'No']
# answers = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No']#38 ответов


first_dict = {}
result = []

def first_input(list_test):
    for i in range(list_test):
    # for i in list_test:
        child, *father = input().replace(":", " ").split()
        # child, *father = i.replace(":", " ").split()
        if child not in first_dict:
            first_dict[child] = father
        else:
            first_dict[child].extend(father)

    for key, value in first_dict.items():
        first_dict[key] = list(set(value))


def second_input(list_find):
    # for i in list_find:
    for i in range(list_find):
        # father, child = i.split()
        father, child = input().split()
        if father == child:
            result.append('Yes')
        else:
            global mas
            mas = []
            find(father, child)
            if father in mas:
                result.append('Yes')
            else:
                result.append('No')


def find(father, child):
    global mas
    mas += first_dict[child]
    for any_child in first_dict[child]:
        try:
            find(father, any_child)
        except:
            KeyError


first_input(int(input()))
# first_input(list_test)

second_input(int(input()))
# second_input(list_find)

for i in result:
    print(i)