# -----------------------
# depencies
# -----------------------
import json
import os
import uuid
import random
import sys
from datetime import datetime
from time import sleep


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


# -----------------------
# PROGRAM functions 
# -----------------------
# pode editar como quiser as funções abaixo! Somente não altere os nomes das funções.
# para alterar as funções abaixo, basta apagar o `pass` e preencher com as instruções.


def validar_nome_usuario():
    nome_usuario = input("\nDigite seu nome: ")
    
    print(f"\nO nome digitado foi: {nome_usuario}")
    
    continuar_login = input("O nome está correto? [S / N]   ").strip().upper()
    
    if continuar_login == "S":
        return nome_usuario
    else:
        return validar_nome_usuario()



def validar_conta_usuario():
    conta_usuario = input("\nDigite o número da conta sem o dígito: ")

    try:
      conta_usuario = int(conta_usuario)
      if conta_usuario <= 0:
          raise Exception("Número de conta inválido.")

    except ValueError:
      print("Digite somente números.")
      return validar_conta_usuario()

    except TypeError:
      print("Digite somente números.")
      return validar_conta_usuario()

    except Exception as e:
      print(f"{e} Tente novamente")
      return validar_conta_usuario()

    except:
      print("Erro. Tente Novamente")
      return validar_conta_usuario()
    else:
      continuar = input(f"Conta digitada: {conta_usuario}. Deseja continuar? [S / N]  ").strip().upper()
      while continuar not in ["S", "N"]:
        continuar = input(f"Opção inválida. Conta digitada: {conta_usuario}. Deseja continuar? [S / N]  ").strip().upper()
      if continuar == "S":
        return str(conta_usuario)
      else:
        return validar_conta_usuario()
     
     
def validar_digito_conta_usuario():
    digito_conta = input("\nDigite o dígito da conta: ")

    try:
      digito_conta = int(digito_conta)
      if digito_conta < 0 or digito_conta > 9:
        raise Exception("Dígito inválido.")

    except ValueError:
      print("Digite somente números.")
      return validar_digito_conta_usuario()
    
    except TypeError:
      print("Digite somente números.")
      return validar_digito_conta_usuario()

    except Exception as e:
      print(f"{e} Tente novamente")
      return validar_digito_conta_usuario()

    except:
      print("Erro. Tente novamente.")
      return validar_digito_conta_usuario

    else:
      continuar = input(f"Dígito digitado: {digito_conta}. Deseja continuar? [S / N]  ").strip().upper()

      while continuar not in ["S", "N"]:
        continuar = input(f"Opção inválida. Dígito digitado: {digito_conta}. Deseja continuar? [S / N]  ").strip().upper()

      if continuar == "S":
        return str(digito_conta)

      else:
        return validar_digito_conta_usuario()      


def definir_conta():
    conta_usuario = validar_conta_usuario()
    digito_conta_usuario = validar_digito_conta_usuario()
    conta_final_usuario = str(conta_usuario) + "-" + str(digito_conta_usuario)
    return conta_final_usuario

def informacoes_login():

    print("Bem vindo ao banco Santander - Ada Tech.")
    print("Para acessar, insira suas informações de login\n")
    nome_usuario = validar_nome_usuario()
    conta_usuario = definir_conta()
    return nome_usuario, conta_usuario
    
    
