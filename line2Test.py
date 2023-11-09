from post import post
from Infix2Postfix import Infix2Postfix

infix1 = ['b', '*', 'b', '-', '4', '*', 'a', '*', 'c']
infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)
#result1 = post(postfix1)
result2 = post(postfix2)
print('중위표기:', infix1)
print('후위표기:', postfix1)
#print('계산결과:', result1, end='\n\n')
print('중위표기:', infix2)
print('후위표기:', postfix2)
print('계산결과:', result2)

