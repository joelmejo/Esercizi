# Given the head of a singly linked list, return true if it is a palindrome. Model the Node and Linked List
#  concepts using classes. 

class Node:
    pos: int= 0
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.pos = Node.pos
        Node.pos += 1 
        
class LinkedList:
    def __init__(self) -> None:
        self.head: Node= None

    def append(self, n: int) -> None:
        if self.head is None:
            self.head = Node(n)
        else:
            head: Node= self.head
            while head.next is not None:
                head = head.next
            head.next = Node(n)
    
    def get_node(self, n: int) -> Node:
        head: Node= self.head
        if head.data == n:
            return head
        
        while head.next is not None:
            head = head.next
            if head.data == n:
                return head
        
def is_palindrome(head: Node) -> list:
    half = (Node.pos) // 2
    headd: Node= head
    first_half: list= []
    second_half: list= []
    for i in range(Node.pos):
        if i < half:
            first_half.append(headd.data)
            headd = headd.next
        else:
            second_half.append(headd.data)
            headd = headd.next
            
    second_half = list(reversed(second_half))
    if (Node.pos - 1) > 1:
        if (Node.pos - 1) % 2 != 1:
            second_half.pop()
        
    for i in range(len(first_half)):
        if first_half[i] != second_half[i]:
            return False
    return True



ll1 = LinkedList()
for value in [1, 2, 3, 2, 1]:
    ll1.append(value)
print(is_palindrome(ll1.head)) #True

ll2 = LinkedList()
for value in [1, 2, 3, 4, 5]:
    ll2.append(value)
print(is_palindrome(ll2.head)) #False

ll3 = LinkedList()
ll3.append(1)
print(is_palindrome(ll3.head)) #True

ll4 = LinkedList()
ll4.append(1)
ll4.append(1)
print(is_palindrome(ll4.head)) #True

ll5 = LinkedList()
ll5.append(1)
ll5.append(2)
print(is_palindrome(ll5.head)) #False