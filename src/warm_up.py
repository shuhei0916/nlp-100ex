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

def ngram(sequence, n):
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

def generate_bigram_set(text):
    text = text.replace(" ", "")
    res = {text[i:i+2] for i in range(len(text) - 1)}
    return res

def template_string(x, y, z):
    return f"{x}時の{y}は{z}"

def cipher(text):
    result = []
    for char in text:
        if char.islower():
            result.append(chr(219 - ord(char)))
        else:
            result.append(char)
    return "".join(result)
    # return "".join([chr(219 - ord(c)) if c.islower() else c for c in text])