class Strumento:
    def __init__(self,id, tipo, marca, anno, valore):
        self.id=id
        self.tipo=tipo
        self.marca=marca
        self.anno=anno
        self.valore=valore
    def __str__(self):
        return f"{self.id} {self.tipo} {self.marca} {self.anno} {self.valore}"
