def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    Takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    return "un" + word


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    Takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    return (' :: ' + vocab_words[0]).join(vocab_words)


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    Takes in a word and returns the base word with `ness` removed.
    """
    return word[:-5] + "y" if word.endswith("iness") else word[:-4]


def noun_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    Takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    return sentence.split()[index].rstrip(".") + "en"
