from post import post

expr1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
expr2 = ['1', '2', '/', '4', '*', '1', '4', '/', '*']
print(expr1, ' --> ', post(expr1))
print(expr2, ' --> ', post(expr2))