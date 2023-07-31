def hexadecimal(start, end):
    new_line = [f"{i} = {hex(i)}" for i in range(start, end + 1)]
    return "\n".join(new_line)

print(hexadecimal(1, 98))