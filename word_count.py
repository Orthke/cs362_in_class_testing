#Word count

def count_words(sentence):
    if sentence == "":
        return 0
    return len(sentence.split(' '))

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    print("Your sentence has {} words".format(count_words(user_input)))