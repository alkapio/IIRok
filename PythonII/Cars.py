class Car:
    counter = 0
    def __init__(self, marka = None, model = None, ile_drzwi = 0, poj_silnika = 0, nr_rej = None, sr_spalanie = 0):
        self.marka = marka
        self.model = model
        self.ile_drzwi = ile_drzwi
        self.poj_silnika = poj_silnika
        self.nr_rej = nr_rej
        self.sr_spalanie = sr_spalanie
        Car.counter += 1


    @property
    def marka(self):
        return self._marka

    @marka.setter
    def marka(self, name):
        if name == "":
            print("Podaj marke!")
        else:
            self._marka = name

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, name):
        if name == "":
            print("Podaj model!")
        else:
            self._model = name

    @property
    def ile_drzwi(self):
        return self._ile_drzwi

    @ile_drzwi.setter
    def ile_drzwi(self, number):
        if number < 2 or number > 6:
            print("Podałeś nieprawidłową liczbę drzwi!")
        else:
            self._ile_drzwi = number

    @property
    def poj_silnika(self):
        return self._poj_silnika

    @ile_drzwi.setter
    def poj_silnika(self, number):
        if number < 0.8 or number > 3:
            print("Podałeś nieprawidłową liczbę drzwi!")
        else:
            self._poj_silnika = number

    @property
    def nr_rej(self):
        return self._nr_rej

    @nr_rej.setter
    def nr_rej(self, text):
        if text == "":
            print("Podałeś nieprawidłowy numer tablicy rejestracyjnej!")
        else:
            self._nr_rej = text

    @property
    def sr_spalanie(self):
        return self._sr_spalanie

    @sr_spalanie.setter
    def sr_spalanie(self, number):
        if number < 4 or number > 13:
            print("Podałeś nieprawidłowe średnie spalanie/100km!")
        else:
            self._sr_spalanie = number


    def gasoline_rate(self, price, distance):
        x = float((self.sr_spalanie * distance)/100)
        grate = float(x * price)
        print("Podróż wyniesie Cie "+str(grate)+" zł\n\n")

    def __str__(self):
        return 'Marka: {''}\nModel: {''}\nIle drzwi: {}\nPojemność silnika: {:.1f}\nNumer rejestracyjny: {''}\nŚrednie spalanie na 100km: {:.1f}'.format(self._marka,
                self._model, self._ile_drzwi, self._poj_silnika, self._nr_rej, self._sr_spalanie)

    def getCounter():
        print("Ilosc samochodow: "+str(Car.counter))


class Garage:
    cars_inside = 0
    cars = []
    def __init__(self, address = None, capacity = 0):
        self.address = address
        self.capacity = capacity

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, add):
        if add == "":
            print("Adres nie moze byc pusty!")
        else:
            self._address = add


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cap):
        if cap<1:
            print("Zła wielkosc garazu")
        else:
            self._capacity = cap


    def add_car(self, marka, model, ile_drzwi, poj_silnika, nr_rej, sr_spalanie):
        if Garage.cars_inside < self.capacity:
            self.cars.append(Car(marka, model, ile_drzwi, poj_silnika, nr_rej, sr_spalanie))
            Garage.cars_inside += 1
        else:
            print("Nie ma miejsca w garazu na ten samochod")

    def delete(self, nr_rejestr):
        for car in self.cars:
            if car.nr_rej == nr_rejestr:
                Garage.cars.remove(car)
                Garage.cars_inside -= 1

    def __str__(self):
        Ginfo = "Informacje o garazu:\nAdres: {}\nPojemnosc: {}\nAktualna ilosc samochodow w garazu: {}\n\n".format(
                self.address, self.capacity, Garage.cars_inside)
        for car in self.cars:
            Ginfo += car.__str__()+"\n\n"
        return Ginfo

class Person:
    def __init__(self, imie = None, nazwisko = None, adres = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.moj_garaz = None

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, im):
        if im != "":
            self._imie = im
        else:
            print("Pole imie nie moze byc puste!")

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, nazw):
        if nazw != "":
            self._nazwisko = nazw
        else:
            print("Pole nazwisko nie moze byc puste!")

    @property
    def adres(self):
        return self._adres

    @adres.setter
    def adres(self, adr):
        if adr != "":
            self._adres = adr
        else:
            print("Pole adres nie moze byc puste!")

    def add(self, marka, model, ile_drzwi, poj_silnika, nr_rej, sr_spalanie):
        self.moj_garaz.add_car(marka, model, ile_drzwi, poj_silnika, nr_rej, sr_spalanie)

    def delete(self, nr_rejestr):
        self.moj_garaz.delete(nr_rejestr)

    def __str__(self):
        Pinfo = "Cześć! Jestem {} {}\nMoj adres zamieszkania to {}\n\n".format(
            self.imie, self.nazwisko, self.adres)
        Pinfo += self.moj_garaz.__str__()
        return Pinfo



#Pkt 1 - tworzymy Janusza
P1 = Person("Janusz", "Malczyk", "Wielicka 17, 39-748 Kraków")
#Dajemy Januszowi garaz
P1.moj_garaz = Garage("Wielicka 18, 39-748 Kraków", 5)
#Januszek kupuje sobie trzy samochody
P1.add("Toyota", "Yaris", 3, 1.0, "KR4FA43", 6.8)
P1.add("Audi", "A3", 5,  2.3, "KR360LU", 7.5)
P1.add("Skoda", "Fabia", 5,  1.8, "KR300GA", 7.2)
#Janusz ma juz w garazu:
print(P1)

#Testujemy samochod Janusza - sprawdzamy ile zapłaci za podróż
P1.moj_garaz.cars[1].gasoline_rate(5.19, 68)
#Halinka wpadła do rowu i skaskowała samochód
P1.delete("KR300GA")
print(P1)
#Janusz ma pecha - złodzieje kradną mu pozostałe samochody!
P1.delete("KR360LU")
P1.delete("KR4FA43")
print(P1)