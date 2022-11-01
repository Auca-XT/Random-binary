def calbol():
  import random

  calculus = ['1', '0']

  bol1 = ""

  for x in range(36):
    bol1 = bol1 + random.choices(calculus)[0]

  print("\033[32m", bol1, "\033[0m")
  
calbol()

i = 1
while i < 120000:
  calbol()
  i += 1