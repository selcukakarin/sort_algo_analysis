import random


def createNumberLists():
    # 100'lük sayı listesi üret
    my_list = []
    for i in range(100):
        my_list.append(random.randint(1, 100))
    with open('utils/yuzluk.txt', 'w') as file:
        for i in my_list:
            file.write("%i\n" % i)
    # 500'lük sayı listesi üret
    my_list = []
    for i in range(500):
        my_list.append(random.randint(1, 100))
    with open('utils/besyuzluk.txt', 'w') as file:
        for i in my_list:
            file.write("%i\n" % i)
    # 1000'lük sayı listesi üret
    my_list = []
    for i in range(1000):
        my_list.append(random.randint(1, 100))
    with open('utils/binlik.txt', 'w') as file:
        for i in my_list:
            file.write("%i\n" % i)
    # 5000'lük sayı listesi üret
    my_list = []
    for i in range(5000):
        my_list.append(random.randint(1, 100))
    with open('utils/besbinlik.txt', 'w') as file:
        for i in my_list:
            file.write("%i\n" % i)
    # 10000'lük sayı listesi üret
    my_list = []
    for i in range(10000):
        my_list.append(random.randint(1, 100))
    with open('utils/onbinlik.txt', 'w') as file:
        for i in my_list:
            file.write("%i\n" % i)
