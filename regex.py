import re
email1 = "Meu numero é 12134-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular"
email4  = "lalalalalal 995431254 hiusahdiashasiuahdhasiudhia 98761234 dhadhahdasid 98761234"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao,email1)
print(retorno)