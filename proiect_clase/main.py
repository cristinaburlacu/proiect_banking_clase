class Client:
    def __init__(self, nume ,nr_telefon , oras ):
        self.nume = nume
        self.nr_telefon = nr_telefon
        self.oras = oras
        self.balanta = 0
        self.tranzactii = []

    def __str__(self):

        return self.nume + str(self.balanta)

    def retragere(self , suma):

        if self.balanta < suma :
            print("n-ai bani")
            return

        self.balanta = self.balanta - suma
        self.tranzactii.append(Tranzactie("retragere" ,self, suma ))




    def depunere(self, suma):

        self.balanta = self.balanta + suma
        self.tranzactii.append(Tranzactie("depunere" ,self  , suma))

    def transfer(self, destinatar , suma):
        if self.balanta < suma:
            print("No money")
            return
        self.balanta = self.balanta - suma
        destinatar.balanta = destinatar.balanta + suma
        self.tranzactii.append(Tranzactie("transfer" , self,  suma , destinatar))

class Tranzactie:
    def init(self, tip ,expeditor, suma, destinatar = None):
        self.tip = tip
        self.expeditor = expeditor
        self.suma = suma
        self.destinatar = destinatar


    def str(self):
        if self.destinatar == None:

            return self.expeditor.nume + "|" +str(self.suma) + "|" + self.tip

        return self.expeditor.nume  + "|" + str(self.suma) + "|" + self.destinatar + "|" + self.tip





client1 = Client("andrei", "08375893" , "suceava")
client2 = Client("adi" , "03844820" , "brasov")

client1.depunere(5)
client1.retragere(3)
print(client1)
client1.transfer(client2 , 500000)
print(client1.tranzactii)

for E in client1.tranzactii:
    print(E)
    print("fkdkd")
