class Tebak:
    def __init__(self):
        self.tebakan = "tebakan"
        self.jawaban = "jawaban"


    def cek(self):
        if self.tebakan == self.jawaban:
            return True
        return False
