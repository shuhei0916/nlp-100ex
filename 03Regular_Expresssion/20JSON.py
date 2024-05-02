import json
import gzip
import shutil

dic = json.loads('{"bar":["baz", null, 1.0, 2]}')
print(type(dic))
print(dic)

dumped = json.dumps(dic)
print(type(dumped))
print(dumped)

source_file = "jawiki-country.json.gz"
target_file = "jawiki-country.json"

with gzip.open(source_file, mode = "rb") as gf, \
open(target_file, mode = "wb") as df:
    for line in gf:
        wiki_dict = json.loads(line)
        if wiki_dict['title'] == 'イギリス':
            print(wiki_dict.get('text'))

        # df.write(line)
