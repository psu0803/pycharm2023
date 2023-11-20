from LinkedList import LinkedList

s = LinkedList()
print("최초 ", s)

s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(3, 40)
s.insert(1, 50)
print("삽입x5 ", s)
s.delete(2)
print("삭제(2)", s)
s.delete(3)
print("삭제(3)", s)
s.delete(0)
print("삭제(0)", s)
