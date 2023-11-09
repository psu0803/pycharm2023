from stack import stack
L = stack(50)

print("최초 ", L)

L.push(10)
L.push(20)
L.push(30)
L.push(40)
L.push(50)
print("삽입x5 ", L)
L.pop()
print("삭제", L)
L.pop()
print("삭제", L)
L.pop()
print("삭제", L)
