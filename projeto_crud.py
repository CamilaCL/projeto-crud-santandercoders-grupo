# projeto_transacoes_bancarias -- DS-PY-17 - logica de programacao II
# readme link here: 
# https://github.com/allansuzuki/ADA_classes/blob/main/DS-PY-Data-Science/DS-PY-017%20L%C3%93GICA%20DE%20PROGRAMA%C3%87%C3%83O%20II%20(PY)/Material%20do%20Aluno/projeto_README.md
# 
# Esse programa é um sistema de gestao de transacoes de uma conta bancária pessoal
# no qual os dados são de transações e possuem seu valor, a categoria do gasto e seu ID.
# 
# Teu objetivo é completar esse sistema CRUD (Create-Read-Update-Delete) simples 
# para ver dados de transacao da tua conta pessoal, criar, editar e excluir transações.
# Também deve fazer com que o programa NUNCA pare, ou seja,
# caso ocorra um possível erro, deve validar as entradas, detectar erros e avisar o usuário
# mas o programa não deve parar.
#
#
# Notas importantes: 
# 1. As funções que geram os dados e criam a interface do sistema já estão prontas. 
# por favor não as altere.
#
# 2. Depois das funções do sistema estão as funções do programa
# No qual podem alterar à vontade, exceto o nome das funções
# Ou seja, podem criar funções, adicionar ou remover parâmetros, 
# mas não alterar o nome das funções existentes.
#
# 3. Coloque opções de navegabilidade em cada janela que o usuário estiver.
# Por exemplo, se ele escolher a opcao "alterar transacao" sem querer, tem que ter a opcao de voltar para a tela anterior ou inicial.
#
# 4. Caso por qualquer motivo queira os dados originais novamente,
# apage o json `transactions` na pasta `data` e inicie o programa novamente para gerar os dados.
# Os valores serão os mesmos, porém os UUID NÃO serão os mesmos!!
#
# Critérios (pontos):
#   tarefas validacoes  total
# C     10      15       25
# R     25      25       50
# U     10      10       20
# D     2.5     2.5      5
#
#
# Boa sorte e divirtam-se :)
# ------------------------------------------------------------------------------
# -----------------------
# depencies
# -----------------------
import json
import os
import uuid
import random
import sys

# -----------------------
# load settings
# -----------------------
sys.path.append('./data/')
from data import settings

# -----------------------
# SYSTEM functions 
# -----------------------
# não alterar nada das funções de system
def criar_transacoes(num_transacoes, proporcao_categorias, seed=settings.seed):
    assert sum([proporcao_categorias[k] for k in proporcao_categorias])==1, '`proporcao_categorias` não soma 100%! Favor rever.'

    # garantir reprodutibilidade dos valores
    random.seed(seed)

    # Calcula o número de transações por categoria com base na proporção
    numero_transacoes_por_categoria = {categoria: int(num_transacoes * proporcao) for categoria, proporcao in proporcao_categorias.items()}
    
    transacoes = []
    
    # Gera as transações
    for categoria, quantidade in numero_transacoes_por_categoria.items():
        for _ in range(quantidade):
            transacao = {
                "UUID": str(uuid.uuid4()),
                "valor": round(random.uniform(1.0, 1000.0), 2),  # Preço aleatório entre 1 e 1000
                "categoria": categoria
            }
            transacoes.append(transacao)
    
    return transacoes

def salvar_json(transacoes, path2save, filename):
    # create path if not exist
    if not os.path.exists(path2save):
        os.makedirs(path2save)
    with open(os.path.join(path2save,filename), "w") as file:
        json.dump(transacoes, file, indent=4)
    print(f"Arquivo salvo em: {os.path.abspath(os.path.curdir)+'/'+path2save+'/'+filename}")

def criar_bd(num_transacoes:int = 10000, proporcao_categorias:list = settings.categorias_proporcao, path2save="./data", filename='transactions.json'):
    salvar_json(criar_transacoes(num_transacoes,  proporcao_categorias),
                path2save, filename
    )

