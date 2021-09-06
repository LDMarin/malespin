

def user_in():
    return input("Palabra a traduccir: ")


def ask_to_continue():
    return input("Desea traduccir otra palabra S / N: ").lower()


def translate(word):
    word = word.lower()
    new_word = ""
    for letter in word:
        if letter == "a":
            letter = "e"
        elif letter == "e":
            letter = "a"
        elif letter == "b":
            letter = "t"
        elif letter == "t":
            letter = "b"
        elif letter == "i":
            letter = "o"
        elif letter == "o":
            letter = "i"
        elif letter == "f":
            letter = "g"
        elif letter == "g":
            letter = "f"
        elif letter == "p":
            letter = "m"
        elif letter == "m":
            letter = "p"
        new_word += letter
    return new_word


def main():
    while True:
        word = user_in()
        new_word = translate(word)
        print(new_word)
        atc = ask_to_continue()
        if atc != "s":
            break


if __name__ == "__main__":
    main()
