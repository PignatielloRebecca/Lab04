
class Cabina:
    def __init__(self, codice, num_letti, ponte, prezzo_base):
        self.codice=codice
        self.num_letti=int(num_letti)
        self.ponte=int(ponte)
        self.prezzo_base=float(prezzo_base)
        self.disponibile=True
        self.passeggero=None

    def prezzo_finale(self):
        return self.prezzo_base


    # creo una funzione che mi assegni la cabina al passeggero
    def assegna_passeggero(self, passeggero):
        self.disponibile=False
        self.passeggero=passeggero

    def __lt__(self, other):
        if isinstance(other, Cabina):
            return self.prezzo_finale()< other.prezzo_finale()  # qui diciamo che una cabina è minore dell'altre
        return  False

    def __eq__(self, other):
        if isinstance(other, Cabina):
           return self.prezzo_finale()==other.prezzo_finale()  # qui le due cabine risultano uguali
        return False

    def __str__(self):
        if self.disponibile:
            cabina="Disponibile"
        else:
            cabina="Occupata"
        return f"{self.codice}: Standard | {self.num_letti} letti - Ponte {self.ponte}- Prezzo {self.prezzo_finale():.2f}-{cabina}"



