def calculate_largest_rectangle(heights):
    sorted_heights=sorted(list(set(heights)),reverse=True)
    print(sorted_heights)
    stack = [min(heights)]
    accumulated_rectangle = 0
    for max_current_height in sorted_heights:
        for height in heights:
            if height >= max_current_height:
                accumulated_rectangle += max_current_height
            elif height<max_current_height:
                compare_acc_height_to_stack(accumulated_rectangle, stack)
                accumulated_rectangle=0

        compare_acc_height_to_stack(accumulated_rectangle, stack)
        accumulated_rectangle=0

    return stack[-1]


def compare_acc_height_to_stack(accumulated_rectangle, stack):
    if accumulated_rectangle > stack[-1]:
        stack.pop()
        stack.append(accumulated_rectangle)

heights=[1,55,13,11,11,11,11]
print(calculate_largest_rectangle(heights))
