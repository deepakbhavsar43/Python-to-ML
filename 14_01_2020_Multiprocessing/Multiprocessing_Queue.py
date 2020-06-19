from multiprocessing import Queue

countries = ['America', 'Russia', 'Germany', 'Japan', 'India']
cnt = 1
# instantiating a queue object
queue = Queue()
print("pushing items to queue :")
for country in countries:
    print("item no :", cnt, ' ', country)
    queue.put(country)
    cnt += 1

print('\nPopping items from queue:')
cnt = 0
print(queue.empty())
while not queue.empty():
    print('item no: ', cnt, ' ', queue.get())
    cnt += 1
print(queue.empty())
