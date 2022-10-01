#Introduction to Multi-Threading - www.101computing.net/multi-threading-in-python

import threading
import time

class PrimeFinderThread(threading.Thread):
  def __init__(self, id,startPos):
    # Calling parent class constructor
    threading.Thread.__init__(self)
    self.id = id
    self.startPos = startPos

  #Funcao para verificar se um numero é primo ou nao
  def isPrime(self,n):
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
  def run(self):
    start = time.time()
    n = self.startPos
    while True and n < 100000000000000:
      if self.isPrime(n):
        print("Thread " + str(self.id) + ": " + str(n) + " is a prime number.")
      n+=1  
    end = time.time()
    print(("o programa demorou: {:.2f} segundos para finalizar no "+ str(self.id) +"º thread ").format(end - start))

#função principal do programa
def main():
  #define o ID do thread e o número inicial para começar a procurar
  thread1 = PrimeFinderThread(1,100000000000000)
  thread2 = PrimeFinderThread(2,200000000000000)
  thread3 = PrimeFinderThread(3,300000000000000)
  thread4 = PrimeFinderThread(4,400000000000000)
  thread5 = PrimeFinderThread(5,500000000000000)
  thread6 = PrimeFinderThread(6,600000000000000)

  
  #inicia o thread
  thread1.start()
  thread2.start()
  thread3.start()
  thread4.start()
  thread5.start()
  thread6.start()

main()