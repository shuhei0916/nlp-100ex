import MeCab

test = "吾輩は猫である。名前はまだ無い。"

tagger = MeCab.Tagger()
print(tagger.parse("吾輩は猫である。"))
col = tagger.parse("吾輩は猫である。").split()
print(col)