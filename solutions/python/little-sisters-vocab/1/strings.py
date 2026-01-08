"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word    


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    result = [prefix]
    for word in words:
        result.append(prefix + word)
    return ' :: '.join(result)
    


def remove_suffix_ness(word):
    root = word[:-4]
    if root[-1] == "i":    
        return root[:-1] + "y"
    else:
        return root 

    
def adjective_to_verb(sentence, index):
    words = sentence.split()
    target_word = words[index].strip(".")
    return target_word + "en"
