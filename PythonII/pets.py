#Alicja Piotrowska, L2
class Pet:
    def __init__(self, name, hunger = 0, tiredness = 0):
        self.name = name
        self._hunger = hunger
        self._tiredness = tiredness

    @property
    def hunger(self):
        return self._hunger

    @property
    def tiredness(self):
        return self._tiredness


    def __passage_of_time(self):
        if self.hunger >= 10:
            print("I'm dead. Thanks for feeding me.")
            exit(1)
        else:
            self._hunger += 1

        if self.tiredness >= 10:
            print("Now I'm crazy. It's a good reason to die.")
            exit(1)
        else:
            self._tiredness += 1

        return self.tiredness, self.hunger


    def talk(self):
        tiredness, hunger = self._Pet__passage_of_time()
        if tiredness + hunger < 5:
            mood = "joyful"
        elif tiredness + hunger <= 10:
            mood = "happy"
        elif tiredness + hunger <= 15:
            mood = "wired"
        elif tiredness + hunger < 20:
            mood = "angry"
        elif tiredness + hunger >= 20:
            mood = "dead"

        return mood


    def eat(self, food = 4):
        self._hunger -= food
        self._Pet__passage_of_time()

    def play(self, zabawa = 4):
        self._hunger += zabawa
        self._Pet__passage_of_time()


    def __str__(self):
        zwierzaczek = "Call me " + self.name + " please.\nI'm " + self.talk() + " now, you can play with me or feed me. I love you for the rest of my life!"
        return zwierzaczek

first = Pet("Bolek")
print(first)
print("Co chciałbyś ze mną robić?")
n = int(input("1. Nakarmic mnie\n2. Pobawić się ze mną\n3. Dać mi czas wolny\n"))
while n:
    if n == 1:
        yummy = int(input("Podaj ile chcesz mi dać jedzenia? - normalna porcja to 4"))
        first.eat(yummy)
        print(first)
    elif n == 2:
        fun = int(input("Podaj ile chcesz się ze mną bawić? - przeciętny czas to 4"))
        first.play(fun)
        print(first)
    elif n == 3:
        print("Dzięki za dziś! Do zobaczenia następnym razem!")
        exit(1)
    else:
        exit(1)

    n = int(input("1. Nakarmic mnie\n2. Pobawić się ze mną\n3. Dać mi czas wolny\n"))