def imprimir_menu_opcoes(menu):
    """
    Essa função imprime as opções do menu na tela
    """
    
    if menu == "menu_inicial":
        print(f"\nBem-vindo {nome_usuario}!")
        print(f'conta: {conta_usuario}')
        print("\nEste programa permite gerenciar transações de sua conta pessoal.")
        print("\nEscolha uma das opções abaixo:")
        print("1. Visualizar relatórios")
        print("2. Cadastrar transações")
        print("3. Editar transações")
        print("4. Excluir transações")
        print("-" * 10)
        print("0. Sair")
        print('\n')

    elif menu == "visualizar_relatorios":
        
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

    elif menu == "cadastrar_transacao":
        
        print("\nDeseja continuar o cadastro dessa transação?")
        print("1. Confirmar cadastro da transação")
        print("2. Refazer o cadastro da transação")
        print("0. Cancelar cadastro e voltar ao menu inicial\n")

    elif menu == "editar_transacao":
        
        print("Escolha a opção que deseja editar")
        print("1. Valor")
        print("2. Categoria")
        print("0. Retornar ao Menu Principal")

    elif menu == "repetir_cadastrar_transacao":
        
        print("\nDeseja cadastrar uma nova transação?")
        print("1. Sim")
        print("0. Retornar ao Menu Principal")

    elif menu == "repetir_editar_transacao":
        
        print("\nDeseja editar uma nova transaçao?")
        print("1. Sim")
        print("0. Retornar ao Menu Principal")

    elif menu == "repetir_excluir_transacao":
        
        print("\nDeseja excluir uma nova transação?")
        print("1. Sim")
        print("0. Retornar ao Menu Principal")

    elif menu == "categoria_transacao":
        print("\nEscolha uma categoria para essa transação: ")
        print("1. Casa")
        print("2. Lazer")
        print("3. Viagens")
        print("4. Investimentos")
        print("5. Transferências")
        print("6. Saúde")
        print("7. Alimentação")
        print("0. Retornar ao Menu Principal")

    elif menu == "escolha_categoria_relatorio":
        print("\nEscolha uma categoria para gerar o relatório:")
        print("1. Casa")
        print("2. Lazer")
        print("3. Viagens")
        print("4. Investimentos")
        print("5. Transferências")
        print("6. Saúde")
        print("7. Alimentação")
        print("8. Valor total da conta")
        print("0. Retornar ao Menu Principal")


def validar_opcao(menu):
    """
    Função para validar a opção do usuário no menu
    """
    quantidade_opcoes_menu = {"menu_inicial" : 4, "visualizar_relatorios": 6, "cadastrar_transacao": 2,
                              "editar_transacao": 2, "repetir_cadastrar_transacao": 1, "repetir_editar_transacao" : 1,
                              "repetir_excluir_transacao": 1, "categoria_transacao": 7, "escolha_categoria_relatorio": 8}

    imprimir_menu_opcoes(menu)

    opcao_usuario = input("Digite a opção desejada: ").strip()

    global trava_menu
    trava_menu = False

    while not trava_menu:
    
        try:
            opcao_usuario = int(opcao_usuario)
            if opcao_usuario < 0 or opcao_usuario > quantidade_opcoes_menu[menu]:
                raise Exception("Opção não existente.")
                
        except ValueError:
            print("\nOpção inválida. Digite somente números. Tente novamente.")
            print("")
            validar_opcao(menu)
            
        except Exception as e:
            print(f"\n{e} Tente novamente.")
            print("")
            validar_opcao(menu)

        except:
            print("Erro. Tente novamente.")
            validar_opcao(menu)
            
        else:
            trava_menu = True
            return opcao_usuario
        

def refazer_operacao(menu):

    opcao_usuario = validar_opcao(menu)

    if opcao_usuario == 1 and menu == "repetir_cadastrar_transacao":
        return cadastrar_transacao()

    elif opcao_usuario == 1 and menu == "repetir_editar_transacao":
        return editar_transacao_por_ID()

    elif opcao_usuario == 1 and menu == "repetir_excluir_transacao":
        return excluir_transacao()

    else:
        return run()


def escolher_categoria_transacao():
    
    dict_categoria = {
        "1": "casa",
        "2": "lazer",
        "3": "viagens",
        "4": "investimentos",
        "5": "transferencias",
        "6": "saude",
        "7": "alimentacao"
        }
    
    opcao_usuario = validar_opcao("categoria_transacao")
    
    if opcao_usuario == 8:
        return opcao_usuario

    else:
        return dict_categoria[str(opcao_usuario)]
    
def tela_login_eterna():
    
    nome_usuario, conta_usuario = informacoes_login()
    
    return run()
    

def run():
    """
    Esta é a função principal que vai rodar o programa
    """  
    print("\nCarregando Menu...")
    
    sleep(3)
    
    os.system('cls' if os.name == 'nt' else 'clear')

    opcao_usuario = validar_opcao("menu_inicial")
    
    if opcao_usuario == 0:
        print("Você deslogou do sistema. Obrigado e volte sempre.\n")
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        return tela_login_eterna()
        
    elif opcao_usuario == 1:
        visualizar_relatorios()

    elif opcao_usuario == 2:    
        cadastrar_transacao()
        
    elif opcao_usuario == 3:
        editar_transacao_por_ID()
        
    else:
        print("\nMenu excluir transação\n")
        excluir_transacao()

        
