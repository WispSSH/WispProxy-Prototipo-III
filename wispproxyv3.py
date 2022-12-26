import re
import requests
import os
import time
import ipcalc
import sys
import json
from requests.exceptions import Timeout
from requests.structures import CaseInsensitiveDict
from datetime import datetime
from threading import Thread

try:
    try:
        login = requests.get("https://bitbin.it/tZs3Lj74/raw/").text
    except:
        print("Conecte-se a internet para executar!")
        print("Caso a mensagem persista chame o desenvolvedor ou atualize o script!")
        time.sleep(5)
        exit(0)
    if os.path.isfile("chave") == True:
        arquivo = open("chave", "r+")
        chave = arquivo.read()
        arquivo.close()
        if chave == login:
            pass
        else:
            print("┌──────────────────────────────┐")
            print("│  Script em desenvolvimento!  │")
            print("├──────────────────────────────┤")
            print("│       Chave No Grupo         │")
            print("│ https://t.me/wispssh_central │")
            print("├──────────────────────────────┘")
            print("│ Adicione a chave para executar o script!")
            chave = input("│─> ")
            print("Deseja salvar a chave para entrar automaticamente?")
            salvar = input("S/N : ")
            if salvar in ["S", "s"]:
                arquivo = open("chave", "w+")
                arquivo.write(chave)
                arquivo.close()
            else:
                pass
    else:
        print("┌──────────────────────────────┐")
        print("│  Script em desenvolvimento!  │")
        print("├──────────────────────────────┤")
        print("│       Chave No Grupo         │")
        print("│ https://t.me/wispssh_central │")
        print("├──────────────────────────────┘")
        print("│ Adicione a chave para executar o script!")
        chave = input("│─> ")
        print("Deseja salvar a chave para entrar automaticamente?")
        salvar = input("S/N : ")
        if salvar in ["S", "s"]:
            arquivo = open("chave", "w+")
            arquivo.write(chave)
            arquivo.close()
        else:
            pass

    if chave == login:
        pass
    else:
        print("Chave invalida!")
        print("Verifique se há alguma atualização ou espaçamento!")
        time.sleep(5)
        exit(0)
except:
    exit(0)

