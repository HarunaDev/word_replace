# create function to replace word

def replace_word():
    text = "hello everyone, and hello hello to you all"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter word replacement: ")

    print(text.replace(word_to_replace, word_replacement))

replace_word()