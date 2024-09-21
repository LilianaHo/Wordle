import random


# generates a list of words from a txt file list
def generate_wordlist(possible_words):
    word_list = []
    with open(possible_words) as f:
        count = sum(1 for _ in f)
    with open(possible_words) as f:
        for _ in range(count):
            line = f.readline()[:5]
            word_list.append(line)
    return word_list


def letter_freq(word):
    letters = []
    freq = []
    for i in word:
        if i not in letters:
            letters.append(i)
            freq.append(int(1))
        else:
            for k in range(len(letters)):
                if letters[k] == i:
                    freq[k] = int(freq[k]) + 1
    return letters, freq


def play(guess_list, answer_list, rounds, word_len = 5):
    possible_guesses, answer = generate_wordlist(str(guess_list)), random.choice(generate_wordlist(str(answer_list)))
    round_over = False
    print("Welcome to Worlde! Try and guess the five letter word in six tries.")
    print("X = letter does not appear in word")
    print("Y = letter appears in word")
    print("G = letter appears in word in that place")
    for i in range(rounds):
        guessing = True
        guess, output = "", []
        while guessing and not round_over:
            guess = input("Guess " + str(i + 1) + "\n").lower()
            if len(guess) == word_len and guess in possible_guesses: guessing = False
            else: print("Invalid Input!")
        letters, freq = letter_freq(answer)
        if not round_over:
            for j in range(word_len):
                if guess[j] == answer[j]:
                    output.append("G")
                    for k in range(len(letters)):
                        if letters[k] == answer[j]:
                            freq[k] = int(freq[k]) - 1
                else: output.append("X")
            for j in range(word_len):
                if guess[j] in answer and output[j] == "X":
                    for k in range(len(letters)):
                        if letters[k] == guess[j]:
                            if freq[k] > 0:
                                output[j] = "Y"
                                freq[k] = int(freq[k]) - 1
            output = "".join(output)
        if output.count("G") == word_len: round_over = True
        print(output)
    print(answer)


guesses = "wordlist.txt"
answers = "answers.txt"

play(guesses, answers, 6)
