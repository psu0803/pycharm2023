from CircularQueue import CircularQueue

q = CircularQueue(8)
q.enqueue('A')
print("삽입 -->", q, q.front, q.rear)
q.enqueue('B')
print("삽입 -->", q, q.front, q.rear)
q.enqueue('C')
print("삽입 -->", q, q.front, q.rear)
q.enqueue('D')
print("삽입 -->", q, q.front, q.rear)
q.enqueue('E')
print("삽입 -->", q, q.front, q.rear)
q.enqueue('F')
print("삽입 -->", q, q.front, q.rear)
