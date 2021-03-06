#[A-Z-ÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ]{2,}(\s[A-Z-ÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ]{2,})   pega o nome da magia

# txt = open("teste.txt", "r+", encoding="UTF-8")
# magias = open("teste2.txt", "w", encoding="UTF-8")
# recipiente = []
# for i in txt:
#     if len(i) < 6:
#         n = 1
#         for k in i:
#             if k.isdigit() == False:
#                 n = 0
#         if n == 1:
#             magias.write(i)
#     else:
#         magias.write(i)

#-------------------------------------

# txt = open("teste2.txt", "r+", encoding="UTF-8")
# magias = open("teste3.txt", "w", encoding="UTF-8")
# recipiente = []
# magiasLista = []
# for i in txt:
#     if i.isupper() and recipiente != []:
#         magiasLista.append(recipiente)
#         recipiente = []
#     recipiente.append(i)
# magiasLista.append(recipiente)
# print(magiasLista)
#
# for i in magiasLista:
#     for k in i:
#         magias.write(k)
#     magias.write("\n")

#-------------------------------------
import re

txt = open("teste3.txt", "r", encoding="UTF-8")
recipiente = []
magiasLista = []

titulos = []

nivels = []

magiasTexto = []
texto = ""

recipienteTC = []
tempoC = []

alcance = []

componentes = []

duracao = []

descricao = []

recipiente2 = []

for i in txt:
    if i.isupper() and recipiente != []:
        for k in recipiente:
            texto += k
        magiasTexto.append(texto)
        texto = ""

        magiasLista.append(recipiente)
        recipiente = []
    recipiente.append(i)
magiasLista.append(recipiente)
for k in recipiente:
    texto += k
magiasTexto.append(texto)
#print(magiasLista)
#print(magiasTexto)


for i in magiasLista:
    titulo = i[0]
    titulos.append(titulo[0:len(titulo)-1])
#print(titulos)

#remover nomes errados
titulos.pop(titulos.index("ESTATÍSTICAS DE OBJETO ANIMADO"))
titulos.pop(titulos.index("PRECIPITAÇÃO"))
titulos.pop(titulos.index("TEMPERATURA VENTO"))

for i in magiasTexto:
    recipienteTC = re.findall(r"Tempo de Conjuração: .*?[A-Z]", i, re.MULTILINE | re.DOTALL)
    if recipienteTC != []:
        tempoC.append(recipienteTC[0][21:len(recipienteTC)-3])
#print(tempoC)

for i in magiasTexto:
    recipienteTC = re.findall(r"[A-Z]*\n.*?\nTempo de Conjuração:", i, re.MULTILINE)
    if recipienteTC != []:
        indice = -1
        for j in recipienteTC[0]:
            if j == '\n':
                indice = recipienteTC[0].index(j)
                break
        nivels.append(recipienteTC[0][indice + 1:len(recipienteTC)-22])
#print(nivels)

for i in magiasTexto:
    recipienteTC = re.findall(r"Alcance: .*?C", i, re.MULTILINE | re.DOTALL)
    if recipienteTC != []:
        alcance.append(recipienteTC[0][9:len(recipienteTC)-3])
#print(alcance)

for i in magiasTexto:
    recipienteTC = re.findall(r"Componentes: .*?D", i, re.MULTILINE | re.DOTALL)
    if recipienteTC != []:
        componentes.append(recipienteTC[0][13:len(recipienteTC)-3])
#print(componentes)

for i in magiasTexto:
    recipienteTC = re.findall(r"Duração: .*", i, re.MULTILINE)
    if recipienteTC != []:
        duracao.append(recipienteTC[0][9:200])
#print(duracao)

for i in magiasTexto:
    recipienteTC = re.findall(r"Duração: .*?\n[A-z].*?\n\n", i, re.MULTILINE | re.DOTALL)
    if recipienteTC != []:
        indice = -1
        for j in recipienteTC[0]:
            if j == '\n':
                indice = recipienteTC[0].index(j)
                break
        descricao.append(recipienteTC[0][indice + 1:len(recipienteTC)-3])
#print(descricao)



escape_dict = {'\a':r'\a',
           '\b':r'\b',
           '\c':r'\c',
           '\f':r'\f',
           '\n':r'\n',
           '\r':r'\r',
           '\t':r'\t',
           '\v':r'\v',
           '\'':r'\'',
           '\"':r'\"',
           '\0':r'\0',
           '\1':r'\1',
           '\2':r'\2',
           '\3':r'\3',
           '\4':r'\4',
           '\5':r'\5',
           '\6':r'\6',
           '\7':r'\7',
           '\8':r'\8',
           '\9':r'\9'}


def raw(text):
    """Returns a raw string representation of text"""
    new_string=''
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    return new_string


json = open("magiasJsonTxt.txt", "w", encoding="UTF-8")
jsonString = """{
    "magias" : {
        \""""
for i in range(len(titulos)):
    jsonString += titulos[i]
    jsonString += """\" : {
            "nivel": \""""
    jsonString += raw(nivels[i])
    jsonString += """\",
            "tempo de conjuracao": \""""
    jsonString += raw(tempoC[i])
    jsonString += """\",
            "alcance": \""""
    jsonString += raw(alcance[i])
    jsonString += """\",
            "componentes": \""""
    jsonString += raw(componentes[i])
    jsonString += """\",
            "duracao": \""""
    jsonString += raw(duracao[i])
    jsonString += """\",
            "descricao": \""""
    jsonString += raw(descricao[i])
    jsonString += """\"
        },
        \""""
jsonString += """\n}
}"""
json.write(jsonString)


# print(len(titulos))
# print(len(nivels))
# print(len(tempoC))
# print(len(alcance))
# print(len(componentes))
# print(len(duracao))
# print(len(descricao))
