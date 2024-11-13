def check_parentheses(s: str) -> bool:
    open_count = 0
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1
            if open_count < 0:
                return False
    return open_count == 0
