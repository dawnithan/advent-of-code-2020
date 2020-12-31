example = [
    '939',
    '7,13,x,x,59,x,31,19'
]

example = [e.strip() for e in example]

with open('day13-input.txt') as file:
    data = [d.strip() for d in file.readlines()]

earliest = int(data[0])
bus_ids = [int(x) for x in data[1].split(',') if x != 'x']

max_timestamp = earliest + max(bus_ids)

timetable = {bus: [] for bus in bus_ids} 

for bus in bus_ids:
    total = 0
    entry_name = bus
    while total <= max_timestamp:
        total += bus
        timetable[entry_name].append(total)

results = []

for bus in timetable.keys():
    earliest = int(data[0])
    while True:
        if earliest > max_timestamp:
            break
        if earliest in timetable[bus]:
            results.append((earliest, bus))
            break
        else:
            earliest += 1

departure_time = min(results)[0]
bus_to_take_id = min(results)[1]
earliest = int(data[0])

print(f'Answer = {(departure_time - earliest) * bus_to_take_id}')

data_modified = data[1].split(',')
input_str = ''

for i in range(len(data_modified)):
    if data_modified[i] != 'x':
        input_str += f'(t + {i}) mod {data_modified[i]} = 0, ' 

print(input_str)