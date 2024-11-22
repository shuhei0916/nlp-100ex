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
    
    
def get_word_lengths(self):
    return "hoge"