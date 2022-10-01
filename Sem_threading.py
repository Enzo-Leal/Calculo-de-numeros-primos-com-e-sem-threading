import time

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

def main(): 
  start = time.time()
  n = 100000000000000
  while True and n < 600000000000000:
    if isPrime(n):
      print(str(n) + " is a prime number.")
    n+=1
  end = time.time()
  print("o programa demorou: {:.2f} segundos para finalizar".format(end - start))


main()