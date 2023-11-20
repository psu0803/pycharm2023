class CircularQueue :
    def __init__( self, capacity ):  #큐생성
        self.capacity = capacity     #용량
        self.array = [None]* capacity #용량 확인
        self.front = 0                #같은 값으로
        self.rear = 0                 #초기화

    def isEmpty( self ) :             #empty셀프값으로
        return self.front == self.rear #front = rear 공백

    def isFull( self ) :              #full셀프값
        return self.front == (self.rear+1)%self.capacity  #front가 rear 다음이면 포화

    def enqueue( self, item ):           #인큐 셀프값
        if not self.isFull() :          #풀 아닐때 가능
            self.rear = (self.rear + 1)%self.capacity     #rear 원형이므로 시계방향으로 회전
            self.array[self.rear] = item                  #그위치에 요소 저장
        else: pass

    def dequeue( self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else: pass

    def peek( self ):                                     #픽 셀프값
        if not self.isEmpty():                            #엠티상태에 작동안함
            return self.array[(self.front + 1) % self.capacity] #어레이 때 프론트+1 값 반환
        else: pass

    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        else :
            return str(self.array[self.front+1:self.capacity] + \
                       self.array[0:self.rear+1])