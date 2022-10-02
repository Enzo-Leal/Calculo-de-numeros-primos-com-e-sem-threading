import time

primos = []

#A Function to decide if a number is a prime number or not
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

def Soma_dos_primos():
  for n in primos:
    soma = 0
    soma += n
    print("A soma dos primos é: " + str(soma))

  

def main(): 
  start = time.time()
  n = 1
  while True and n < 60000:
    if isPrime(n):
      primos.append(n)
      print(str(n) + " is a prime number.")
    n+=1

  Soma_dos_primos()
  end = time.time()
  print("o programa demorou: {:.2f} segundos para finalizar".format(end - start))


main()