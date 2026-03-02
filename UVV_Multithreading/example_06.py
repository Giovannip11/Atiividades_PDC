import queue

fila_fifo = queue.PriorityQueue()

fila_fifo.put("Primeiro da fila")

fila_fifo.put("Segundo da fila")

fila_fifo.put("Terceiro da fila")

print(fila_fifo.get())

fila_prior = queue.PriorityQueue()
fila_prior.put((532,"Primeiro da fila"))
fila_prior.put((89,"Segundo da fila"))
fila_prior.put((53,"Terceiro da fila"))

print("PRIOR: ",fila_prior.get())
