import random

compiled_sentence = ""
# all types of sentences used in this program
type_of_sentence_structures = ["Subject-verb", "Subject-verb-object", "Subject-verb-adjective",
                               "Subject-verb-adverb-noun"]

# create list of nouns from text file
nouns = open("sentence_objects/nouns.txt")
nouns_list = nouns.read().split(";")

# create list of verbs from text file
verbs = open("sentence_objects/verbs.txt")
verbs_list = verbs.read().split(";")
verbs_present = open("sentence_objects/present_tense_verbs")
verbs_present_list = verbs_present.read().split(";")

# create list of adjectives from text file
adjectives = open("sentence_objects/adjectives.txt")
adjectives_list = adjectives.read().split(";")

# create a list of descriptive words
description_verbs = open("sentence_objects/description_verbs")
description_verbs_list = description_verbs.read().split(";")

# create a list of descriptive words
adverbs = open("sentence_objects/adverbs.txt")
adverbs_list = description_verbs.read().split(";")

# create a list of preposition words
manner_prepositions = open("sentence_objects/prepositions/manner.txt")
manner_prepositions_list = manner_prepositions.read().split(";")
time_prepositions = open("sentence_objects/prepositions/time.txt")
time_prepositions_list = time_prepositions.read().split(";")
manner_prepositions.close()


def generate_subject_verb():
    """Uses a template to randomly generate a subject-verb sentence using words from a separate text file"""
    constructed_sentence = nouns_list[random.randint(0, len(nouns_list) - 1)] + " " + \
                           manner_prepositions_list[random.randint(0, len(manner_prepositions_list) - 1)] + " " + \
                           verbs_present_list[random.randint(0, len(verbs_present_list) - 1)] + " " \
                           + time_prepositions_list[random.randint(0, len(time_prepositions_list) - 1)] + "."
    # return the assembled sentence
    return constructed_sentence


def generate_verb_object():
    """Uses a template to randomly generate a verb-object sentence using words from a separate text file"""
    # arrange the randomly selected words into the template format
    constructed_sentence = nouns_list[random.randint(0, len(nouns_list) - 1)] + " " + \
                           verbs_list[random.randint(0, len(verbs_list) - 1)] + " " + \
                           nouns_list[random.randint(0, len(nouns_list) - 1)] + "."
    # return the assembled sentence
    return constructed_sentence


def generate_verb_adjective():
    """Uses a template to randomly generate a verb-adjective sentence using words from a separate text file"""
    # arrange the randomly selected words into the template format
    constructed_sentence = nouns_list[random.randint(0, len(nouns_list) - 1)] + " " + \
                           description_verbs_list[random.randint(0, len(description_verbs_list) - 1)] + " " + \
                           adjectives_list[random.randint(0, len(adjectives_list) - 1)] + "."
    # return the assembled sentence
    return constructed_sentence


def generate_subject_verb_adverb_noun():
    """Uses a template to randomly generate a subject-verb0adverb-object
    sentence using words from a separate text file"""
    # arrange the randomly selected words into the template format
    constructed_sentence = nouns_list[random.randint(0, len(nouns_list) - 1)] + " " + \
                           verbs_list[random.randint(0, len(verbs_list) - 1)] + " " + \
                           adverbs_list[random.randint(0, len(adverbs_list) - 1)] + \
                           nouns_list[random.randint(0, len(nouns_list) - 1)] + "."

    # return the assembled sentence
    return constructed_sentence


class sentence:
    """A sentence object that can generate a grammaticaly correct sentence"""

    def __init__(self, sentence_structure_class):
        """initiate the sentence type for the sentence class"""
        self.structure_type = type_of_sentence_structures[sentence_structure_class]

    def compile_sentence(self):
        """randomly select one of sentence generating functions above and use them to generate a sentence"""
        # check what type of sentence the object wants to be compiled
        global compiled_sentence

        if self.structure_type is type_of_sentence_structures[0]:  # subject verb
            compiled_sentence = generate_subject_verb()
        elif self.structure_type is type_of_sentence_structures[1]:  # subject verb object
            compiled_sentence = generate_verb_object()
        elif self.structure_type is type_of_sentence_structures[2]:  # subject verb adjective
            compiled_sentence = generate_verb_adjective()
        elif self.structure_type is type_of_sentence_structures[3]:  # subject verb adverb noun
            compiled_sentence = generate_subject_verb_adverb_noun()

        # make sure the first letter of the sentence is capitalized

        # Divide the sentence into separate words and check if the first word has a capital letter
        compiled_sentence_words = compiled_sentence.split()
        compiled_sentence = ""
        # Put the words back together in order
        for i in range(len(compiled_sentence_words)):
            if i == 0:
                compiled_sentence += compiled_sentence_words[i].capitalize()
            else:
                compiled_sentence += compiled_sentence_words[i]
            compiled_sentence += " "
        # return the finished compiled sentence
        return compiled_sentence
