import ArrayListFn as q

print("최초 ", q.array[0:q.size])

q.insert(0, 10)
q.insert(0, 20)
q.insert(1, 30)
q.insert(3, 40)
q.insert(2, 50)
print("삽입x5 ", q.array[0:q.size])
q.delete(2)
print("삭제(2)", q.array[0:q.size])
q.delete(3)
print("삭제(3)", q.array[0:q.size])
q.delete(0)
print("삭제(0)", q.array[0:q.size])

