def print_line(length: int, pen: str) -> None:
    """Print a line of length with pen characters."""
    print(pen*length)

def get_string():
    string = input("String: ")
    return string

print_line(25, "<UNK>")
name = get_string()
print("CP1404"[name])
