from extratorArgumentosUrl import ExtratorArgumentosUrl
'''
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"

argumento = "Rodrigo de Oliveira Siqueira"
#            0123456789 11  15
listaUrl = argumento.split(" ")
print(listaUrl)
'''

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar"
#                   find

argumentosUrl = ExtratorArgumentosUrl(url)
moedaOrigem,moedaDestino = argumentosUrl.extraiArgumentos()
print(moedaDestino,moedaOrigem)

#index = url.find("moedadestino") + len("moedadestino") + 1
#substring = url[index:]
#print(substring)