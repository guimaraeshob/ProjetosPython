
import openpyxl
from PIL import Image,ImageDraw,ImageFont

# Acessar planilha de dados dos alunos
workbook_alunos = openpyxl.load_workbook('planilha_alunos.xlsx')

# Acessar a aba 'sheet1'
sheet_alunos = workbook_alunos['Sheet1']

# Percorer a planilha 
for indice,linha in enumerate(sheet_alunos.iter_rows(min_row=2)): #max_row=2 para imprimir somente 1 diploma
    nome_curso = linha[0].value
    nome_aluno = linha[1].value
    participacao = linha[2].value
    data_inicio = linha[3].value
    data_termino = linha[4].value
    carga_hora = linha[5].value
    data_emissao = linha[6].value

    # Tranferirir os dados da planilha para o certificado
    fonte_nome = ImageFont.truetype('./tahomabd.ttf',90)
    fonte_geral = ImageFont.truetype('./tahoma.ttf',80) 
    fonte_data = ImageFont.truetype('./tahoma.ttf',55) 

    # Abrindo a imagem do diploma
    imagem = Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(imagem)
    desenhar.text((1020,825),nome_aluno,fill='black',font=fonte_nome)
    desenhar.text((1070,950),nome_curso,fill='black',font=fonte_geral)
    desenhar.text((1435,1065),participacao,fill='black',font=fonte_geral)
    desenhar.text((1480,1182),str(carga_hora),fill='black',font=fonte_geral)

    desenhar.text((750,1770),data_inicio,fill='blue',font=fonte_data)
    desenhar.text((750,1930),data_termino,fill='blue',font=fonte_data)
    desenhar.text((2220,1930),data_emissao,fill='blue',font=fonte_data)

    imagem.save(f'./{indice} {nome_aluno} certificado.png')
