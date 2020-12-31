from queue import Queue

with open("day22-input.txt") as file:
    data = [d.strip() for d in file.readlines()]

p1_q = Queue(maxsize=50)
p2_q = Queue(maxsize=50)

curr_q = p1_q
for line in data:
    if len(line) < 1:
        curr_q = p2_q
    elif not line.startswith("Player"):
        curr_q.put(int(line))
    
print(p1_q.queue)
print(p2_q.queue)

while True:
    if p1_q.empty() or p2_q.empty():
        break

    p1_draw = p1_q.get()
    p2_draw = p2_q.get()

    if p1_draw > p2_draw:
        p1_q.put(p1_draw)
        p1_q.put(p2_draw)
    elif p1_draw < p2_draw:
        p2_q.put(p2_draw)
        p2_q.put(p1_draw)

print(p1_q.queue)
print(p2_q.queue)

winning_q = p1_q if p1_q.full() else p2_q

total = 0
pos = len(winning_q.queue)
for _ in range(len(winning_q.queue)):
    total += winning_q.get() * pos
    pos -= 1

print(total)