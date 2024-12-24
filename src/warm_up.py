def reverse_string(s):
    return s[::-1]

def extract_old_characters(s):
    return s[::2]


def interleave_strings(s1, s2):
    return "".join([a + b for a, b in zip(s1, s2)] )
    # res = ""
    # for i, j in zip(s1, s2):
    #     res += i + j
    # return res
    
    
def get_word_lengths(sentence):
    return [len(word.strip(",.")) for word in sentence.split()]

def create_element_dict(sentence):
    words = sentence.split()
    one_char_poisition = {1, 5, 6, 7, 8, 9, 15, 16, 19}
    element_dict = {}
    for i, word in enumerate(words, start=1):
        if i in one_char_poisition:
            element_dict[word[:1]] = i
        else:
            element_dict[word[:2]] = i
    return element_dict

def ngram(sequence, n, mode):   
    if mode == "char":
        sequence = sequence.replace(" ", "")
        return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]
    elif mode == "word":
        return [sequence.split()[i:i+n] for i in range(len(sequence.split()) - n + 1)]
    else:
        raise ValueError("mode must be 'char' or 'word'")



# def ngram(sequence, n):
#     return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]