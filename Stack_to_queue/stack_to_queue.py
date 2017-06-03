from arrayqueue import ArrayQueue
from arraystack import ArrayStack

def stack_to_queue(stack):
    queue = ArrayQueue()
    stack = list(stack)
    for element in stack[::-1]:
        queue.add(element)
    return queue