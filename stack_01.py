def isfull():
    global size, queue,front,rear
    if (rear == size-1):
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
    rear += 1
    queue[rear] = data

def dequeue():
    global size, queue,front,rear
    if(isempty()):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None

    for i in range(front+1, rear+1):
        queue[i-1] = queue[i]
        queue[i]=None
    front =-1
    rear-=1

    return data
def peek():
    global size, queue,front,rear
    if(isempty()):
        print("큐가 비었습니다.")
        return None
    return queue[fornt+1]


size = 5
queue = [None for _ in range(size)]
front = rear =-1

if __name__=="__main__":
    enqueue('정국')
    enqueue('뷔')
    enqueue('지민')
    enqueue('진')
    enqueue('슈가')
    print("대기 줄 상태 : ", queue)

    for _ in range(rear+1):
        print(dequeue(), '님 식당에 들어감')
        print("대기 줄 상태 : ", queue)

    print("식당 영업 종료!")
    
