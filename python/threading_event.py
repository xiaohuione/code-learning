# encoding: utf-8
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

def worker(event):
    while not event.is_set():
        logging.debug('Waiting for redis ready...')
        event.wait(1)
    logging.debug('redis ready, and connect to redis server and do some work [%s]', time.ctime())
    time.sleep(1)
    logging.debug('work done')

if __name__ == '__main__':
    readis_ready = threading.Event()
    threads = []
    t1 = threading.Thread(target=worker, args=(readis_ready,), name='t1')
    threads.append(t1)
    t2 = threading.Thread(target=worker, args=(readis_ready,), name='t2')
    threads.append(t2)
    for t in threads:
        logging.debug("start {0}".format(t.name))
        t.start()

    logging.debug('first of all, check redis server, make sure it is OK, and then trigger the redis ready event')
    time.sleep(3) # simulate the check progress 
    readis_ready.set()
    t.join()
    logging.debug('end test')