def load_bd(filepath='./data/transactions.json'):
    with open(filepath, "r") as file:
        bd = json.load(file)
    return bd


# -----------------------
# MAIN SCRIPT
# -----------------------
# não alterar nada abaixo
if __name__ == "__main__":
    
    # -----------------------
    # NÃO ALTERAR ESTE BLOCO
    # -----------------------
    # criar o banco de dados caso ele não exista
    print(os.path.abspath('.'))
    if not os.path.exists('./data/transactions.json'):
        criar_bd()
    
    # load bd 
    bd = load_bd()
    # -----------------------

def tela_inicial():
    print("Bem-vindo <teu nome inteiro aqui>!")
    print('conta: 0000001-0')
    print("\nEste programa permite gerenciar transações de sua conta pessoal.")
    print("\nEscolha uma das opções abaixo:")
    print("1. Visualizar relatórios")
    print("2. Cadastrar transações")
    print("3. Editar transações")
    print("4. Excluir transações")
    print("-" * 10)
    print("0. Sair")
    print('\n')

# -----------------------
# PROGRAM functions 
# -----------------------
# pode editar como quiser as funções abaixo! Somente não altere os nomes das funções.
# para alterar as funções abaixo, basta apagar o `pass` e preencher com as instruções.

def run():
    """
    Esta é a função principal que vai rodar o programa
    """  
    global parar_programa
    parar_programa = False
    
    while not parar_programa:
        
        # exibe a tela inicial
        tela_inicial()
    
        # Escolha da opção do usuário
        opcao_tela_inicial = input("Digite a opção desejada: ").strip()
        opcao_tela_inicial = validar_opcao(opcao_tela_inicial, "menu_inicial")
    
        # abaixo colocar a função que joga a pessoa para o próximo menu usando a variavel opcao tela inicial
        if opcao_tela_inicial == 0:
            print("Você saiu do sistema. Obrigado e volte sempre.")
            parar_programa = True
            
        elif opcao_tela_inicial == 1:
            visualizar_relatorios()

        elif opcao_tela_inicial == 2:    
            cadastrar_transacao()
            
        elif opcao_tela_inicial == 3:
            editar_transacao_por_ID()
            
        else:
            print("\nMenu excluir transação\n")
            excluir_transacao()
        

def validar_opcao(opcao_usuario, menu):
    """
    Função para validar a opção do usuário no menu
    """
    quantidade_opcoes_menu = {"menu_inicial" : 4, "visualizar_relatorios": 6}

    try:
        opcao_usuario = int(opcao_usuario)
        if opcao_usuario < 0 or opcao_usuario > quantidade_opcoes_menu[menu]:
            raise Exception("Opção inválida")
            
    except ValueError:
        print("Opção inválida. Digite somente números.")
        print("")
        return None
        
    except Exception as e:
        print("Opção inválida")
        print("")
        return None
        
    else:
        return opcao_usuario
        

def visualizar_relatorios():
    """
    Mostra um menu de opcoes no qual gera relatórios com base na escolha do usuário.
    """

    print("\nEscolha um relatório para ser visualizado:")
    print("1. Exibir soma total de transações")
    print("2. Exibir as 5 transações mais caras")
    print("3. Exibir as 5 transações medianas")
    print("4. Exibir as 5 transações mais baratas")
    print("5. Exibir a média total")   
    print("6. Consultar transação por ID") 
    print("-" * 10)
    print("0. Voltar ao menu principal")
    print('\n')

    opcao_visualizar_relatorio = input("Digite a opção desejada: ").strip()
    opcao_visualizar_relatorio = validar_opcao(opcao_visualizar_relatorio, "visualizar_relatorios")

    if opcao_visualizar_relatorio == 0:
        print("Retornando ao menu principal")
        run()
        
    elif opcao_visualizar_relatorio == 1:
        print("\nCalculando soma total das transações...\n")
        calcular_total_transacoes()

    elif opcao_visualizar_relatorio == 2:
        print("\nCalculando as 5 transações mais caras...\n")    
        mostrar_m5_transacoes("max")
   
    elif opcao_visualizar_relatorio == 3:
        print("Calculando as 5 transações medianas...")
        mostrar_m5_transacoes("mean")

    elif opcao_visualizar_relatorio == 4:
        print("Calculando as 5 transações mais baratas...")
        mostrar_m5_transacoes("min")

    elif opcao_visualizar_relatorio == 5:
        print("Calculando a média de todas as trasações...") 
        calcular_media()

    else:
        consultar_transacao_por_ID()

