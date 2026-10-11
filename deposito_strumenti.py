#Importo attrgetter per ordinare successivamente per marca
from operator import attrgetter
class Strumento:
    def __init__(self,id, tipo, marca, anno, valore):
        self.id=id
        self.tipo=tipo
        self.marca=marca
        self.anno=anno
        self.valore=valore
    def __str__(self):
        return f"{self.id} {self.tipo} {self.marca} {self.anno} {self.valore}"

class Prestito:
    def __init__(self,id_prestito,data, id_strumento, cognome_allievo):
        self.id_prestito=id_prestito
        self.data=data
        self.id_strumento=id_strumento
        self.cognome_allievo=cognome_allievo
    def __str__(self):
        return f"{self.id_prestito} {self.data} {self.id_strumento} {self.cognome_allievo}"



class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self._responsabile=responsabile
        self.strumenti=[]
        self.prestiti=[]

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self,responsabile):
        self._responsabile=responsabile
        return


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path,"r") as infile:
            #Leggiamo ogni riga,la puliamo e la dividiamo nei campi del csv
            for linea in infile:
                linea=linea.strip()
                campi=linea.split(",")
                strumento=Strumento(campi[0],campi[1],campi[2],int(campi[3]),float(campi[4]))
                self.strumenti.append(strumento)


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        #Ricerco valore massimo di id
        #parto da massimo =0 in caso fosse vuoto il sistema
        massimo=0
        for s in self.strumenti:
            numero=int(s.id[1:])
            if numero>massimo:
                massimo=numero
        #creo nuovo id anteponendo S davanti a successivo di max
        nuovo_id="S"+str(massimo+1)
        #creo oggetto strumento
        strumento=Strumento(nuovo_id,tipo,marca,anno_acquisto,valore)
        #aggiungo oggetto a lista strumenti
        self.strumenti.append(strumento)
        return strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        #abbiamo importato attrgetter
        return sorted(self.strumenti, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # controlliamo che id strumento sia presente nel sistema
        problema = True
        for s in self.strumenti:
            if s.id == id_strumento:
                problema = False
                break
        if problema:
            raise Exception("Strumento non presente nel database")
        #come abbiamo fatto precedentemente per assegnare codice,troviamo max tra quelli
        #già esistenti e facciamo +1
        max_prestito=0
        for p in self.prestiti:
            numerop=int(p.id_prestito[1:])
            if numerop>max_prestito:
                max_prestito=numerop
            # controlliamo anche che lo strumento non sia già stato prestato
            if p.id_strumento==id_strumento:
                raise Exception("Strumento già in prestito")
        id_prestito="P"+str(max_prestito+1)
        #creo oggetto prestito
        prestito=Prestito(id_prestito,data,id_strumento,cognome_allievo)
        self.prestiti.append(prestito)
        return prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO