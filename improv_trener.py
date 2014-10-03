import random
import time

old = ["czepiec", "funt", "kiep", "przebyt", "dziesiecina", "czcigodny", "skryba"]
nice = ["dowcip","slonce", "pomarancza", "muzyka", "saksofon", "taniec", "usmiech"]
sad = ["trumna", "wojna", "kolba", "bruk", "egzekucja", "bloto", "bug", "krew"]
my_list = [] 
 
a = input("Na jaki temat chcesz improwizowac - smutny (s), wesoly (w), staropolski (o), chcę stworzyć własną listę słów(l)? ")

q = 1
if a == 'l':
        while q != 2:
                my_word = input("Napisz słowo, które chcesz dodać do swojej listy, wciśnij enter aby zakończyć tworzenie listy i uruchomić program: ")
                if my_word == '':
                        q += 1
                else:
                        my_list.append(my_word)

def improwizacja(dane):
	while True:
		print(random.choice(dane))
		time.sleep(random.choice(range(5,10)))
f = 1
while f != 2:
    if a == 's':
        improwizacja(sad)
    elif a == 'w':
        improwizacja(nice)
    elif a == 'o':
        improwizacja(old)
    elif a == 'l':
        improwizacja(my_list)
    else:
        a = input('Podaj prawidlowa odpowiedz: "s", "w", "o"')
        f += 1
