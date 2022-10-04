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
        x = self.head
        #print(x.value,"value")
        if self.head is None:
            p = Node(item)
            self.head = p
            self.tail = self.head
            self.head.next = self.tail
            self.tail.previous = self.head
            self.tail.next = None
            self.head.previous = None
        else:
            dummy = self.head
            dummy.next = self.head.next
            self.head =Node(item)
            self.head.previous = None
            self.head.next = dummy
            dummy.previous =self.head


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
                if pos ==0:
                    self.addHead(item)
                    return
                    """x.next =self.head.next
                    y =self.head = Node(item) 
                    z=self.head.next = x
                    x.previous = self.head"""
                    
                    
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
    def addAndsort(self,item):
        p = Node(item)
        if self.head == None:
            self.append(item)
            return
        else:
            p =self.head
            i =0
            while p != None:
                if p.value <= item :
                    p = p.next
                    i +=1
                else:
                    self.insert(i, item)
                    return
            self.append(item)


def RadixSort(lst):
    round =1
    mround =1
    n0 = LinkedList()
    n1 = LinkedList()
    n2 = LinkedList()
    n3 = LinkedList()
    n4 = LinkedList()
    n5 = LinkedList()
    n6 = LinkedList()
    n7 = LinkedList()
    n8 = LinkedList()
    n9 = LinkedList()
    n0c = LinkedList()
    n1c = LinkedList()
    n2c = LinkedList()
    n3c = LinkedList()
    n4c = LinkedList()
    n5c = LinkedList()
    n6c = LinkedList()
    n7c = LinkedList()
    n8c = LinkedList()
    n9c = LinkedList()
    n09c = [n0c,n1c,n2c,n3c,n4c,n5c,n6c,n7c,n8c,n9c]
    n09 = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]
    x =max(lst)
    y =min(lst)
    Max=0
    if x>y*-1 :
        Max =x
    else:
        Max = y*-1
    while Max !=0:
        Max = int(Max/10)
        mround+=1
    print("------------------------------------------------------------")
    print("Round :",round)
    for i in lst:
        if i <0:
            z = (i*-1)%10
        else:
            z = i%10
        if z == 0:
            n0c.append(i)
        elif z == 1:
            n1c.append(i)
        elif z == 2:
            n2c.append(i)
        elif z == 3:
            n3c.append(i)
        elif z == 4:
            n4c.append(i)
        elif z == 5:
            n5c.append(i)
        elif z == 6:
            n6c.append(i)
        elif z == 7:
            n7c.append(i)
        elif z == 8:
            n8c.append(i)
        elif z == 9:
            n9c.append(i)
    for i in range(len(n09c)):
        p = n09c[i].head
        while p != None:
            n09[i].addAndsort(p.value)
            n09c[i].pop(0)
            p =p.next
    for i in range(len(n09)):
        print(i,": ",end="")
        if not n09[i].isEmpty():
            print(n09[i])
        else:
            print()
        if n09[0].size()==len(lst):
            mround = round
    while round != mround:
        #print(round)
        #print(mround)
        temp =[]
        round+=1
        print("------------------------------------------------------------")
        print("Round :",round)
        for i in n09:
            p =i.head
            while p != None:
                if p.value <0:
                    z = (-1*p.value %10**round)//10**(round-1)
                else:
                    z = (p.value %10**round)//10**(round-1)
                #print("+++++++++++++++++++++++++++",p.value)
                if z == 0:
                    n0c.append(p.value)
                    i.pop(0)
                elif z== 1:
                    n1c.append(p.value)
                    i.pop(0)
                elif z== 2:
                    n2c.append(p.value)
                    i.pop(0)
                elif z == 3:
                    n3c.append(p.value)
                    i.pop(0)
                elif z == 4:
                    n4c.append(p.value)
                    i.pop(0)
                elif z == 5:
                    n5c.append(p.value)
                    i.pop(0)
                elif z == 6:
                    n6c.append(p.value)
                    i.pop(0)
                elif z == 7:
                    n7c.append(p.value)
                    i.pop(0)
                elif z == 8:
                    n8c.append(p.value)
                    i.pop(0)
                elif z == 9:
                    n9c.append(p.value)
                    i.pop(0)
                p =p.next
        for i in range(len(n09c)):
            p = n09c[i].head
            while p != None:

                n09[i].addAndsort(p.value)
                n09c[i].pop(0)
                p =p.next
        for i in range(len(n09)):
            print(i,": ",end="")
            if not n09[i].isEmpty():
                print(n09[i])
            else:
                print()
        if n09[0].size()==len(lst):
            break
    """for i in n09:
        print(i)
    print("NW")
    for i in n09c:
        print(i) """
    l =""
    p = n0.head
    while p != None:
        l += str(p.value)
        if p.next !=None:
            l+= " -> "
        p = p.next
    print("------------------------------------------------------------")
    print(round-1,"Time(s)")
    print("Before Radix Sort :",s)
    print("After  Radix Sort :",l)
lst = list(map(int, input("Enter Input : ").split(' ')))
s =""
for i in range(len(lst)):
    s+= str(lst[i])
    if i != len(lst)-1:
        s+= " -> "
RadixSort(lst)
