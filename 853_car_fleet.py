def calculate_car_fleet(target: int, position, speed):
    cars_pos_speed = sorted(zip(position, speed))
    stack = []
    for car_pos, car_speed in reversed(cars_pos_speed):
        time = (target - car_pos) / car_speed
        if not stack or time > stack[-1]:
            stack.append(time)

    return len(stack)


position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
res = calculate_car_fleet(12, position, speed)
print(res)
