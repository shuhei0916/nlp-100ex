import MeCab
tager = MeCab.Tagger()
with open('data/neko.txt', 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        print(line)
        i += 1
        if i > 20:
            break


# test = "吾輩は猫である。名前はまだ無い。"

# tagger = MeCab.Tagger()
# print(tagger.parse("吾輩は猫である。"))
# col = tagger.parse("吾輩は猫である。").split()

# print(col)