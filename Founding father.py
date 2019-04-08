sl = {'Harold Abelson': 'Logo',
        'Andrei Alexandrescu': 'C++',
        'Alfred Vaino Aho': 'AWK',
        'Guido van Rossum': 'Python',
        'Jeremy Ashkenas': 'CoffeeScript',
        'Walter Bright': 'D',
        'John George Kemeny': 'Basic',
        'Peter Naur': 'Algol',
        'Don Syme': 'F',
        'Kenneth Eugene Iverson': 'APL',

        }
a = input('Введите Sort или Search: ')
if a == 'Sort':
        sortName = sorted(sl.keys())
        for lang in sortName:
                print(lang, " - ", sl[lang])
elif a == 'Search':
        searchName = input(" Введите имя: ")
        for name, value in sl.items():
                if name == searchName:
                        print(searchName, 'Разработал язык', sl[name])
                        break
        else:
                print("в списке нет")
else:
        print('Введена команда неправилно')
