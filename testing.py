import math


def is_prime(p):
  if p <= 1:
    return False
  elif p <= 3:
    return True
  elif p % 2 == 0 or p % 3 == 0:
    return False
  i = 5
  while i <= int(math.sqrt(p)):
    if p % i == 0 or p % (i + 2) == 0:
      return False
    i += 6
  return True


def devider(var):
  field = []
  if is_prime(var):
    print(var)
    return

  else:
    while var > 1:
      for i in range(2, var + 1):
        if is_prime(i) and var % i == 0:
          field.append(i)
          var = int(var / i)
          print("check", i, var)
          break

  unique = list(set(field))
  unique.sort()
  string = ""
  for x in range(len(unique)):
    string += f"{unique[x]}"
    if field.count(unique[x]) != 1:
      string += f"^{field.count(unique[x])}"

    if x < len(unique) - 1:
      string += "*"

  print(string)


devider(126)