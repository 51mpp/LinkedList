
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
        cur, s = self.head, str(self.head.value) + ""
        while cur.next != None:
            s += str(cur.next.value) + ""
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
                else:
                    a = x.previous
                    b = x.next
                    a.next = b
                    b.previous = a
            return "Success"



def color_crush(lst):
    L = LinkedList()
    for i in lst:
        L.append(i)
    x = L.head
    crush = True
    crushcount = 0
    i =0
    while crush:
        #print(L.size())
        if L.size() - i>2:
            y =x.next
            z =y.next
        else:
            break
        #print(str(x.value)+str(y.value)+str(z.value))
        #print(L)
        if x.value==y.value and y.value ==z.value :
            #print(i)
            L.pop(i)
            
            L.pop(i)
            L.pop(i)
            
            crushcount +=1
            
            i =0
            x = L.head
        elif i == L.size():
            break
        else:
            x = x.next
            i+=1
    print(L.size())
    print(L.reverse())
    if crushcount >1:
        print("Combo : {0} ! ! !".format(crushcount))
            
            

lst = input('Enter Input : ').split(' ')

color_crush(lst)