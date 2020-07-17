import requests

def retornaDadosCEP(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/' .format(cep))
    print(response.status_code)
    print(response.text)
    dados = response.json()
    print(dados['logradouro'])

if __name__ == '__main__':
    retornaDadosCEP('35502299')