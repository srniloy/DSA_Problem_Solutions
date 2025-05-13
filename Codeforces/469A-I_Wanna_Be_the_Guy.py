
n = int(input())
little_x = {}
little_y = {}

lines = list(map(int, input().split()))
little_x['completed'] = lines[0]
little_x['steps'] = lines[1:]

lines = list(map(int, input().split()))
little_y['completed'] = lines[0]
little_y['steps'] = lines[1:]



total_steps = sorted(little_x['steps']+little_y['steps'])
count = 1
for i in range(len(total_steps)-1):
    if total_steps[i] != total_steps[i+1]:
        count += 1
if little_x['completed'] == 0 and little_y['completed'] == 0:
    print("Oh, my keyboard!")
else:
    print("I become the guy." if count >= n else "Oh, my keyboard!")

