class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self._responsabile=responsabile

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
            # c'è intestazione salta prima riga
            infile.readline()
            for linea in infile:
                linea=linea.strip()
                campi=linea.split(",")
                strumento={"id":campi[0],"nome":campi[1],"marca":campi[2],"anno":int(campi[3]),"valore":float(campi[4])}





    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
