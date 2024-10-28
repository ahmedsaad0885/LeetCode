def generate_parentheses(n):
    stack = [("(", 1, 0)]
    result = []
    while stack:
        current, open_count, closed_count = stack.pop()
        if len(current) == 2 * n:
            result.append(current)
            continue

        if closed_count < open_count:
            stack.append((current + ")", open_count, closed_count + 1))

        if open_count < n:
            stack.append((current + "(", open_count + 1, closed_count))
    return result


print(generate_parentheses(3))
