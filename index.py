# importando bibliotecas que vou usar
import os
import shutil

# Definindo um vetor com o nome das DLL's que eu quero instalar
nomeDll = [r"dll-nome-1.dll",r"dll-nome-2.dll",r"dll-nome-3.dll"]

# Definindo um vetor para gravar quais DLL's já existiam na pasta
dllExistente = []

# Definindo um vetor para gravar quais DLL's não existiam na pasta
dllNaoExistente = []

# Definindo variaveis
# a variavel caminhoOrigem se refere a pasta DLL que será consumida para copiar e colar as dll's
caminhoOrigem = r'DLL'
caminhoDestinoSys32 = r'C:\Windows\System32'
caminhoDestinoSyswow64 = r'C:\Windows\SysWOW64'
indiceExistente = 0
indiceNaoExistente = 0


# Se o caminho na pasta sysWOW64 existir, então é 64 bits e vai registrar na pasta sysWOW64
if os.path.exists(caminhoDestinoSyswow64):
    for nome in nomeDll:
        # Verificando se a DLL já existia
        if os.path.isfile(caminhoDestinoSyswow64+'/'+nome):
            print("")
            print("A Dll ",nome, "Já existia na pasta sysWOW64")
            # Se existir, removendo DLL Existente
            os.remove(caminhoDestinoSyswow64+'/'+nome)
            print("A DLL ",nome," foi removida" )
            # Salvando o nome da dll em um vetor para apresentar as DLL's que foram sobrescritas
            dllExistente.append(nome)
            # Movendo dll para pasta sysWOW64
            shutil.copy2(caminhoOrigem+"/"+nome , caminhoDestinoSyswow64)
            print("A DLL ",nome,"foi sobrescrita com sucesso!")
            print("")
        else:
            # Movendo dll para pasta sysWOW64
            shutil.copy2(caminhoOrigem+"/"+nome , caminhoDestinoSyswow64)
            print("A DLL ",nome,"foi colada com sucesso!")
            # Salvando o nome em um vetor para apresentar as DLL's que foram coladas
            dllNaoExistente.append(nome)
# Se não, é 32 bits e vai ser registrado na pasta system32
else: 
    for nome in nomeDll:
        # Verificando se a DLL já existia
        if os.path.isfile(caminhoDestinoSys32+'/'+nome):
            print("")
            print("A Dll ",nome, "Já existia na pasta System 32")
            # Removendo DLL Existente
            os.remove(caminhoDestinoSys32+'/'+nome)
            print("A DLL ",nome," foi removida" )
            # Salvando o nome em um vetor para saber as DLL's que foram sobrescritas
            dllExistente.append(nome)
            # Movendo dll para pasta system32
            shutil.copy2(caminhoOrigem+"/"+nome , caminhoDestinoSys32)
            print("A DLL ",nome,"foi sobrescrita com sucesso!")
            print("")
        else:
            # Movendo dll para pasta system32
            shutil.copy2(caminhoOrigem+"/"+nome , caminhoDestinoSys32)
            print("A DLL ",nome,"foi colada com sucesso!")
            # Salvando o nome para saber as DLL's que foram coladas
            dllNaoExistente.append(nome)

# Registrando as DLL's para x64 ou x86
if os.path.exists(caminhoDestinoSyswow64):
    os.system('regsvr32 C:\Windows\SysWOW64\dll-nome-1.dll')
    os.system('regsvr32 C:\Windows\SysWOW64\dll-nome-2.dll')
    os.system('regsvr32 C:\Windows\SysWOW64\dll-nome-3.dll')
    sistema64 = 's'
else:
    os.system('regsvr32 C:\Windows\system32\dll-nome-1.dll')
    os.system('regsvr32 C:\Windows\system32\dll-nome-2.dll')
    os.system('regsvr32 C:\Windows\system32\dll-nome-3.dll')
    sistema64 = 'n'


# Mensagem final
print("")
print("=================== DLL's que ja existiam ===============")
print("")
print("DLL's que foram substituidas: ")
print("Foram substituidas",len(dllExistente),"DLL's")
print("")
#laço de repeticao para imprimir as dll's existentes
for i in dllExistente:      
    print(dllExistente[indiceExistente])
    indiceExistente += 1  
print("")
print("=================== DLL's que não existiam ===============")
print(" ")
print("DLL's que estavam faltando:")
print("Foram copiadas", len(dllNaoExistente),"DLL's")
print("")
#laço de repeticao para imprimir dll's que nao existiam
for i in dllNaoExistente:
    print(dllNaoExistente[indiceNaoExistente])
    indiceNaoExistente += 1

if sistema64 == 's':
    print("O programa finalizou a execução no sistema 64 bits")
else: 
    print("O programa finalizou a execução no sistema 32 bits")
print("")
print(r"Aperte [Enter] para Encerrar")
The_end = input()