def conteudo_transacao_especifica(lista_transacoes, indice, imprimir_na_tela=False):
    
    conteudo_transacao_especifica = f"""
        ID: {lista_transacoes[indice]["UUID"]}\n
        Valor: R$ {lista_transacoes[indice]["valor"]:.2f}\n
        Categoria: {lista_transacoes[indice]["categoria"]}
        """
    if imprimir_na_tela == True:
        print(conteudo_transacao_especifica)
    else:
        return conteudo_transacao_especifica



def encontrar_transacao_por_chave_valor(lista_transacoes, chave, valor):
    for i, transacao in enumerate(lista_transacoes):
        if transacao.get(chave) == valor:
            return i # Retorna o índice na lista, caso encontre
    return -1  # Retorna -1 se não encontrar


# Quero criar uma forma de salvar os relatórios em uma pasta "relatorios"
def salvar_relatorio(nome_arquivo, conteudo):
    """
    Salvar o relatório gerado em .txt
    \nAplicar esta função em todos os relatórios listados em `visualizar_relatorios`
    """ 
    salvar_relatorio = input("Deseja salvar o relatório? [S / N] ").strip().upper()[0]

    while salvar_relatorio not in ["S", "N"]:
        salvar_relatorio = input("\nOpção inválida. Digite novamente S ou N. Deseja salvar o relatório?").strip().upper()[0]

    if salvar_relatorio == "S":
        
        pasta_relatorios = "relatorios"
        os.makedirs(pasta_relatorios, exist_ok=True)  
        nome_arquivo = str(nome_arquivo) + ".txt"
        caminho_arquivo = os.path.join(pasta_relatorios, nome_arquivo)
            
        with open(nome_arquivo, "w", encoding="utf-8") as relatorio_txt:
            for linha in conteudo:
                relatorio_txt.write(linha)
                relatorio_txt.write("\n")
        
        print(f"\nArquivo salvo sob o nome {nome_arquivo} na pasta relatorios.\n")

        print("Voltando ao menu principal\n")
        run()

    else:
        print("\nVoltando ao menu principal\n")
        run()



def calcular_total_transacoes():
    """
    Calcula o valor total de transações da conta.
    Utilize essa mesma função para o caso `por categoria`
    """
    total_transacoes = sum(float(transacao["valor"]) for transacao in bd)
    
    conteudo_relatorio_total_transacoes = f"O valor total de transações registradas foi de R$ {total_transacoes:.2f}"

    print("")

    print(conteudo_relatorio_total_transacoes)

    print("")
    
    salvar_relatorio("relatorio_total_transacoes", conteudo_relatorio_total_transacoes)


