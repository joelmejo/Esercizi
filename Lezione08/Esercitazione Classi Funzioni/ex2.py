# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack
#  should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# - push(x: int) -> None: Pushes element x to the top of the stack.
# - pop() -> None Removes the element on the top of the stack and returns it.
# - pop() -> None Returns the element on the top of the stack.
# - empty() -> None Returns true if the stack is empty, false otherwise.

class Queue:
    def __init__(self) -> None:
        self.coda: list = []

    def push(self, x) -> None:
        self.coda.append(x)

    def pop(self) -> int:
        return self.coda.pop(-1)
    
    def top(self) -> int:
        return self.coda[-1]
    
    def empty(self) -> bool:
        return len(self.coda) == 0


class MyStack:
    def __init__(self) -> None:
        self.coda1: Queue=Queue()
        self.coda2: Queue=Queue()
    
    def push(self, x) -> None:
        while not self.coda1.empty():
            element: int= self.coda1.pop()
            self.coda2.push(element)

        self.coda1.push(x)

        while not self.coda2.empty():
            element: int= self.coda2.pop()
            self.coda1.push(element)
    
    def pop(self) -> int:
        while len(self.coda1.coda) > 1:
            element: int= self.coda1.pop()
            self.coda2.push(element)

        removed = self.coda1.pop()

        while not self.coda2.empty():
            element: int= self.coda2.pop()
            self.coda1.push(element)
        return removed
    
    def top(self) -> int:
        while not self.coda1.empty():
            element: int= self.coda1.pop()
            self.coda2.push(element)

        result = self.coda2.top()

        while not self.coda2.empty():
            element: int= self.coda2.pop()
            self.coda1.push(element)
        
        return result
    
    def empty(self) -> bool:
        return self.coda1.empty()

mystack = MyStack()
mystack.push(1)
mystack.push(2)
print(mystack.top())    # Output: 2
print(mystack.pop())    # Output: 2
print(mystack.empty())  # Output: False
print(mystack.pop())    # Output: 1
print(mystack.empty())  # Output: True