def check_balanced_bracket():
    stack = list()
    bracket = input("Bracket: ")
    for character in bracket:
        if character == "(" or character == "[":
            stack.append(character)
            continue
        # Check if the stack is empty
        if len(stack) == 0:
            return False
        if (character == ")" and stack.pop() != "(") or character == "]" and stack.pop() != "[":
            return False
    # Check if the stack is empty
    return len(stack) == 0


def main():
    print(check_balanced_bracket())


main()
