
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + ""
        while cur.previous != None:
            s += str(cur.previous.value) + ""
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        #Code Here
        if self.head is None:
            p = Node(item)
            self.head = p
            self.tail = self.head
            self.head.next = self.tail
            self.tail.previous = self.head
            self.tail.next = None
            self.head.previous = None

        else:
            p = Node(item)   #สร้างp
            dummy = Node(None) #สร้าง d
            p.previous = self.tail #ให้ก่อน p เป็นค่า tail
            p.next = None   #ให้หน้า p เป็น None
            dummy = self.tail #เก็บค่า tail ไว้
            dummy.previous = self.tail.previous
            self.tail = p
            self.tail.next = p.next #เปลี่ยน p เป็นค่า tail
            self.tail.previous = dummy

            dummy.next = self.tail #โยง dummy หา tail

    def addHead(self, item):
        #Code Here
        if self.head is None:
            p = Node(item)
            self.head = p
            self.tail = self.head
            self.head.next = self.tail
            self.tail.previous = self.head
            self.tail.next = None
            self.head.previous = None
        else:
            p = Node(item)
            dummy = Node(None)
            p.next = self.head.next
            p.previous = None
            dummy = self.head
            dummy.next = self.head.next
            self.head =p
            self.head.previous = p.previous
            self.head.next = dummy
            dummy.previous = self.head

    def insert(self, pos, item):
        #Code Here
        p = Node(item)
        if self.head is None:
            p = Node(item)
            self.head = p
            self.tail = self.head
            self.head.next = self.tail
            self.tail.previous = self.head
            self.tail.next = None
            self.head.previous = None
        else:
            if pos >= self.size():
                self.append(item)
            elif pos < 0:
                if pos <= self.size()*-1:
                    self.addHead(item)
                else:
                    x = self.tail
                    for i in range((pos+1)*-1):
                        x = x.previous
                    #print(x.value)
                    p.next = x
                    p.previous = x.previous
                    m = x.previous
                    m.next =p
                    x.previous = p
            else:
                x = self.head
                for i in range(pos):
                    x = x.next
                p.next = x
                p.previous = x.previous
                m = x.previous
                m.next =p
                x.previous = p


            

    def search(self, item):
        #Code Here
        x = self.head
        while x.value != item:
            x = x.next
            if x == None:
                return "Not Found"
        return "Found"
        
            



    def index(self, item):
        #Code Here
        x = self.head
        i = 0
        while x.value != item:
            x = x.next
            i+=1
            if x == None:
                return -1
        return i


    def size(self):
        #Code Here
        i =0
        x =self.head
        #print(self.head)
        while x != None:
            i+=1
            x = x.next
        return i

    def pop(self, pos):
        #Code Here
        #print(self.size())
        if self.head is None:
            return "Out of Range"
        else:
            if int(pos) >= self.size():
                return "Out of Range"
            elif pos < 0:
                if pos <= self.size()*-1:
                    return "Out of Range"
                else:
                    x = self.tail
                    for i in range((pos+1)*-1):
                        x = x.previous
                    a = x.previous
                    b = x.next
                    a.next = b
                    b.previous = a
                    return "Success"
            else:
                x = self.head
                for i in range(pos):
                    x = x.next
                y = x.next
                if pos ==0:
                    if self.size()==1:
                        self.head.next = self.tail
                        self.tail.next = None
                        self.head.previous = None
                        self.tail.previous = self.head
                        self.head = None
                        self.tail = None
                    elif self.size() ==2:
                        self.head =self.tail
                        self.head.next = self.tail
                        self.tail.previous = self.head
                        self.head.previous = None
                        self.tail.next = None
                    else:
                        k = self.head.next
                        l = k.next
                        self.head = k
                        self.head.next = k.next
                        self.head.previous = None
                        l.previous = self.head
                elif y ==None:
                    k =  self.tail.previous
                    self.tail = self.tail.previous
                    self.tail.previous = k.previous
                    self.tail.next = None
                else:
                    a = x.previous
                    b = x.next
                    a.next = b
                    b.previous = a
            return "Success"




def VIM(lst):

    V = LinkedList()
    pos = 0
    for i in range(len(lst)):
        #print(V)
        #print(V)
        #print(V.size())
        if lst[i][0] == 'I':
            if pos ==0:
                V.addHead(lst[i][1])
            elif pos == V.size():
                V.append(lst[i][1])
            else:
                V.insert(pos,lst[i][1]) 
            pos+=1 
        elif lst[i][0] == 'L':
            if pos > 0:
                pos -= 1
                #print(pos)
        elif lst[i][0] == 'R':
            if pos < V.size():
                pos +=1
        elif lst[i][0] == 'B':
            if pos> 0:
                V.pop(pos-1)
                pos -=1
        elif lst[i][0] == 'D':
            if pos < V.size():
                V.pop(pos)
    #print(pos)
    if(pos ==0):
        V.addHead("|")
    elif(pos==V.size()):
        V.append("|")
    else:
        V.insert(pos,'|')
    print(V)



lst = input('Enter Input : ').split(',')

for i in range(len(lst)):
    lst[i] = list(lst[i].split(" ")) 

#print(lst)

VIM(lst)