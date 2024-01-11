class City:
    def __init__(self, mesto, ulica, cislodomu, smerovecislo, stat):
        self.city = mesto
        self.street = ulica
        self.numberofstreet = cislodomu
        self.zip = smerovecislo
        self.country = stat
    def address(self):
        print("Address:")
        print(f"city:{self.city}")
        print(f"street:{self.street}")
        print(f"number of street:{self.numberofstreet}")
        print(f"zip:{self.zip}")
        print(f"country:{self.country}")
        print()
        print(f"Address:\n street:{self.city} \n number of street:{self.numberofstreet} \n zip:{self.zip} \n country:{self.country}")

adresa1=City("Bratislava","Moja",1,85320,"Slovensko")
adresa1.address()
adresa2=City("Malacky","Bratislavska",5,90001,"SR")
adresa2.address()
adresa3=City("Martin","Maticna",18,70023,"Slovenska republika")
adresa3.address()

