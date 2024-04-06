class Televizor:
    def __init__(self):
        self.trenutni_kanal = 0
        self.naziv_trenutnog_kanala = ""
        self.kanali = []
        self.jacina_tona = 5

    def get_trenutni_kanal(self):
        return self.trenutni_kanal

    def set_trenutni_kanal(self, novi_kanal):
        if 0 <= novi_kanal < len(self.kanali):
            self.trenutni_kanal = novi_kanal
            self.naziv_trenutnog_kanala = self.kanali[novi_kanal]

    def get_naziv_trenutnog_kanala(self):
        return self.naziv_trenutnog_kanala

    def get_jacina_tona(self):
        return self.jacina_tona

    def set_jacina_tona(self, nova_jacina):
        if 0 <= nova_jacina <= 10:
            self.jacina_tona = nova_jacina

    def dodaj_kanal(self, naziv_kanala):
        self.kanali.append(naziv_kanala)

    def obrisi_kanal(self, naziv_kanala):
        if naziv_kanala in self.kanali:
            self.kanali.remove(naziv_kanala)

    def pojacaj_ton(self):
        if self.jacina_tona < 10:
            self.jacina_tona += 1

    def ime_kanala(self, broj_kanala):
        if 1 <= broj_kanala < len(self.kanali):
            return self.kanali[broj_kanala - 1]
        else:
            return "Kanal nije pronađen"

televizor = Televizor()
televizor.dodaj_kanal("National Geographic")
televizor.dodaj_kanal("HBO")
televizor.dodaj_kanal("Discovery Channel")
print("Trenutni kanal:", televizor.get_trenutni_kanal())
print("Trenutni naziv kanala:", televizor.get_naziv_trenutnog_kanala())
televizor.set_trenutni_kanal(3)
print("Prebaceni kanal:", televizor.get_trenutni_kanal())
print("Trenutni naziv kanala:", televizor.get_naziv_trenutnog_kanala())
televizor.pojacaj_ton()
print("Jačina tona:", televizor.get_jacina_tona())
print("Naziv kanala na 2. poziciji:", televizor.ime_kanala(2))