def visualizar_relatorios():

    """
    Mostra um menu de opcoes no qual gera relatórios com base na escolha do usuário.
    """

    opcao_usuario = validar_opcao("visualizar_relatorios")


    if opcao_usuario == 0:
        print("Retornando ao menu principal")
        return run()
        
    elif opcao_usuario == 1:
        return calcular_total_transacoes()

    elif opcao_usuario == 2:
        return mostrar_m5_transacoes("max")
   
    elif opcao_usuario == 3:
        return mostrar_m5_transacoes("mean")

    elif opcao_usuario == 4:
        return mostrar_m5_transacoes("min")

    elif opcao_usuario == 5:
        return calcular_media()

    else:
        return consultar_transacao_por_ID()


def conteudo_transacao_especifica(lista_transacoes, indice, imprimir_na_tela=False):
    
    transacao_especifica = f"""
        ID: {lista_transacoes[indice]["UUID"]}\n
        Valor: R$ {lista_transacoes[indice]["valor"]:.2f}\n
        Categoria: {lista_transacoes[indice]["categoria"]}
        """
    if imprimir_na_tela == True:
        print(transacao_especifica)
    else:
        return transacao_especifica



def encontrar_transacao_por_chave_valor(lista_transacoes, chave, valor):
    for i, transacao in enumerate(lista_transacoes):
        if transacao.get(chave) == valor:
            return i # Retorna o índice na lista, caso encontre
    return -1  # Retorna -1 se não encontrar

def definir_categoria_filtragem(opcao_usuario):
    
    dict_categoria = {
    "1": "casa",
    "2": "lazer",
    "3": "viagens",
    "4": "investimentos",
    "5": "transferencias",
    "6": "saude",
    "7": "alimentacao"
    }
    
    opcao_usuario = str(opcao_usuario)
    
    return dict_categoria[opcao_usuario]


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

        #Concatenação de data e hora no nome do arquivo para que não sobrescrevam arquivos do mesmo modelo.
        data_hora_atual = datetime.now()
        data_hora_str = data_hora_atual.strftime('%Y-%m-%d_%H-%M-%S')

        
        nome_arquivo = str(nome_arquivo) + "_" + data_hora_str + ".txt"
        caminho_arquivo = os.path.join(pasta_relatorios, nome_arquivo)

        if type(conteudo) == list:
            
            with open(caminho_arquivo, "w", encoding="utf-8") as relatorio_txt:
                for linha in conteudo:
                    relatorio_txt.write(linha)
                    relatorio_txt.write("\n")
            
            print(f"\nArquivo salvo sob o nome {nome_arquivo} na pasta relatorios.\n")
    
            print("Voltando ao menu principal\n")
            return run()


        else:
            
            with open(caminho_arquivo, "w", encoding="utf-8") as relatorio_txt:
                relatorio_txt.write(conteudo)
            
            print(f"\nArquivo salvo sob o nome {nome_arquivo} na pasta relatorios.\n")
    
            print("Voltando ao menu principal\n")
            return run()
            

    else:
        print("\nVoltando ao menu principal\n")
        return run()


def calcular_total_transacoes():
    """
    Calcula o valor total de transações da conta.
    Utilize essa mesma função para o caso `por categoria`
    """

    opcao_usuario = validar_opcao("escolha_categoria_relatorio")
    
    if opcao_usuario == 8:
        total_transacoes = sum(float(transacao["valor"]) for transacao in bd)
        conteudo_relatorio_total_transacoes = f"O valor total de transações registradas foi de R$ {total_transacoes:.2f}"
        nome_relatorio = "relatorio_total_transacoes"


    else:
        categoria_para_filtrar = definir_categoria_filtragem(opcao_usuario)
        total_transacoes = sum(float(transacao["valor"]) for transacao in bd if transacao["categoria"] == categoria_para_filtrar)
        conteudo_relatorio_total_transacoes = f"O valor total de transações registradas da categoria {categoria_para_filtrar.capitalize()} foi de R$ {total_transacoes:.2f}"
        nome_relatorio = "relatorio_total_transacoes_" + categoria_para_filtrar

    print("")

    print(conteudo_relatorio_total_transacoes)

    print("")
    
    return salvar_relatorio(nome_relatorio, conteudo_relatorio_total_transacoes)


