import threading


def function(i):
    print('Função chamada pelo thread %i\n' % i)
    return 


threads = []
for i in range(5):
    t =threading.Thread(target=function,args=(i,))
    threads.append(t)
    t.start()
    t.join()

print(threads)