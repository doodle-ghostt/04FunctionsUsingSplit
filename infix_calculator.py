n1, operator, n2 = input("Give me and equation, user! ").split(" ")
n1 = int(n1)
n2 = int(n2)
if operator == "*":
  print(n1*n2)
elif operator == "/":
  print(n1/n2)
elif operator == "+":
  print(n1+n2)
else:
  print(n1-n2)