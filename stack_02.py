def isfull():
    global size, queue,front,rear
    if ((rear+1)%size == front):
        return True
    else:
        return False
def isempty():
    global size, queue,front,rear
    if (front ==rear):
        return True
    else:
        return False

def enqueue(data):
    global size, queue,front,rear
    if(isfull()):
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear+1) % size
    queue[rear] = data

def dequeue():
    global size, queue,front,rear
    if(isempty()):
        print("큐가 비었습니다.")
        return None
    front = (front+1)%size
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global size, queue,front,rear
    if(isempty()):
        print("큐가 비었습니다.")
        return None
    return queue[(fornt+1)%size]

def ctime():
    global size, queue,front,rear
    timesum = 0
    for i in range((front+1)%size,(rear+1)%size):
        timesum +=queue[i][1]
    return timesum
size = 6
queue = [None for _ in range(size)]
front = rear = 0

if __name__=="__main__":
    waitcall =[('사용',9),('고장',3),('환불',4),('환불',4),('고장',3)]
    for call in waitcall:
        print("귀하의 대기 예상시간은", ctime(), "분입니다.")
        print("현재 대기 콜--> : ", queue)
        enqueue(call)
        print()


    print("최종 대기 콜-->",queue)
    print("프로그램 종료!")
    
