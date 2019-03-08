'''
argumento = "www.bytebank.com.br/cambio?moedaorigem=real"
#            0123456789 11  15
substring=argumento[5:11]
print(substring)
'''

argumento = "moedaorigem=real"
#            0123456789 11  15
listaargumentos = argumento.split("=")
print(listaargumentos)