# ===================================================== Imports ========================================================

from playsound import playsound


# ==================================================== functions =======================================================


def check_answer(answer_input: str, desired_answer: str):
    """a system which intakes a complete sentence and another sentence and compares
    the two and scores the other sentence on how similar it is to the complete sentence. """
    counter = 0
    special_condition_retrieval = open("game_data/data.txt")
    special_condition = special_condition_retrieval.read()
    # initialize the points variable
    scores = {"Words": 0, "Letters": 0, "Sentences": 0, "Score": 0, "Correct_words": 0, "Correct_letters": 0,
              "Sim": 0, "total": 0}
    scores["total"] += 1
    scores["Words"] += len(answer_input.split(" "))
    scores["Sentences"] += 1
    sentence = answer_input.split(" ")
    for i in range(len(sentence)):
        for i in range(len(sentence[i])):
            scores["Letters"] += 1

    # first check if the two points are identical and award points if they are
    if answer_input == desired_answer:
        scores["Score"] += 10
        print(f"'{answer_input}' is 100% similar to '{desired_answer}'")
        scores["Correct_words"] += len(answer_input.split(" "))
        words = answer_input.split(" ")
        for i in range(len(words)):
            for x in range(len(words[i])):
                scores["Correct_letters"] += 1
    elif len(answer_input) < 2:
        scores["Score"] += 0
    # if there are zero words in the answer award zero points
    elif len(answer_input) == 0:
        print(f"'{answer_input}' is 0% similar to '{desired_answer}'")
        scores["Score"] = 0
        scores["Sim"] += similarity
    elif answer_input.strip().lower() == special_condition.strip().lower():
        playsound("audio/special_condition.mp3")
        scores["Score"] += 1000
        scores["Correct_words"] += 1000
        scores ["Correct_letters"] += 1000
    # if the other two don't amount to anything do an indent analysis of each word and letter the user imputed
    else:
        # split the sentences up into words
        words_in_answer_input = answer_input.split()
        words_in_desired_answer = desired_answer.split()
        # establish some of the boundaries for how similar two sentences can be
        max_similarity = 10
        total_similarity = 0
        similarity_per_word = max_similarity / len(words_in_desired_answer)
        # if there are the same amount of words in both strings analyse based on word similarities
        if len(words_in_desired_answer) == len(words_in_answer_input):
            # loop through every word in the string and compare the letters in the words
            for i in range(len(words_in_desired_answer)):
                # try statement so the code is able to deal with potential index errors
                try:
                    # reset base similarity to zero
                    similarity: int = 0
                    # divide the words up in to individual letters
                    user_answer_word_being_analysed = words_in_answer_input[i]
                    desired_answer_word_being_analysed = words_in_desired_answer[i]
                    # divide the max similarity per word by the amount of letters to be awarded to similar letters
                    similarity_per_letter_in_word = similarity_per_word / len(desired_answer_word_being_analysed)
                    # check if the letters are the same
                    for y in range(len(user_answer_word_being_analysed)):
                        if user_answer_word_being_analysed[y] == desired_answer_word_being_analysed[y]:
                            similarity += similarity_per_letter_in_word
                            if counter != 0:
                                scores["Correct_letters"] += len(user_answer_word_being_analysed)
                                scores["Sim"] += similarity
                    total_similarity += similarity
                except IndexError:
                    print("Index error")
                    counter += 1
                # calculate the score based on how similar the two sentences are
                if total_similarity > 9:
                    scores["Score"] += 4
                    scores["Sim"] += similarity
                elif total_similarity > 7:
                    scores["Score"] += 3
                    scores["Sim"] += similarity
                elif total_similarity > 6:
                    scores["Score"] += 2
                    scores["Sim"] += similarity
                elif total_similarity > 5:
                    scores["Score"] += 1
                    scores["Sim"] += similarity
            print(f"'{answer_input}' is {total_similarity * 10}% similar to '{desired_answer}'")
        # if the two words are of different length compare them for each letter as a whole and penalize
        elif len(words_in_desired_answer) != len(words_in_answer_input):
            # divide the sentence into individual letters
            combined_input = answer_input.strip()
            combined_desired = desired_answer.strip()
            maximum_similarity = 10
            similarity = 0
            similarity_per_word = maximum_similarity / len(combined_input)
            # accommodate the code for potential index errors
            try:
                # check every letter in the word and then assign an overall similarity score
                for z in range(len(combined_desired)):
                    if combined_input[z] == combined_desired[z]:
                        if counter < 1:
                            scores["Correct_letters"] += 1
                            similarity += similarity_per_word
                            scores["Sim"] += similarity
                print(f"'{answer_input}' is {similarity * 10}% similar to '{desired_answer}'")
            except IndexError:
                print("Index error 1")
                counter += 1
                print(f"'{answer_input}' is {similarity * 10}% similar to '{desired_answer}'")
            # calculate the score with the additional penalty of having the wrong amount of words
            if similarity > 9:
                scores["Score"] += 4
                scores["Sim"] += similarity
            elif similarity > 7:
                scores["Score"] += 3
                scores["Sim"] += similarity
            elif similarity > 6:
                scores["Score"] += 2
                scores["Sim"] += similarity


    return scores


# ====================================================== Tests =========================================================

# test sentences
test_answer = "Test answer"
test_desired_answer = "Test answer"

# test conditions
if __name__ == '__main__':
    print("Testing")
    x = check_answer("Sara won't clean today.", "John Cena won't date now.")
    print(f"points = {x}")
