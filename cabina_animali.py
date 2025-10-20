
from cabina import Cabina
class cabina_animali(Cabina):

    def __init__(self, codice, num_letti, ponte, prezzo_base, max_animali):
        super().__init__(codice, num_letti, ponte, prezzo_base)
        self.max_animali=max_animali


    def prezzo_finale(self):
        return self.prezzo_base*(1+0.1*self.max_animali)

    def __str__(self):
        if self.disponibile:
            cabina="Disponibile"
        else:
            cabina="Occupata"
        return f"{self.codice}: Animali | {self.num_letti} letti - Ponte {self.ponte}- Prezzo {self.prezzo_finale():.2f}- Max animali{self.max_animali}-{cabina}"