def mostrar_m5_transacoes(parametro):
    """
    Mostra as m5 transações realizadas, sendo m parâmetro que deve ser adicionada à função.
    \nm : 'max','min','median', sendo 
    \n\t'max' mostra os top 5 maior valor,
    \n\t'min' mostra os top 5 menor valor,
    \n\t'mean' mostra os top 5 valores próximos a média
    
    Utilize essa mesma função para o caso `por categoria`
    """

    if parametro == "max":
        dados_ordenados =  sorted(bd, key=lambda x: x['valor'], reverse=True)[0:5]

        conteudo_relatorio_max5_transacoes = ["As 5 maiores transações são: \n"]

        print("\n As 5 maiores transações são: ")
        for idx, dado in enumerate(dados_ordenados):
            transacao_lista_temp = f"{idx+1}: {dado}\n"
            print(transacao_lista_temp)
            
            conteudo_relatorio_max5_transacoes.append(transacao_lista_temp)

        salvar_relatorio("relatorio_5_maiores_transacoes", conteudo_relatorio_max5_transacoes)

    elif parametro == "min":
        dados_ordenados =  sorted(bd, key=lambda x: x['valor'], reverse=False)[0:5]

        conteudo_relatorio_min5_transacoes = ["As 5 menores transações são: \n"]
        print("\n As 5 maiores transações são: ")
        for idx, dado in enumerate(dados_ordenados):
            transacao_lista_temp = f"{idx+1}: {dado}\n"
            print(transacao_lista_temp)
            
            conteudo_relatorio_min5_transacoes.append(transacao_lista_temp)

        salvar_relatorio("relatorio_5_menores_transacoes", conteudo_relatorio_min5_transacoes)


    elif parametro == "mean":
        dados_ordenados =  sorted(bd, key=lambda x: x['valor'], reverse=False)
        indice_mediano = len(dados_ordenados) // 2
        transacoes_medianas = dados_ordenados[indice_mediano-2:indice_mediano+3]

        conteudo_relatorio_mean5_transacoes = ["As 5 transações medianas são: \n"]
        print("\n As 5 transações medianas são: ")
        for idx, dado in enumerate(transacoes_medianas):
            transacao_lista_temp = f"{idx+1}: {dado}\n"
            print(transacao_lista_temp)
            
            conteudo_relatorio_mean5_transacoes.append(transacao_lista_temp)
    
        salvar_relatorio("relatorio_5_transacoes_medianas", conteudo_relatorio_mean5_transacoes)
        

def calcular_media():
    """
    Calcula a média dos valores das transações.
    Utilize essa mesma função para o caso `por categoria`
    """
    total_transacoes = sum(float(transacao["valor"]) for transacao in bd)
    quantidade_transacoes = len(bd)

    media_valores_transacoes = total_transacoes / quantidade_transacoes
    conteudo_media_valores_transacoes = f"A média de valores das transações dessa conta é de R$ {media_valores_transacoes:.2f}"

    print("")

    print(conteudo_media_valores_transacoes)

    print("")
    
    salvar_relatorio("relatorio_media_valores_transacoes", conteudo_media_valores_transacoes)
    

def consultar_transacao_por_ID():
    """
    Consulta uma transação específica pelo seu UUID.
    """

    print("\nConsulta de transação por ID\n")
    id_consulta = input("Digite o ID único de transação para edição (Digite 0 para voltar ao menu inicial): ").strip().lower()
    
    if id_consulta == "0":
        print("\nRetornando ao Menu Inicial\n")
        run()

    indice = encontrar_transacao_por_chave_valor(bd, "UUID", id_consulta)

    if indice == -1:
        print("\nTransação não encontrada. Tente novamente")
        consultar_transacao_por_ID()

    else:
        print("\nTrasanção encontrada!\n")

        conteudo_transacao_especifica = conteudo_transacao_especifica(lista_transacoes=bd, indice=indice, imprimir_na_tela=False)
        print(conteudo_transacao_especifica)

        #Comentado pq estou tentando fazer isso com função
        #conteudo_transacao_especifica = f"""
        #ID: {bd[indice]["UUID"]}\n
        #Valor: R$ {bd[indice]["valor"]:.2f}\n
        #Categoria: {bd[indice]["categoria"]}
        #"""
        
        
        nome_arquivo_transacao_especifica = "relatorio_transacao_id_" + id_consulta
        
        salvar_relatorio(nome_arquivo_transacao_especifica, conteudo_transacao_especifica)


