from logging import exception

from cabina import Cabina
from passeggero import Passeggero
from cabina_animali import cabina_animali
from cabina_deluxe import cabina_deluxe



class Crociera:
    def __init__(self, nome):
        self._nome=nome
        self.passeggeri={}
        self.cabine={}

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nuovo_nome):
        self._nome=nuovo_nome

        """Inizializza gli attributi e le strutture dati"""
        # TODO

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        import csv
        try:

         with open(file_path, 'r', encoding='utf-8') as file:
            reader=csv.reader(file)

            for row in reader:
                codice=row[0].strip()
                if codice.startswith("CAB"):
                    num_letti=row[1]
                    ponte=row[2]
                    prezzo_base=float(row[3])

                    # se ci sono 4 campi, la cambina è una cabina stardard
                    if len(row)==4:
                        cabina=Cabina(codice, num_letti, ponte, prezzo_base)

                    # verifica che il 4 campo è un valore numerico, se è un valore numerico--> cabina animali
                    # se il campo non è un valore numerico--> cabina deluxe
                    elif len(row)==5 and row[4].isdigit():
                        max_animali=int(row[4])
                        cabina=cabina_animali(codice, num_letti, ponte, prezzo_base, max_animali)

                    elif len(row)==5:
                        tipolgia=row[4]
                        cabina=cabina_deluxe(codice, num_letti, ponte, prezzo_base,tipolgia)

                    else:
                        raise Exception (f"formato {row} non valido")

                    self.cabine[codice]=cabina  # creo il mio dizionario cabine

                elif codice.startswith("P"):
                    nome=row[1].strip()
                    cognome=row[2].strip()
                    passeggero=Passeggero(codice, nome, cognome)

                    self.passeggeri[codice]=passeggero

                else:
                    raise ValueError ("Formato non valido")

        except FileNotFoundError:
            raise FileNotFoundError("File non trovato")


        # TODO


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        if codice_cabina not in self.cabine:
            raise ValueError ("Cabina inesistente")

        if codice_passeggero not in self.passeggeri:
            raise ValueError("Passeggero non esistente")

        cabina=self.cabine[codice_cabina]
        passeggero=self.passeggeri[codice_passeggero]

        if not cabina.disponibile:
            raise ValueError ("Cabina già occupata ")
        if passeggero.cabina is not None:
            raise ValueError(" Passeggerò già sistemato ")

        cabina.assegna_passeggero(passeggero)
        passeggero.assegna_cabina(cabina)
        # TODO

    def cabine_ordinate_per_prezzo(self):
        return sorted(self.cabine.values())  # grazie ai metodi Eq e lt  implementati in cabina
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):

        for passeggero in self.passeggeri.values():
            print(passeggero)
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

