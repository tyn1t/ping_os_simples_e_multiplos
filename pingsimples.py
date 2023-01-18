import os  #Importa o modulo ou biblioteca os (Intergra os programas e recusoa do S.O)

print('#' * 60) ##Imprime #60 vezes

ip_ou_host = input("Digite o Ip ou host a ser verificado: ")
#criamos uma variavel que vai receber do usuario um ip

print("_" * 60) ##Imprime #60 vezes

os.system('ping -n 6 {}'.format(ip_ou_host)) ##chamando system da biblioteca os - comanda ping
## -n -num de pacotes que serão 6 {}

##Imprime #60 vezes