try:
    def sair():
        logo = (f"""┌─────────────────────────────────────────────────────────────────┐
│{config.cor}  _       _                     ___                              {cores.branco}│ 
│{config.cor} ( )  _  ( ) _                 (  _`\                            {cores.branco}│
│{config.cor} | | ( ) | |(_)  ___  _ _      | |_) ) _ __    _          _   _  {cores.branco}│
│{config.cor} | | | | | || |/',__)( '_`\    | ,__/'( '__) /'_`\ (`\/')( ) ( ) {cores.branco}│
│{config.cor} | (_/ \_) || |\__, \| (_) )   | |    | |   ( (_) ) >  < | (_) | {cores.branco}│
│{config.cor} `\___x___/'(_)(____/| ,__/'   (_)    (_)   `\___/'(_/\_)`\__, | {cores.branco}│
│{config.cor}                     | |                                 ( )_| | {cores.branco}│
│{config.cor}                     (_)                                 `\___/' {cores.branco}│
├─────────────────────────────────────────────────────────────────┤
│{config.cor} Saindo...                                                       {cores.branco}│
└─────────────────────────────────────────────────────────────────┘""")
        inicio2 = 3
        limpar()
        print(logo)
        for inicio in range(4):
            print(f"{config.cor}> Contagem {inicio2}...{cores.branco}", end="\r")
            inicio2 = inicio2 - 1
            time.sleep(1)

    data = datetime.today().strftime('%d-%m-%Y_%Hh-%Mm')

    class cores():
        vermelho = "\033[1;31m"
        verde = "\033[1;32m"
        branco = "\033[1;37m"
        fpreto = "\033[40;1;37m"

    def lista_verificar():
        verificar_lista = os.path.exists("lista.txt")
        if verificar_lista == True:
            pass
        else:
            open("lista.txt", "w")
        verificar_vazio = os.path.getsize("lista.txt") > 0
        if verificar_vazio == False:
            print("┌──────────────────────┐")
            print("│     Lista vazia      │")
            print("│ Voltando para o menu │")
            print("└──────────────────────┘")
            time.sleep(3)
            menu()
        else:
            pass

    def limpar():
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    class config():
        config_existe = os.path.exists("config.txt")
        if config_existe == True:
            pass
        else:
            config = open("config.txt", "w")
            config.write(
                "Cores={roxo}\nVelocidade={normal}\nDominio={seuservidor}\n_USE_O_MENU_PARA_EDITAR_")
            config.close()
        config = open("config.txt", "r")
        config = config.read()
        # cores
        try:
            cores_config = config.split("Cores={")[1].split("}")[0]
            if cores_config == "azul":
                cor = "\033[1;34m"
            elif cores_config == "vermelho":
                cor = "\033[1;31m"
            elif cores_config == "verde":
                cor = "\033[1;32m"
            elif cores_config == "branco":
                cor = "\033[1;37m"
            elif cores_config == "roxo":
                cor = "\033[1;35m"
            else:
                cor = "\033[1;35m"
        except:
            cor = "\033[1;35m"
        # velocidade
        try:
            velocidade_config = config.split("Velocidade={")[1].split("}")[0]
            if velocidade_config == "muito-rapido":
                velocidade = 1
            elif velocidade_config == "rapido":
                velocidade = 2
            elif velocidade_config == "moderado":
                velocidade = 3
            elif velocidade_config == "normal":
                velocidade = 4
            elif velocidade_config == "devagar":
                velocidade = 5
            else:
                velocidade = 4
        except:
            velocidade = 4

        #dominio
        try:
            dominio_config = config.split("Dominio={")[1].split("}")[0]
        except:
            pass

    def menu():
        limpar()
        # ┌─┐
        # │ │
        # ├─┤
        # └─┘
        logo = (f"""┌─────────────────────────────────────────────────────────────────┐
│{config.cor}  _       _                     ___                              {cores.branco}│ 
│{config.cor} ( )  _  ( ) _                 (  _`\                            {cores.branco}│
│{config.cor} | | ( ) | |(_)  ___  _ _      | |_) ) _ __    _          _   _  {cores.branco}│
│{config.cor} | | | | | || |/',__)( '_`\    | ,__/'( '__) /'_`\ (`\/')( ) ( ) {cores.branco}│
│{config.cor} | (_/ \_) || |\__, \| (_) )   | |    | |   ( (_) ) >  < | (_) | {cores.branco}│
│{config.cor} `\___x___/'(_)(____/| ,__/'   (_)    (_)   `\___/'(_/\_)`\__, | {cores.branco}│
│{config.cor}                     | |                                 ( )_| | {cores.branco}│
│{config.cor}                     (_)                                 `\___/' {cores.branco}│
│{config.cor}                                                                 {cores.branco}│
├─────────────────────────────────────────────────────────────────┤""")
        print(logo)
        print(f"│ {config.cor}Desenvolvido por WispSSH {cores.branco}                                       │")
        print(f"│ {config.cor}NET ON = Wi-Fi ligado{cores.branco}                                           │")
        print(f"│ {config.cor}NET OFF = Dados Moveis sem internet{cores.branco}                             │")
        print("├─────────────────────────────────────────────────────────────────┤")
        print(f"│ {config.cor}✵  Prototipo Final{cores.branco}                                              │")
        print(f"│ {config.cor}✵  Versão Gratuita{cores.branco}                                              │")
        print(f"│ {config.cor}✵  Grupo https://t.me/wispssh_central{cores.branco}                           │")
        print("├─────────────────────────────────────────────────────────────────┤")
        print(f"│ {config.cor}1-> Ip Scanner (0-255) (NET OFF){cores.branco}                                │")
        print(f"│ {config.cor}2-> Lista Scanner (NET OFF){cores.branco}                                     │")
        print(f"│ {config.cor}3-> Proxy Finder (NET ON/OFF){cores.branco}                                   │")
        print(f"│ {config.cor}4-> Resultados{cores.branco}                                                  │")
        print(f"│ {config.cor}5-> Configurações{cores.branco}                                               │")
        print(f"│ {config.cor}6-> Reiniciar{cores.branco}                                                   │")
        print(f"│ {config.cor}7-> Atualizar{cores.branco}                                                   │")
        print(f"│ {config.cor}0-> Sair{cores.branco}                                                        │")
        print("├─────────────────────────────────────────────────────────────────┘")
        opcao = input("│─> ")
        if opcao == "0":
            sair()
        elif opcao == "1":
            try:
                print("│ Coloque o ip desejado (Ex: 128.0.0.x)")
                colocar_ip = input("│─> ")
                colocar_ip = colocar_ip.replace("x", "")
                for index in range(256):
                    t1 = Thread(target=lista_scanner,args=(f"{colocar_ip}{index}",))
                    t1.start()
                time.sleep(3)
                menu()
            except KeyboardInterrupt:
                sair()

            except:
                print("Não foi possivel executar, contate o desenvolvedor!")
                time.sleep(3)
                menu()
        elif opcao == "2":
            try:
                inicio = time.time()
                lista = []
                arquivo = open("lista.txt", "r", encoding="utf-8")
                item = arquivo.read().split('\n')
                for addlista in item:
                    adicionar = addlista.replace(" ", "")
                    lista.append(adicionar)
                lista = list(filter(None, lista))
                arquivo.close()
                print(f"Encontrei {len(lista)} Itens!")
                time.sleep(3)
                threads = []
                for index in range(len(lista)):
                    t1 = Thread(target=lista_scanner, args=(lista[index].replace(" ", ""),))
                    t1.start()
                    threads.append(t1)       
                for thread_fim in threads:
                    thread_fim.join()
                fim = time.time() - inicio
                fim = int(fim)
                input(f"Tempo da verificação : {fim:.2f} segundos") 
                menu()
            except KeyboardInterrupt:
                sair()

            except:
                print("Não foi possivel executar, contate o desenvolvedor!")
                time.sleep(3)
                menu()
        elif opcao == "3":
            try:
                print("┌───────────────────────────────────────────────────────────────────┐")
                print("│ Ative seu Wi-Fi para atualizar a lista de ip que será verificada! │")
                print("│                      *IP LIST CLOUDFLARE*                         │")
                print("│                      ENTER para continuar                         │")
                input("└───────────────────────────────────────────────────────────────────┘")

                def conexao():
                    try:
                        requests.get("http://google.com")
                        pass
                    except:
                        print("Sem conexão com a internet!")
                        time.sleep(3)
                        menu()
                conexao()
                cloudipv4 = requests.get(
                    "https://www.cloudflare.com/ips-v4").text.split("\n")
                print("┌───────────────────────────────────────────────────────────────────┐")
                print("│ Ative seus DADOS MOVEIS sem internet para começar a verificação!  │")
                print("│                      ENTER para continuar                         │")
                input("└───────────────────────────────────────────────────────────────────┘")

                def cloudflare():
                    try:
                        #cloudipv4 = requests.get("https://www.cloudflare.com/ips-v4").text.split("\n")
                        print(f"Encontramos : {len(cloudipv4)} cloudflare ip!")
                        print("Iniciando verificação, vai demorar!")
                        time.sleep(3)
                        for i in cloudipv4:
                            for x in ipcalc.Network(i):
                                t1 = Thread(target=lista_scanner, args=(x,))
                                t1.start()
                        time.sleep(3)
                        menu()
                    except:
                        print(
                            "Houve um erro ao coletar os dados e iniciar a verificação!")
                        time.sleep(3)
                        menu()
                cloudflare()
                time.sleep(3)
                menu()
            except KeyboardInterrupt:
                sair()
            except:
                print("Não foi possivel executar, contate o desenvolvedor!")
                time.sleep(3)
                menu()

        elif opcao == "4":
            try:
                if os.path.exists("resultado") == True:
                    resultados = 0
                    for x in os.listdir("resultado"):
                        resultados += 1
                        print(f"{resultados} - {x}")
                    print(f"\n{resultados} Resultado encontrados.")
                    print("Qual resultado deseja visualizar? (numero)")
                    abrir = input("│─> ")
                    escolha = os.listdir("resultado")[int(abrir)-1]
                    arquivo = open(f"resultado/{escolha}", "r+")
                    print(f"\nArquivo : {escolha}\n")
                    print(arquivo.read())
                    arquivo.close()
                    voltar = input(
                        "Escreva *deletar* para apagar! ou ENTER para continuar!")
                    if voltar == "deletar":
                        os.remove(f"resultado/{escolha}")
                    menu()

                else:
                    print("Sem resultados")
                    time.sleep(3)
                    menu()
            except:
                print("Houve um erro ao execultar o comando!")
                menu()
        elif opcao == "5":
            try:
                print(f"""├────────────────────────┐
│{config.cor} 1 - Alterar Cor        {cores.branco}│
│{config.cor} 2 - Alterar Velocidade {cores.branco}│
│{config.cor} 3 - Alterar Dominio    {cores.branco}│
├────────────────────────┘""")
                escolha = input("│─> ")
                if escolha == "1":
                    with open("config.txt", "r") as arquivo:
                        cor_atual = arquivo.read().split("Cores={")[1].split("}")[0]
                        arquivo.close()
                    print(f"""├──────────────┐
│{config.cor} 1 - Vermelho {cores.branco}│
│{config.cor} 2 - Azul     {cores.branco}│
│{config.cor} 3 - Verde    {cores.branco}│
│{config.cor} 4 - Branco   {cores.branco}│ 
│{config.cor} 5 - Roxo     {cores.branco}│
│{config.cor} 6 - Voltar   {cores.branco}│
├──────────────┘
│─> Cor atual : {cor_atual}""")
                    cor = input("│─> ")
                    if cor == "1":
                        with open("config.txt", "r+") as arquivo:
                            mudar_cor = arquivo.readlines()
                            mudar_cor[0] = "Cores={vermelho}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_cor)
                            arquivo.close()
                        print("Cor Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()
                    elif cor == "2":
                        with open("config.txt", "r+") as arquivo:
                            mudar_cor = arquivo.readlines()
                            mudar_cor[0] = "Cores={azul}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_cor)
                            arquivo.close()
                        print("Cor Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()      
                    elif cor == "3":
                        with open("config.txt", "r+") as arquivo:
                            mudar_cor = arquivo.readlines()
                            mudar_cor[0] = "Cores={verde}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_cor)
                            arquivo.close()
                        print("Cor Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()     
                    elif cor == "4":
                        with open("config.txt", "r+") as arquivo:
                            mudar_cor = arquivo.readlines()
                            mudar_cor[0] = "Cores={branco}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_cor)
                            arquivo.close()
                        print("Cor Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()          
                    elif cor == "5":
                        with open("config.txt", "r+") as arquivo:
                            mudar_cor = arquivo.readlines()
                            mudar_cor[0] = "Cores={roxo}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_cor)
                            arquivo.close()
                        print("Cor Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()      
                    else: 
                        menu()
                elif escolha == "2":
                    with open("config.txt", "r") as arquivo:
                        velocidade_atual = arquivo.read().split("Velocidade={")[1].split("}")[0]
                        arquivo.close()
                    print(f"""
├───────────────────────┐
│{config.cor} 1 - Muito-rapido (1s) {cores.branco}│
│{config.cor} 2 - Rapido (2s)       {cores.branco}│
│{config.cor} 3 - Moderado (3s)     {cores.branco}│
│{config.cor} 4 - Normal (4s)       {cores.branco}│ 
│{config.cor} 5 - Devagar (5s)      {cores.branco}│
│{config.cor} 6 - Voltar            {cores.branco}│
├───────────────────────┘
│─> Velocidade atual : {velocidade_atual}""")
                    velocidade = input("│─> ")
                    if velocidade == "1":
                        with open("config.txt", "r+") as arquivo:
                            mudar_velocidade = arquivo.readlines()
                            mudar_velocidade[1] = "Velocidade={muito-rapido}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_velocidade)
                            arquivo.close()
                        print("Velocidade Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()      
                    if velocidade == "2":
                        with open("config.txt", "r+") as arquivo:
                            mudar_velocidade = arquivo.readlines()
                            mudar_velocidade[1] = "Velocidade={rapido}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_velocidade)
                            arquivo.close()
                        print("Velocidade Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()
                    if velocidade == "3":
                        with open("config.txt", "r+") as arquivo:
                            mudar_velocidade = arquivo.readlines()
                            mudar_velocidade[1] = "Velocidade={moderado}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_velocidade)
                            arquivo.close()
                        print("Velocidade Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()
                    if velocidade == "4":
                        with open("config.txt", "r+") as arquivo:
                            mudar_velocidade = arquivo.readlines()
                            mudar_velocidade[1] = "Velocidade={normal}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_velocidade)
                            arquivo.close()
                        print("Velocidade Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()
                    if velocidade == "5":
                        with open("config.txt", "r+") as arquivo:
                            mudar_velocidade = arquivo.readlines()
                            mudar_velocidade[1] = "Velocidade={devagar}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_velocidade)
                            arquivo.close()
                        print("Velocidade Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()
                    else:
                        menu()
                elif escolha == "3":
                    with open("config.txt", "r") as arquivo:
                        dominio_atual = arquivo.read().split("Dominio={")[1].split("}")[0]
                        arquivo.close()
                    print(f"""├───────────────────────┐
│{config.cor} 1 - Adicionar Dominio {cores.branco}│
│{config.cor} 0 - Voltar            {cores.branco}│
├───────────────────────┘
│─> Dominio atual : {dominio_atual}""")
                    dominio = input("│─> ")
                    if dominio == "1":
                        print("│ Digite Seu Dominio")
                        dominio_salvar = input("│─> ")
                        dominio_salvar = "{"+dominio_salvar+"}"
                        with open("config.txt", "r+") as arquivo:
                            mudar_dominio = arquivo.readlines()
                            mudar_dominio[2] = f"Dominio={dominio_salvar}\n"
                            arquivo.close()
                        with open("config.txt", "w") as arquivo:
                            arquivo.writelines(mudar_dominio)
                            arquivo.close()
                        print("Dominio Alterada Com Sucesso!\nReinicie para atualizar!")
                        time.sleep(3)
                        menu()
                    else:
                        menu()
                else:
                    menu()
            except:
                menu()
        elif opcao == "6":
            try:
                print("│ Deseja Reiniciar? (S/N)")
                escolha = input("│─> ")
                if escolha == "S" or escolha == "s":
                    os.system(f"python wispproxyv3.py")
                    exit(0)
                else:
                    menu()
            except:
                menu()
        elif opcao == "7":
            try:
                print("│ Deseja Atualizar? (S/N)")
                escolha = input("│─> ")
                if escolha == "S" or escolha == "s":
                    link = requests.get("https://github.com/WispSSH/WispProxy-Prototipo-III/blob/main/wispproxyv3.py?raw=true")
                    with open("wispproxyv3.py", "wb+") as atualizar:
                        atualizar.write(link.content)
                    exit(0)
                else:
                    menu()
            except:
                menu()

        else:
            menu()
        

    def lista_scanner(host):
        try:
            headers = CaseInsensitiveDict()
            headers["Upgrade"] = "websocket"
            proxies = {
                "http":f"{host}:80"
                #"https":f"{host}:443"
            }
            verificar = requests.get(f'http://{config.dominio_config.replace(" ","")}', headers=headers, timeout=config.velocidade, proxies=proxies).status_code
            print(verificar)
            if verificar == 101:
                print(f'{cores.branco}│ {cores.verde}[+] {host}{cores.branco}')

                if os.path.isdir("resultado") == True:
                    pass
                else:
                    os.makedirs('resultado')

                valido_txt = open(f"./resultado/valido-{data}.txt", 'a')
                valido_txt.write(f'{host} - Encontramos! WispSSH\n')
                valido_txt.close()
            else:
                print(f'{cores.branco}│ {cores.vermelho}[-] {host}{cores.branco}')
        except Timeout:
            print(f'{cores.branco}│ {cores.vermelho}[-] {host}{cores.branco}')
        except:
            print(f'{cores.branco}│ {cores.vermelho}[-] {host}{cores.branco}')
    menu()

except KeyboardInterrupt:
    sair()
