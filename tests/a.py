class Gra():

    def __init__(self, minimum, maximum, liczba):
        self.minimum = minimum
        self.maximum = maximum
        self.liczba = liczba

    def sprawdz_liczbe_int(self, liczba):
        print("sprawdzam liczbe")
        if liczba == isinstance(liczba, int) and self.minimum <= liczba >= self.maximum:
            return True
        else:
            return False

    def graj(self):
        if self.sprawdz_liczbe_int(input("wpisz liczbe od "+str(self.minimum)+" do "+str(self.maximum)+": ")) == True:
            print("dobra liczba")
a1 = Gra(0, 100, 50) 
a1.graj()