def valor_transacao_cadastro():
    while True:
    
        try:
            valor_transacao = float(input("Digite o valor da transação a ser cadastrada (use ponto em vez de vírgula no decimal): R$ ").strip())
            if valor_transacao < 0:
                raise Exception("Não é possível cadastrar uma transação menor que R$ 0,00.")
            break            
        except ValueError:
            print("Digite somente números. Use ponto em vez de vírgula no decimal.")
            
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")
                   
    if valor_transacao == 0:
        print("\nRetornando ao menu inicial.\n")
        run()
    
    valor_transacao = round(valor_transacao, 2)

    return valor_transacao

def cadastrar_transacao():
    """
    Cadastra uma nova transação.
    \nObs:Para gerar um novo uuid, veja como é feito na função `criar_transacoes`.
    """
    print("\nCadastro de novas transaões")
    print("-"*10)

    # Criação de ID automática

    UUID = str(uuid.uuid4())
    
    print("Para cancelar o cadastro e voltar ao menu inicial, digite 0\n")

    valor_transacao = valor_transacao_cadastro()

    #Comentei pq estou testando fazer isso com função
    
    #while True:
     #   
      #  try:
       #     valor_transacao_cadastro = float(input("Digite o valor da transação a ser cadastrada (use ponto em vez de vírgula no decimal): R$ ").strip())
        #    if valor_transacao_cadastro < 0:
         #       raise Exception("Não é possível cadastrar uma transação menor que R$ 0,00.")
          #  break            
        # except ValueError:
         #   print("Digite somente números. Use ponto em vez de vírgula no decimal.")
            
        #except Exception as e:
        #    print(f"Erro: {e} Tente novamente.")
            
        
   # if valor_transacao_cadastro == 0:
    #    print("\nRetornando ao menu inicial.\n")
     #   run()

    #valor_transacao_cadastro = round(valor_transacao_cadastro, 2)

    categoria_transacao_cadastro = input("Digite a categoria de cadastro dessa transação: ").strip().lower()

    transacao = {
                "UUID": str(uuid.uuid4()),
                "valor": f"{valor_transacao:.2f}",
                "categoria": categoria_transacao_cadastro
            }
    
    print(f""""Os dados informados foram: \n
    "UUID": {transacao["UUID"]}\n
    "Valor": R$ {transacao["valor"]}\n
    "Categoria": {transacao["categoria"]}
    """)

    print("\nDeseja continuar o cadastro dessa transação?")
    print("1. Cadastra a transação")
    print("2. Refazer o cadastro da transação")
    print("0. Cancelar cadastro e voltar ao menu inicial\n")

    continuar_cadastro = input("Escolha uma das opções acima: (1, 2 ou 0)" ).strip()
    while continuar_cadastro not in ['1', '2', '0']: 
        continuar_cadastro = input("Escolha uma das opções acima: (1, 2 ou 0)" ).strip()

    if continuar_cadastro == "1":
        bd.append(transacao)
        print("\nTransação cadastrada com sucesso\n")

    elif continuar_cadastro == "2":
        cadastrar_transacao()

    else:
        print("\nCadastro cancelado. Retornando ao menu inicial\n")
        run()


