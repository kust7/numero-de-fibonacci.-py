
def fibonacci(n):
  fib_sequence = [0, 1]

  for i in range(2, n):
      next_term = fib_sequence[i-1] + fib_sequence[i-2]
      fib_sequence.append(next_term)

  return fib_sequence
def main():  
  n = int(input("Digite o número de termos desejado: "))
  result = fibonacci(n)
  print(f"Os {n} primeiros termos da sequência de Fibonacci são: {result}")
return 0

if __name__ == "__main__":
  main()
