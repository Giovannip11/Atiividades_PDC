from my_thread import MyThread


thread_01 = MyThread ('A',0.5)
thread_02 = MyThread ('B',1)


thread_01.start()
thread_02.start()

thread_01.join()
thread_02.join()



print('FIM')