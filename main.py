class City:
    def __init__(self, mesto, ulica, cislodomu, smerovecislo, stat):
        self.city = mesto
        self.street = ulica
        self.numberofstreet = cislodomu
        self.zip = smerovecislo
        self.country = stat
    def adress(self):
        print("Adress:")
        print(f"city:{self.city}")
        print(f"street:{self.street}")
        print(f"number of street:{self.numberofstreet}")
        print(f"zip:{self.zip}")
        print(f"country:{self.country}")
        print()

adresa1=City("Bratislava","Moja",1,85320,"Slovensko")
adresa1.adress()
print(adresa1.zip)