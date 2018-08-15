class Pupil:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.marks = {}


    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, fname):
        if len(fname) > 3:
            self._imie = fname
        else:
            print("Za krótkie imie")

    @property
    def nazwisko(self):
        return self._nazwisko

    @nazwisko.setter
    def nazwisko(self, lname):
        if len(lname) > 3:
            self._nazwisko = lname
        else:
            print("Za krótkie nazwisko")


    def complete_marks(self, subject, grade):
        grades = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6]
        if len(subject) > 2:
            if grade in grades:
                self.marks[subject] = grade
            else:
                print("Nie ma takiej oceny")
        else:
            print("Zbyt krótka nazwa przedmiotu!")

    def print_marks(self):
        print(self.marks)

    def mean(self):
        suma = 0
        count = 0
        for a in self.marks.values():
            suma += a
            count += 1
        wynik = suma / count
        wynik = round(wynik, 2)
        return wynik

    def __str__(self):
        return "Uczeń: {} {}\nŚrednia ocen: {}\n".format(self.imie, self.nazwisko,self.mean())

class Student(Pupil):
    def __init__(self, imie, nazwisko):
        super().__init__(imie, nazwisko)
        self.weights = {}

    def complete_weights(self, subject, weight):
        if subject in self.marks.keys():
            self.weights[subject] = {}
            if 0<=weight<=1:
                self.weights[subject] = weight
            else:
                print("Zła waga klucza")
        else:
            print("Nie ma takiego przedmiotu w bazie")


    def mean(self):
        suma = 0
        count = 0
        for a in self.marks.keys():
            ocena = self.marks[a]
            przedmiot = a
            if przedmiot in self.weights.keys():
                waga = self.weights[przedmiot]
                count += waga
            suma += ocena*waga
        wynik = suma/count
        wynik = round(wynik, 2)
        return wynik

    def __str__(self):
        return "Uczeń: {} {}\nŚrednia ważona ocen: {}\n".format(self.imie, self.nazwisko,self.mean())



#Pupil
print("Obiekt klasy Pupil")
first = Pupil("Jacek", "Tuptuś")
first.complete_marks("matematyka", 5)
first.complete_marks("polski", 3.5)
first.complete_marks("fizyka", 4)
first.complete_marks("historia", 4.5)
first.print_marks()
print(first)


#Student
print("\n\nStudent")
second = Student("Jacek", "Tuptuś")
second.complete_marks("matematyka", 5)
second.complete_marks("polski", 3.5)
second.complete_marks("fizyka", 4)
second.complete_marks("historia", 4.5)
second.print_marks()
second.complete_weights("historia", 0.7)
second.complete_weights("matematyka", 1)
second.complete_weights("polski", 0.4)
second.complete_weights("fizyka", 0.5)
print(second.weights)
print(second)