def mostrar_m5_transacoes(parametro):
    """
    Mostra as m5 transações realizadas, sendo m parâmetro que deve ser adicionada à função.
    \nm : 'max','min','median', sendo 
    \n\t'max' mostra os top 5 maior valor,
    \n\t'min' mostra os top 5 menor valor,
    \n\t'mean' mostra os top 5 valores próximos a média
    
    Utilize essa mesma função para o caso `por categoria`
    """

    opcao_usuario = validar_opcao("escolha_categoria_relatorio")
    
    if opcao_usuario == 8:
        dados = bd

    else:
        categoria_para_filtrar = definir_categoria_filtragem(opcao_usuario)
        dados = [transacao for transacao in bd if transacao["categoria"] == categoria_para_filtrar]

    if parametro == "max":

        dados_ordenados =  sorted(dados, key=lambda x: x['valor'], reverse=True)[0:5]

        if opcao_usuario == 8:
            
            conteudo_relatorio_max5_transacoes = ["As 5 maiores transações são: \n"]
    
            print("")
            print(conteudo_relatorio_max5_transacoes[0])
            for idx, dado in enumerate(dados_ordenados):
                transacao_lista_temp = f"{idx+1}: {dado}\n"
                print(transacao_lista_temp)
                
                conteudo_relatorio_max5_transacoes.append(transacao_lista_temp)
    
            return salvar_relatorio("relatorio_5_maiores_transacoes", conteudo_relatorio_max5_transacoes)

        else:
            
            conteudo_relatorio_max5_transacoes = [f"As 5 maiores transações da categoria {categoria_para_filtrar.capitalize()} são \n"]

            print("")
            print(conteudo_relatorio_max5_transacoes[0])
            for idx, dado in enumerate(dados_ordenados):
                transacao_lista_temp = f"{idx+1}: {dado}\n"
                print(transacao_lista_temp)
                
                conteudo_relatorio_max5_transacoes.append(transacao_lista_temp)

            nome_relatorio = "relatorio_5_maiores_transacoes_" + categoria_para_filtrar
    
            return salvar_relatorio(nome_relatorio, conteudo_relatorio_max5_transacoes)
            

    elif parametro == "min":
        dados_ordenados =  sorted(dados, key=lambda x: x['valor'], reverse=False)[0:5]

        if opcao_usuario == 8:
            
            conteudo_relatorio_min5_transacoes = ["As 5 menores transações são: \n"]
            
            print("")
            print(conteudo_relatorio_min5_transacoes[0])
            for idx, dado in enumerate(dados_ordenados):
                transacao_lista_temp = f"{idx+1}: {dado}\n"
                print(transacao_lista_temp)
                
                conteudo_relatorio_min5_transacoes.append(transacao_lista_temp)
    
            return salvar_relatorio("relatorio_5_menores_transacoes", conteudo_relatorio_min5_transacoes)

        else:

            conteudo_relatorio_min5_transacoes = [f"As 5 menores transações da categoria {categoria_para_filtrar.capitalize()} são: \n"]
            
            print("")
            print(conteudo_relatorio_min5_transacoes[0])
            for idx, dado in enumerate(dados_ordenados):
                transacao_lista_temp = f"{idx+1}: {dado}\n"
                print(transacao_lista_temp)
                
                conteudo_relatorio_min5_transacoes.append(transacao_lista_temp)

            nome_relatorio = "relatorio_5_menores_transacoes_" + categoria_para_filtrar
            
            return salvar_relatorio(nome_relatorio, conteudo_relatorio_min5_transacoes)            


    elif parametro == "mean":

        dados_ordenados =  sorted(dados, key=lambda x: x['valor'], reverse=False)
        indice_mediano = len(dados_ordenados) // 2
        transacoes_medianas = dados_ordenados[indice_mediano-2:indice_mediano+3]

        if opcao_usuario == 8:
            
            conteudo_relatorio_mean5_transacoes = ["As 5 transações medianas são: \n"]
            
            print("")
            print(conteudo_relatorio_mean5_transacoes[0])
            for idx, dado in enumerate(transacoes_medianas):
                transacao_lista_temp = f"{idx+1}: {dado}\n"
                print(transacao_lista_temp)
                
                conteudo_relatorio_mean5_transacoes.append(transacao_lista_temp)
        
            return salvar_relatorio("relatorio_5_transacoes_medianas", conteudo_relatorio_mean5_transacoes)

        else:
            
            conteudo_relatorio_mean5_transacoes = [f"As 5 transações medianas da categoria {categoria_para_filtrar.capitalize()} são: \n"]
            
            print("")
            print(conteudo_relatorio_mean5_transacoes[0])
            for idx, dado in enumerate(transacoes_medianas):
                transacao_lista_temp = f"{idx+1}: {dado}\n"
                print(transacao_lista_temp)
                
                conteudo_relatorio_mean5_transacoes.append(transacao_lista_temp)
        
            nome_relatorio = "relatorio_5_transacoes_medianas_" + categoria_para_filtrar
            return salvar_relatorio(nome_relatorio, conteudo_relatorio_mean5_transacoes)

            

