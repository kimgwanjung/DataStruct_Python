class Node():
    def __init__(self):
        self.plink = None
        self.data = None
        self.nlink =None

def print1(start):
    current = start
    if current.nlink == None:
        return
    print("정방향 --->", end = ' ')
    print(current.data, end= ' ')
    while current.nlink != None:
        current = current.nlink
        print(current.data, end = ' ')
    print()
    print("역방향 --->", end = ' ')
    print(current.data, end = ' ')
    while current.plink != None:
        current = current.plink
        print(current.data, end= ' ')
mem = []
head, current, pre = None, None, None
array1 =["다현", "정연","쯔위","사나","지효"]

if __name__ == "__main__":
    node  = Node()
    node.data = array1[0]
    head=node
    mem.append(node)

    for data in array1[1:]:
        pre =node
        node=Node()
        node.data=data
        pre.nlink = node
        node.plink = pre
        mem.append(node)

    print1(head)
