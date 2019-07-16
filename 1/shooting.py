import math

shots = int(input())
points = 0

for i in range(0, shots):
    nums = input().split()
    cur_points = 0
    x = float(nums[0])
    y = float(nums[1])
    distance = abs(math.sqrt(x**2 + y**2))
    cur_points = math.floor(11 - distance)

    if distance == int(distance):
        cur_points -= 1
    
    if cur_points > 0:
        points += cur_points

print(points)