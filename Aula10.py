from datetime import date,time,datetime,timedelta
def Usando_date():
    dataAtual = date.today()
    print(dataAtual.strftime('%d/%m/%Y'))

def usandoTime():
    horario = time(hour=15,minute=18,second=30)
    print(type(horario))
    print(horario.strftime('%H:%M:%S'))

def usandoDatetime():
    dataHoraAtual = datetime.now()
    print(dataHoraAtual)
    print(dataHoraAtual.strftime('%c'))
    print(dataHoraAtual - timedelta(days=365, hours=1,minutes=1, seconds=10))

if __name__ == '__main__':
    usandoTime()
    Usando_date()
    usandoDatetime()