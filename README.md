# WispProxy-Prototipo-II

```
_ _ _ _ ____ ___    ___  ____ ____ _  _ _   _
| | | | [__  |__]   |__] |__/ |  |  \/   \_/    
|_|_| | ___] |      |    |  \ |__| _/\_   |
```

- Primeiro projeto experimental feito para checar os status dos proxys.
- Versão liberada gratuitamente.
- Grupo com a chave de execução.
- https://t.me/wispssh_central

## Instalação

Aplicativo Necessario (Android)

[Termux](https://play.google.com/store/apps/details?id=com.termux&hl=pt_BR&gl=US)

Termux (Instalador)

```bash
pkg upgrade && pkg update && pkg install python && pkg install git && pip install requests && pip install datetime && pip install ipcalc && pip install six && cd $home && mkdir WispProxy && git clone https://github.com/WispSSH/WispProxy-Prototipo-III.git WispProxy && cd WispProxy && rm README.md && python wispproxyv3.py
```

Atualizar Script (Já instalado)

```bash
cd $home && git clone https://github.com/WispSSH/WispProxy-Prototipo-III.git atualizar && mv atualizar/wispproxyv3.py WispProxy/wispproxyv3.py && rm -r -f atualizar && cd WispProxy && python wispproxyv3.py
```

Dependencias

```bash
pip install requests
pip install datetime
pip install ipcalc
pip install six
```

Inicie o script com

```bash
python wispproxyv3.py
```

## Demonstrações

Menu Estilo

![image](https://user-images.githubusercontent.com/100727796/182263451-a798a401-cc6b-4ba1-ba15-e1009aea2caf.png)

## Funções

- Ip Range
- List Checker
- Proxy Finder


## Como utilizar

- Ip Scanner (Necessita de dados sem internet)

Adicione um ip que na ultima casa esteja com .x e ele irá verificar todas as ocorrencias de 0 a 254.

- Lista Scanner (Necessita de dados sem internet)

Adicione uma lista de ip/hostname no arquivo lista.txt que o aplicativo irá verificar um por um.

- Proxy Finder

Procura alguma proxy cloudflare valida.

## Extra

- Script desenvolvido com a intenção de auxiliar na busca de proxys.
- Lembrando que não estou ganhando nada por ter feito e liberado o script.




