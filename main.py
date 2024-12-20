def main(): 
    text = getText("/Users/jdiegoms/workspace/github.com/jdiegoms/bookbot/books/frankenstein.txt")
    num_words = numWords(text) 
    chars = chardDict(text)
    report = getReport(text, num_words, chars)
    print(report)
    return


def numWords(text):
    words = text.split()
    return len(words)

def getText(path):
    with open(path) as f:
        contents = f.read()
    return contents

def chardDict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def getReport(text, num_words, chars):
    print("Begin Report:")
    print(f"there are {num_words} words in this text!")
    print("----------Character Count----------")
    for key, value in chars.items():
        if (key.isalpha()):
            if value != 1:
                print(f"The character {key} is used {value} times in this text")
            else:
                print(f"The character {key} is used {value} time in this text")
    return("End Report")


main()
