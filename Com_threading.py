#Introduction to Multi-Threading - www.101computing.net/multi-threading-in-python

import threading
import time

class PrimeFinderThread(threading.Thread):
  def __init__(self, id,startPos):
    # Calling parent class constructor
    threading.Thread.__init__(self)
    self.id = id
    self.startPos = startPos

  #A Function to decide if a number is a prime number or not
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
    
  # Check all the numbers from startPos, 1 by 1, to find prime numbers
  def run(self):
    start = time.time()
    n = self.startPos
    while True and n < 100000000001000:
      if self.isPrime(n):
        print("Thread " + str(self.id) + ": " + str(n) + " is a prime number.")
      n+=1  
    end = time.time()
    print("o programa demorou: {:.2f} segundos para finalizar no "+ str(self.id) +"º thread ".format(end - start))


#Main Program Starts Here...
#Let's intialise three different threads.Each thread will be used to dientify prime numbers starting with a different starting position
#thread1 = PrimeFinderThread(1,100000000000000)
#thread2 = PrimeFinderThread(2,300000000000000)
#thread3 = PrimeFinderThread(3,500000000000000)

#Let's start our three threads to implement concurrent processing!
#thread1.start()
#thread2.start()
#thread3.start()


def main():
  thread1 = PrimeFinderThread(1,100000000000500)
  thread2 = PrimeFinderThread(2,100000000000700)
  thread3 = PrimeFinderThread(3,100000000000800)

  thread1.start()
  thread2.start()
  thread3.start()

main()