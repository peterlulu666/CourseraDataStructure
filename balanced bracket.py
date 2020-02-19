def check_balanced_bracket():
    stack = list()
    bracket = input("Bracket: ")
    for character in bracket:
        if character == "(" or character == "[":
            stack.append(character)
        if len(stack) == 0:
            return False
        if (character == ")" and stack.pop() != "(") or character == "]" and stack.pop() != "[":
            return False
    return True


def main():
    print(check_balanced_bracket())


main()
