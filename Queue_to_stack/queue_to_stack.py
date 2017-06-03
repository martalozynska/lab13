from arrayqueue import ArrayQueue
from arraystack import ArrayStack

def queue_to_stack(queue):
    stack = ArrayStack()
    que = ArrayQueue(queue)
    lst = []
    while len(que) != 0:
        lst.append(que.pop())
    quee = ArrayQueue(lst[::-1])
    while len(quee) != 0:
        stack.push(quee.pop())
    return stack