
class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice=codice
        self.nome=nome
        self.cognome=cognome
        self.cabina=None

    # creo la funzione che assegni il passeggero alla cabina
    def assegna_cabina(self, cabina):
        self.cabina=cabina

    def __str__(self):
         if self.cabina:
             return f"{self.codice}: {self.nome} {self.cognome} | Cabina {self.cabina.codice}"
         else:
             return f"{self.codice}: {self.nome} {self.cognome}"