def calcular_media():
    """
    Calcula a média dos valores das transações.
    Utilize essa mesma função para o caso `por categoria`
    """

    opcao_usuario = validar_opcao("escolha_categoria_relatorio")
    
    if opcao_usuario == 8:
        dados = bd

    else:
        categoria_para_filtrar = definir_categoria_filtragem(opcao_usuario)
        dados = [transacao for transacao in bd if transacao["categoria"] == categoria_para_filtrar]
      
    
    total_transacoes = sum(float(transacao["valor"]) for transacao in dados)
    quantidade_transacoes = len(dados)

    media_valores_transacoes = total_transacoes / quantidade_transacoes

    if opcao_usuario == 8: 
        conteudo_media_valores_transacoes = f"A média de valores das transações dessa conta é de R$ {media_valores_transacoes:.2f}"
    
        print("")
        print(conteudo_media_valores_transacoes)
        print("")
        
        return salvar_relatorio("relatorio_media_valores_transacoes", conteudo_media_valores_transacoes)

    else:
        conteudo_media_valores_transacoes = f"A média de valores das transações dessa conta na categoria {categoria_para_filtrar.capitalize()} é de R$ {media_valores_transacoes:.2f}"
    
        print("")
        print(conteudo_media_valores_transacoes)
        print("")

        nome_relatorio = "relatorio_media_valores_transacoes_" + categoria_para_filtrar
        
        return salvar_relatorio(nome_relatorio, conteudo_media_valores_transacoes)

            

def calcular_media():
    """
    Calcula a média dos valores das transações.
    Utilize essa mesma função para o caso `por categoria`
    """

    opcao_usuario = validar_opcao("escolha_categoria_relatorio")
    
    if opcao_usuario == 8:
        dados = bd

    else:
        categoria_para_filtrar = definir_categoria_filtragem(opcao_usuario)
        dados = [transacao for transacao in bd if transacao["categoria"] == categoria_para_filtrar]
      
    
    total_transacoes = sum(float(transacao["valor"]) for transacao in dados)
    quantidade_transacoes = len(dados)

    media_valores_transacoes = total_transacoes / quantidade_transacoes

    if opcao_usuario == 8: 
        conteudo_media_valores_transacoes = f"A média de valores das transações dessa conta é de R$ {media_valores_transacoes:.2f}"
    
        print("")
        print(conteudo_media_valores_transacoes)
        print("")
        
        return salvar_relatorio("relatorio_media_valores_transacoes", conteudo_media_valores_transacoes)

    else:
        conteudo_media_valores_transacoes = f"A média de valores das transações dessa conta na categoria {categoria_para_filtrar.capitalize()} é de R$ {media_valores_transacoes:.2f}"
    
        print("")
        print(conteudo_media_valores_transacoes)
        print("")

        nome_relatorio = "relatorio_media_valores_transacoes_" + categoria_para_filtrar
        
        return salvar_relatorio(nome_relatorio, conteudo_media_valores_transacoes)
    

def consultar_transacao_por_ID():
    """
    Consulta uma transação específica pelo seu UUID.
    """

    print("\nConsulta de transação por ID\n")
    id_consulta = input("Digite o ID único de transação para edição (Digite 0 para voltar ao menu inicial): ").strip().lower()
    
    if id_consulta == "0":
        print("\nRetornando ao Menu Inicial\n")
        return run()

    indice = encontrar_transacao_por_chave_valor(bd, "UUID", id_consulta)

    if indice == -1:
        print("\nTransação não encontrada. Tente novamente")
        return consultar_transacao_por_ID()

    else:
        print("\nTrasanção encontrada!\n")

        transacao_especifica = conteudo_transacao_especifica(lista_transacoes=bd, indice=indice, imprimir_na_tela=False)
        print(transacao_especifica)
        
        
        nome_arquivo_transacao_especifica = "relatorio_transacao_id_" + id_consulta
        
        return salvar_relatorio(nome_arquivo_transacao_especifica, transacao_especifica)

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
            
        except:
            print("Erro. Tente novamente.")
                   
    if valor_transacao == 0:
        print("\nRetornando ao menu inicial.\n")
        return run()
    
    valor_transacao = round(valor_transacao, 2)

    return valor_transacao