def editar_transacao_por_ID():
    """
    Edita uma transação específica pelo seu UUID.
    """
    print("\nEditor de transação")
    print("\nConsulta de transação por ID\n")
    
    id_consulta = input("Digite o ID único de transação para consulta (Digite 0 para voltar ao menu principal): ").strip().lower()

    if id_consulta == "0":
        print("Retornando ao menu principal")
        run()

    indice = encontrar_transacao_por_chave_valor(bd, "UUID", id_consulta)

    if indice == -1:
        print("\nTransação não encontrada. Voltando ao Menu Anterior")
        visualizar_relatorios()


    else:
        print("\nTrasanção encontrada!\n")
        conteudo_transacao_especifica = conteudo_transacao_especifica(lista_transacoes=bd, indice=indice, imprimir_na_tela=True)
        
        #conteudo_transacao_especifica = f"""
        #ID: {bd[indice]["UUID"]}\n
        #Valor: R$ {bd[indice]["valor"]:.2f}\n
        #Categoria: {bd[indice]["categoria"]}
        #"""
        
        #print(conteudo_transacao_especifica)


        print("Escolha a opção que deseja editar")
        print("1. Valor")
        print("2. Categoria")
        print("0. Retornar ao Menu Principal")
        
    
        opcao_edicao_cadastro = input("Escolha uma das opções acima: (1, 2 ou 0)" ).strip()

        while opcao_edicao_cadastro not in ['1', '2', '0']: 
            opcao_edicao_cadastro = input("Opção inválida. Escolha uma das opções acima: (1, 2 ou 0)" ).strip()
    
        if opcao_edicao_cadastro == "1":
            novo_valor_transacao = valor_transacao_cadastro()
            bd[indice]["valor"] = novo_valor_transacao
            
            print("\nEdição concluída com sucesso. Novos dados dessa transação abaixo: \n")

            conteudo_transacao_especifica(lista_transacoes = bd, indice = indice, imprimir=True)
            
            #conteudo_transacao_especifica = f"""
            #ID: {bd[indice]["UUID"]}\n
           # Valor: R$ {bd[indice]["valor"]:.2f}\n
           # Categoria: {bd[indice]["categoria"]}
           # """
        
            #print(conteudo_transacao_especifica)
            print("\nRetornando ao Menu Inicial\n")
            run()
    
    
        elif opcao_edicao_cadastro == "2":
            nova_categoria_transacao = input("Digite a nova categoria dessa transação: ").strip().lower()
            bd[indice]["categoria"] = nova_categoria_transacao
            
            print("\nEdição concluída com sucesso. Novos dados dessa transação abaixo: \n")
            conteudo_transacao_especifica(lista_transacoes = bd, indice = indice, imprimir=True)

            print("\nRetornando ao Menu Inicial\n")
            run()

        else:
            print("\nEdição cancelada. Retornando ao Menu Principal\n")
            run()

def excluir_transacao():
    """
    Exclui uma transação específica pelo UUID.
    """
    print("\nExclusão de transações")
    id_consulta = input("Digite o ID único de transação para exclusão (Digite 0 para voltar ao menu principal): ").strip().lower()

    if id_consulta == "0":
        print("Retornando ao menu principal")
        run()

    indice = encontrar_transacao_por_chave_valor(bd, "UUID", id_consulta)

    if indice == -1:
        print("\nTransação não encontrada. Voltando ao Menu Principal")
        run()

    else:
        print("\nTrasanção encontrada!\n")
        print("Dados da transação a ser excluída:\n")
        
        conteudo_transacao_especifica = conteudo_transacao_especifica(lista_transacoes=bd, indice=indice, imprimir_na_tela=True)
        
        opcao_final_exclusao = input("Você tem certeza que deseja excluir essa transação? [S / N] ").strip().upper()[0]
    
        while opcao_final_exclusao not in ["S", "N"]:
            opcao_final_exclusao = input("\nOpção inválida. Você tem certeza que deseja excluir essa transação? [S / N] ").strip().upper()[0]
    
        if opcao_final_exclusao == "S":
            # Excluir o arquivo
            del(bd[indice])
            
            print("\nExclusão realizada com sucesso. Retornando ao Menu Principal\n")
            run()
            
        else:
            print("\nExclusão cancelada. Retornando ao menu principal\n")
            run()
        

# -----------------------
# ABAIXO PODE ALTERAR
# -----------------------
#limpar console (opcional)
os.system('cls' if os.name == 'nt' else 'clear')
# inicia o programa
run()