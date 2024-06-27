# Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle
#  in a linked list if there is some node in the list that can be reached again by continuously following
#  the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
#  connected to. Note that pos is not passed as a parameter. Return true if there is a cycle in the linked list.
#  Otherwise, return false.
 
# Model the Node and Linked List concepts using classes.

class Node:
    pos: int= 0
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.pos = Node.pos
        Node.pos += 1 


        
class LinkedList:
    pass
        
def has_cycle(head: Node) -> list[int]:
    pass




ll1: LinkedList= LinkedList()
for i in range(5):
    ll1.append(i)
node1: Node= ll1.get_node(1)  # Node with value 1
node4: Node= ll1.get_node(4)  # Node with value 4
node4.next = node1  # Creating a cycle

print(has_cycle(ll1.head)) # True