def cadastrar_transacao():
    """
    Cadastra uma nova transação.
    \nObs:Para gerar um novo uuid, veja como é feito na função `criar_transacoes`.
    """
    print("\nCadastro de novas transações")
    print("-"*10)

    # Criação de ID automática

    UUID = str(uuid.uuid4())
    
    print("Para cancelar o cadastro e voltar ao menu inicial, digite 0\n")

    valor_transacao = valor_transacao_cadastro()

    categoria_transacao_cadastro = escolher_categoria_transacao()

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

    continuar_cadastro = validar_opcao("cadastrar_transacao")

    if continuar_cadastro == 1:
        bd.append(transacao)
        print("\nTransação cadastrada com sucesso\n")
        return refazer_operacao("repetir_cadastrar_transacao")

    elif continuar_cadastro == 2:
        return cadastrar_transacao()

    else:
        print("\nCadastro cancelado. Retornando ao menu inicial\n")
        return run()



def editar_transacao_por_ID():
    """
    Edita uma transação específica pelo seu UUID.
    """

    print("\nEditor de transação")
    print("\nConsulta de transação por ID\n")
    
    id_consulta = input("Digite o ID único de transação para consulta (Digite 0 para voltar ao menu principal): ").strip().lower()

    if id_consulta == "0":
        print("Retornando ao menu principal")
        return run()

    indice = encontrar_transacao_por_chave_valor(bd, "UUID", id_consulta)

    if indice == -1:
        print("\nTransação não encontrada.")
        return refazer_operacao("repetir_editar_transacao")


    else:
        print("\nTrasanção encontrada!\n")
        conteudo_transacao_especifica(lista_transacoes=bd, indice=indice, imprimir_na_tela=True)

        opcao_usuario = validar_opcao("editar_transacao")
    
        if opcao_usuario == 1:
            novo_valor_transacao = opcao_usuario()
            bd[indice]["valor"] = novo_valor_transacao
            
            print("\nEdição concluída com sucesso. Novos dados dessa transação abaixo: \n")

            conteudo_transacao_especifica(lista_transacoes = bd, indice = indice, imprimir=True)
            
            print("\nRetornando ao Menu Inicial\n")
            return run()
    
    
        elif opcao_usuario == 2:
            nova_categoria_transacao = escolher_categoria_transacao()
            bd[indice]["categoria"] = nova_categoria_transacao
            
            print("\nEdição concluída com sucesso. Novos dados dessa transação abaixo: \n")
            conteudo_transacao_especifica(lista_transacoes = bd, indice = indice, imprimir=True)
            return refazer_operacao("repetir_editar_transacao")

        
        else:
            print("\nEdição cancelada. Retornando ao Menu Principal\n")
            return run()


def excluir_transacao():
    """
    Exclui uma transação específica pelo UUID.
    """

    print("\nExclusão de transações")
    id_consulta = input("Digite o ID único de transação para exclusão (Digite 0 para voltar ao menu principal): ").strip().lower()

    if id_consulta == "0":
        print("Retornando ao menu principal")
        return run()

    indice = encontrar_transacao_por_chave_valor(bd, "UUID", id_consulta)

    if indice == -1:
        print("\nTransação não encontrada.")
        return refazer_operacao("repetir_excluir_transacao")

    else:
        print("\nTrasanção encontrada!\n")
        print("Dados da transação a ser excluída:\n")
        
        conteudo_transacao_especifica(lista_transacoes=bd, indice=indice, imprimir_na_tela=True)
        
        opcao_final_exclusao = input("Você tem certeza que deseja excluir essa transação? [S / N] ").strip().upper()[0]
    
        while opcao_final_exclusao not in ["S", "N"]:
            opcao_final_exclusao = input("\nOpção inválida. Você tem certeza que deseja excluir essa transação? [S / N] ").strip().upper()[0]
    
        if opcao_final_exclusao == "S":
            # Excluir o arquivo
            del(bd[indice])
            
            print("\nExclusão realizada com sucesso.")
            return refazer_operacao("repetir_excluir_transacao")
            
        else:
            print("\nExclusão cancelada. Retornando ao menu principal\n")
            return run()


# -----------------------
# ABAIXO PODE ALTERAR
# -----------------------
#limpar console (opcional)
os.system('cls' if os.name == 'nt' else 'clear')

# inicia o programa
nome_usuario, conta_usuario = informacoes_login()


run()