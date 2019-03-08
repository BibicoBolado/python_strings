from extratorArgumentosUrl import ExtratorArgumentosUrl
link = "https://blog.alura.com.br/como-comparar-objetos-no-python/"
'''
url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar"

argumento = "Rodrigo de Oliveira Siqueira"
#            0123456789 11  15
listaUrl = argumento.split(" ")
print(listaUrl)
'''
'''
url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"
#                   find

argumentosUrl = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(url)
moedaOrigem,moedaDestino = argumentosUrl.extraiArgumentos()
valor = argumentosUrl.extraiValor()
print(moedaDestino,moedaOrigem,valor)

#index = url.find("moedadestino") + len("moedadestino") + 1
#substring = url[index:]
#print(substring)

#string = "bytebankbytebyte"
#stringNova = string.replace("byte","rodrigo",1)
#print(stringNova)

banco1 = "bytebank"
banco2 = "Bytebank".lower()

#print(banco2)
urlByteBank = "https://bytebank.com"
url1        = "hhtps://buscasites.com/busca?q=https://bytebank.com"
url2        = "https://bitebank.com.br"
url3        = "https://bytebank.com/cambio/teste/teste"

print(url1.startswith(urlByteBank))
'''

url = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1500"
outraUrl = "https://bytebank.com/cambio?moedaoRigem=moedadestino&moedadestino=dolar&valor=1900"
argumentosUrl  = ExtratorArgumentosUrl(url)
argumentosUrl2 = ExtratorArgumentosUrl(outraUrl)

print(argumentosUrl==argumentosUrl2)