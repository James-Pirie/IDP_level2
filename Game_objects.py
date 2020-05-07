def check_answer(answer_input: str, desired_answer: str):
    """a system which intakes a complete sentence and another sentence and compares
    the two and scores the other sentence on how similar it is to the complete sentence. """
    # initialize the points variable
    points = 0
    # first check if the two points are identical and award points if they are
    if answer_input == desired_answer:
        points += 10
        print(f"'{answer_input}' is 100% similar to '{desired_answer}'")
    elif len(answer_input) == 0:
        print(f"'{answer_input}' is 0% similar to '{desired_answer}'")
        points = 0
    else:
        words_in_answer_input = answer_input.split()
        words_in_desired_answer = desired_answer.split()
        max_similarity = 10
        total_similarity = 0
        similarity_per_word = max_similarity / len(words_in_desired_answer)
        if len(words_in_desired_answer) == len(words_in_answer_input):
            print("more words")
            for i in range(len(words_in_desired_answer)):
                try:
                    similarity: int = 0
                    user_answer_word_being_analysed = words_in_answer_input[i]
                    desired_answer_word_being_analysed = words_in_desired_answer[i]
                    similarity_per_letter_in_word = similarity_per_word / len(desired_answer_word_being_analysed)
                    for y in range(len(user_answer_word_being_analysed)):
                        if user_answer_word_being_analysed[y] == desired_answer_word_being_analysed[y]:
                            similarity += similarity_per_letter_in_word
                    total_similarity += similarity
                except IndexError:
                    print("Index error")
                if total_similarity > 9:
                    points += 4
                elif total_similarity > 7:
                    points += 3
                elif total_similarity > 6:
                    points += 2
                elif total_similarity > 5:
                    points += 1
            print(f"'{answer_input}' is {total_similarity * 10}% similar to '{desired_answer}'")
        elif len(words_in_desired_answer) != len(words_in_answer_input):
            print("less words")
            combined_input = answer_input.strip()
            combined_desired = desired_answer.strip()
            maximum_similarity = 10
            similarity = 0
            similarity_per_word = maximum_similarity/len(combined_input)
            print(similarity_per_word)
            try:
                for z in range(len(combined_desired)):
                    if combined_input[z] == combined_desired[z]:
                        similarity += similarity_per_word
                        print("adding")
                print(f"'{answer_input}' is {similarity * 10}% similar to '{desired_answer}'")
            except IndexError:
                print("Error")
                print(f"'{answer_input}' is {similarity * 10}% similar to '{desired_answer}'")
            if similarity > 9:
                points += 3
            elif similarity > 7:
                points += 2
            elif similarity > 6:
                points += 1
    return points


test_answer = "The man fed the duck."
test_desired_answer = "The man fed the duck."

if __name__ == '__main__':
    print("Testing")
    x = check_answer(test_answer, test_desired_answer)
    print(f"points = {x}")
