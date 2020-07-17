class Error(Exception):
    pass
class InputError(Error):
    def __init__(self,message):
        self.message = message
while(True):
    try:
        x = int(input('entre com a nota'))
        print(x)
        if(x>10 or x<0):
            raise InputError('Valor INVÁLIDO')
        break
    except  ValueError:
        print('Valor Inválido')
    except InputError as ex:
        print(ex)

