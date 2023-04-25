# registrador-dll
Programa criado em Python, usando as bibliotecas OS e Shutil, afim de instalar e registrar DLL's no Windows

Passos do programa: 

1- Primeiro ele identifica de o Windows é x64 ou x86, para saber onde colar as DLL'S

  *Sistemas baseados em x64 possuem as DLL'S na pasta SysWOW64, e sistemas baseados em x86 possuem as DLL'S na pasta System32, por isso é importante identificar qual em   qual arquitetura o sistema é baseado*

2- Depois ele verifica se a DLL já existe na pasta 

  *Se não, ele cola as DLL's (primeira imagem)*

  *Se sim, ele substitui as DLL's (Segunda imagem)*

3- e por fim, usando a biblioteca OS ele vai tentar registrar essas DLLS via comando no CMD (terceira imagem, uma mensagem por vez)

    *nesse caso deu erro porque as DLL'S usadas são fictícias*

Lembrando que o programa consome os arquivos na pasta DLL que fica na raiz do código e precisa ser executado como ADM.

Programa pensado para agilizar tarefas repetitivas, por exemplo no caso da instalação de um programa que necessite de DLL's especificas.
