#Introduction to Multi-Threading - www.101computing.net/multi-threading-in-python

from concurrent.futures import thread
import threading
import time

primos = []

n = 100000000

#Funcao para verificar se um numero é primo ou nao
def isPrime(n):
  if (n <= 1) :
    return False
  elif (n <= 3) :
    return True
  elif (n % 2 == 0 or n % 3 == 0) :
    return False
  else:
    i = 5
    while(i * i <= n) :
      if (n % i == 0 or n % (i + 2) == 0) :
        return False
      i = i + 6
    return True
  
# checa se o numero é primo e imprime na tela caso seja primo


def Soma_dos_numeros_ate_n():
  for i in range(1,100000):
    soma = 0
    soma = soma + i
    print("A soma dos numeros ate n é: " + str(soma))

def Subtração_dos_primos():
  for i in range(1, 100000):
    sub =0
    sub = sub - i
    print("A subtração dos numeros ate n é: " + str(sub))

#def Divisão_dos_primos():
#  for i in range(1, 10000):
#    div=0
#    div = div / i
#    print("A divisão dos numeros ate n é: " + str(div))
#
#def Multiplicação_dos_primos():
#  for i in range(1, 10000):
#    mult = 0
#    mult = mult * i
#    print("A multiplicação dos numeros ate n é: " + str(mult))

def IMPRIME_PRIMOS():
  n = 1
  while True and n < 60000:
    if isPrime(n):
      primos.append(n)
      print(str(n) + " is a prime number.")
    n+=1

    

thread1 = threading.Thread(target=IMPRIME_PRIMOS)
thread2 = threading.Thread(target=Soma_dos_numeros_ate_n)
thread3 = threading.Thread(target=Subtração_dos_primos)


#função principal do programa
def main():
  start = time.time()
  thread1.start()
  thread2.start()
  thread3.start()
  end = time.time()
  print("o programa demorou: {:.2f} segundos para finalizar".format(end - start))
  

main()