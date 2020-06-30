class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        self.canal+=1

    def diminui_canal(self):
        self.canal-=1

tel = Televisao()
print(tel.ligada)
tel.power()
print(tel.ligada)
print(tel.canal)
tel.diminui_canal()
print(tel.canal)
tel.aumenta_canal()
print('Canal: {}'.format(tel.canal))
