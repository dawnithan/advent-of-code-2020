with open("day25-input.txt") as file:
    data = [int(d.strip()) for d in file.readlines()]

subject_number = 7
initial_number = 1

count = 0

while initial_number != data[0]:
    initial_number *= subject_number 
    initial_number %= 20201227
    count += 1
    
# https://sublimerobots.com/2015/01/simple-diffie-hellman-example-python/
print(pow(data[1], count, 20201227))