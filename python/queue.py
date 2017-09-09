# encoding: utf-8

import Queue

fifo_queue = Queue.Queue(maxsize=10)
lifo_queue = Queue.LifoQueue(maxsize=10)
priority_queue = Queue.PriorityQueue(maxsize=10)

fifo_queue.put('first')
fifo_queue.put('last')
print "fifo queue get {0}".format(fifo_queue.get())


lifo_queue.put('first')
lifo_queue.put('last')
print "lifo queue get {0}".format(lifo_queue.get())


priority_queue.put('first')
priority_queue.put('last')
print "priority queue get {0}".format(priority_queue.get())
