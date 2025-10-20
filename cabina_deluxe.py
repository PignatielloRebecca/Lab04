from cabina import Cabina
class cabina_deluxe(Cabina):

    def __init__(self, codice, num_letti, ponte, prezzo_base, tipologia):
        super().__init__(codice, num_letti, ponte, prezzo_base)
        self.tipologia=tipologia


    def prezzo_finale(self):
        return self.prezzo_base*1.2

    def __str__(self):
        if self.disponibile:
            cabina = "Disponibile"
        else:
            cabina = "Occupata"

        return f"{self.codice}: Deluxe ({self.tipologia} | {self.num_letti} letti - Ponte {self.ponte}- Prezzo {self.prezzo_finale():.2f}-{cabina}"