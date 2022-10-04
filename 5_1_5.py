class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self,head = None):
        if head is None:
            self.head = self.tail =None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size =1
            while t.next is not None:
                t = t.next
                self.size +=1
                self.tail = t 
    def __str__(self):
        s = 'link list : '
        p = self.head
        while p is not None:
            if p.next is None:
                 s+= str(p.data)+ ""
                 break
            s+= str(p.data)+ "->"
            p = p.next
        return s
    def _len_(self):
        return self.size
    def isEmpty(self):
        return self.size == 0
    def append(self,data):
        p = Node(data)
        if self.head is None:
            self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
        self.size +=1
    def nodeAt(self,index):
        p =self.head
        if index == 0:
            return p
        if index == 1:
            return p
        for i in range(index-1):
            p = p.next
        return p
    def insert(self,index,data):
        #print(ll.size)
        #print(self.head.data)
        if index>=0 and data <= ll.size+1 :
            if self.head == None and index >0:
                print("Data cannot be added")
                return
            print("index = "+str(index)+" and data = "+str(data))
        else:
            print("Data cannot be added")
            return
        p = Node(data)
        q = self.nodeAt(index)
        if q == self.head and index ==0:
            if self.isEmpty():
                self.append(data)
                return
            
            x = Node(0)
            x = self.head
            x.next = self.head.next
            self.head = p
            self.head.next = x
        else:
            p.next = q.next
            q.next = p
            self.size +=1


lst = list(map(str, input("Enter Input : ").split(',')))

lst[0] = list(lst[0].split(' '))

for i in range(len(lst)):
    if i >0:
        lst[i] = list(lst[i].split(':'))

ll = LinkedList()
if lst[0] != [""]:
    for i in lst[0]:
        ll.append(i)
        #print(ll.size)
if(ll.size == 0):
    print("List is empty")
else:
    print(ll.__str__())
for j in range(len(lst)):
    if j >0:
        ll.insert(int(lst[j][0]),int(lst[j][1]))
        if(ll.size == 0):
            print("List is empty")
        else:
            print(ll.__str__())
