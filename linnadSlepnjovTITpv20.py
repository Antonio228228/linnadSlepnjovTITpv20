cities = []
populations = []
 
while True:
    city = input('Введите название города. ')
    population = int(input('Введите население этого города. '))
    cities.append(city)   #raswirenie
    populations.append(population)
    escape = input('Введите "q" для завершения ввода данных о городах \
или Enter для продолжения. ')
    if escape.lower() == 'q':
        break
 
city_dict = dict(zip(cities, populations))  #zip объединяет элементы из нескольлких источников данных (cities, populations)
 
def get_population(city, cities):   #uznaem population
    if city in cities.keys():    #dictionary keys returns a view object
        return f'The population of {city} is {cities[city]} people.'
    else:
        return 'The city is not in the list.' 
 
def show_inf(cities):  #v alfavitnom poryadke spisok gorodov
    sorted_tuple = sorted(cities.items())  #alphabet poryadok, items() vozvrawaet values of object, элементы кортежa(списки) tuple не могут быть изменены
    return sorted_tuple
 
def most_pop(cities):  #samiy gustonaselenniy
    big = 0         #сравниваем густонаселенность, если поп выше чем биг, то присваивается к переменной биг - популяция и город к имени
    town = ''
    for city, pop in cities.items(): 
        if pop > big:
            big = pop
            town = city
    return f'{town} : {big}'     #возвращается город и густонаселенность
 
def less(cities, num):  #samiy malonaselenniy
    my_dic = {}
    for city, pop in cities.items():
        if pop < num:      #сравниваем колво населения с pop
            my_dic[city] = pop
    return my_dic
 
 
while True:   
    menu = input('Команды: 1, 2, 3, 4, q ')
    if menu == '1':
        city = input('Введите название города. ')
        print(get_population(city, city_dict))
    if menu == '2':
        print(show_inf(city_dict))
    if menu == '3':
        print(most_pop(city_dict))
    if menu == '4':
        num = int(input('Введите количество населения. '))
        print(less(city_dict, num))
    if menu == 'q':
        break
