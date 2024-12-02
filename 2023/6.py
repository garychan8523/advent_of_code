from functools import reduce

# times = [7, 15, 30]
# distances = [9, 40, 200]

times = [59688274]
distances = [543102016641022]

def get_distance(hold_time, total_time):
    return (total_time - hold_time) * hold_time

out = []
for i in range(len(times)):
    time = times[i]
    counter = 0
    for j in range(time+1):
        if get_distance(j, time) > distances[i]:
            counter += 1
    out.append(counter)

print(out)
print(reduce((lambda x, y: x * y), out))
