import random
class Node():
    def __init__(self):
        self.data=None
        self.link=None
def printNode(start):
    current = start
    if current ==None:
        return
    print(current.data, end=' ');
    while current.link !=None:
        current = current.link
        print(current.data,end=' ')
    print()
def Lotto1(num):
    global memory, head,current,pre
    node = Node();
    node.data=num
    memory.append(node)
    if head ==None:
        head = node
        return
    if head.data>num:
        node.link = head
        head=node
        return
    current= head
    while current.link != None:
        pre = current
        current = current.link
        if current.data>num:
            pre.link = node
            node.link = current
            return
    current.link = node
def Findnum(num):
    global memory, head, current,pre
    if head ==None:
        return False
    current =head
    if current.data ==num:
        return True
    while current.link != None:
        current = current.link
        if current.data == num:
            return True
        return False
memory =[]
head, current, pre =None, None,None

if __name__ == "__main__":
    cnt = 0
    while True:
        lotto =random.randint(1,45)
        if Findnum(lotto):
            continue
        cnt +=1
        Lotto1(lotto)
        if cnt>=6:
            break

    printNode(head)
            
