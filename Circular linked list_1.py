import random
import math

class Node():
    def __init__(self):
        self.data = None
        self.link = None
def print1(start):
    current = start
    if current == None:
        return
    while current.link != head:
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], ' 편의점 거리 ', math.sqrt(x*x+y*y))
    print()

def List1(store):
    global mem, head, current, pre

    node = Node()
    node.data = store
    mem.append(node)
    if head == None:
        head =node
        node.link = head
        return
    nodeX, nodeY = node.data[1:]
    nodeD = math.sqrt(nodeX*nodeX + nodeY*nodeY)
    headX, headY = head.data[1:]
    headD = math.sqrt(headX*headX + headY*headY)
    if headD > nodeD:
        node.link =head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head= node
        return
    current = head
    while current.link != head:
        pre = current
        current = current.link
        currX, currY = current.data[1:]
        currD = math.sqrt(currX * currX +currY*currY)
        if currD > nodeD :
            pre.link= node
            node.link = current
            return
    current.link = node
    node.link = head




mem = []
head, current, pre = None,None, None
if __name__ =="__main__":
    Array1 = []
    name1 = 'A'

    for _ in range(10):
        S=(name1, random.randint(1,100), random.randint(1,100))
        Array1.append(S)
        name1 = chr(ord(name1)+1)

    for S in Array1:
        List1(S)
    print1(head)
