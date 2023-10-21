import openpyxl
import pyautogui
import pyperclip
import time

# Abrir planilha
workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')

# Abrir a aba do Excel correta
sheet_produtos = workbook['Produtos']

quantidade_linha = 0

for linha in sheet_produtos.iter_rows(min_row=2):

   quantidade_linha += 1
  
   nome_produto =  linha[0].value
   pyperclip.copy(nome_produto)
   pyautogui.click(1334,388,duration=1)
   pyautogui.hotkey('ctrl','v')

   descricao =  linha[1].value
   pyperclip.copy(descricao)
   pyautogui.click(1342,506,duration=1)
   pyautogui.hotkey('ctrl','v')

   categoria =  linha[2].value
   pyperclip.copy(categoria)
   pyautogui.click(1318,615,duration=1)
   pyautogui.hotkey('ctrl','v')

   codigoProduto =  linha[3].value
   pyperclip.copy(codigoProduto)
   pyautogui.click(1331,694,duration=1)
   pyautogui.hotkey('ctrl','v')

   pesoProduto =  linha[4].value
   pyperclip.copy(pesoProduto)
   pyautogui.click(1339,777,duration=1)
   pyautogui.hotkey('ctrl','v')

   dimencaoProduto =  linha[5].value
   pyperclip.copy(dimencaoProduto)
   pyautogui.click(1327,870,duration=1)
   pyautogui.hotkey('ctrl','v')

   time.sleep(2)

   # Clicar no botão (Próximo)
   pyautogui.click(1351,929 , duration=1)

   time.sleep(5)

   precoProduto =  linha[6].value
   pyperclip.copy(precoProduto)
   pyautogui.click(1342,421,duration=1)
   pyautogui.hotkey('ctrl','v')


   qtdEstoque =  linha[7].value
   pyperclip.copy(qtdEstoque)
   pyautogui.click(1342,504,duration=1)
   pyautogui.hotkey('ctrl','v')

   
   dataValidade =  linha[8].value
   pyperclip.copy(dataValidade)
   pyautogui.click(1308,582,duration=1)
   pyautogui.hotkey('ctrl','v')
   
   
   corProduto =  linha[9].value
   pyperclip.copy(corProduto)
   pyautogui.click(1307,671,duration=1)
   pyautogui.hotkey('ctrl','v')
   

   # Tamanho do produto é uma opção entre (pequeno, médio e grande)
   tamanhoProduto = linha[10].value
   pyautogui.click(1391,752,duration=1)


   if tamanhoProduto == 'Pequeno':
      pyautogui.click(1405,787,duration=1)
   elif tamanhoProduto == 'Médio':
      pyautogui.click(1337,807,duration=1)
   elif tamanhoProduto == 'Grande':
      pyautogui.click(1340,831,duration=1)

   #Material
   material = linha[11].value
   pyperclip.copy(material)
   pyautogui.click(1326,852,duration=1)
   pyautogui.hotkey('ctrl','v')

   #Clicar botão (Próximo)
   pyautogui.click(1344,909,duration=1)
   
   time.sleep(4)

   #Fabricante
   fabricante = linha[12].value
   pyperclip.copy(fabricante)
   pyautogui.click(1331,445,duration=1)
   pyautogui.hotkey('ctrl','v')

   #Pais de Origem 
   paisOrigem = linha[13].value
   pyperclip.copy(paisOrigem)
   pyautogui.click(1327,534,duration=1)
   pyautogui.hotkey('ctrl','v')

   #Observação
   observacao = linha[14].value
   pyperclip.copy(observacao)
   pyautogui.click(1344,620,duration=1)
   pyautogui.hotkey('ctrl','v')

   # Código de Barras
   codigoBarra = linha[15].value
   pyperclip.copy(codigoBarra)
   pyautogui.click(1334,749,duration=1)
   pyautogui.hotkey('ctrl','v')

   #Localização do Armazém
   localizacaoArmazem = linha[16].value
   pyperclip.copy(localizacaoArmazem)
   pyautogui.click(1335,834,duration=1)
   pyautogui.hotkey('ctrl','v')

   #Clicar botão (Concluir)
   pyautogui.click(1327,890,duration=1)

   print(f"Processadas {quantidade_linha} linhas da planilha")
   #Popup - Produto salvo no banco de dados
   pyautogui.click(1721,215,duration=1)
   #Popup 
   pyautogui.click(1718,215,duration=1)
   #Popup - botão (Adicionar Mais Um ?)
   pyautogui.click(1545,666,duration=2)




   



   








   




   

   
   


