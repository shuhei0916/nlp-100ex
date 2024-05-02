import collections

def main():
    filename = './data/popular-names.txt'
    name_list = []
    with open(filename, 'r') as f:
        for line in f:
            name, sex, num, year = line.rstrip('\n').split(' ')
            name_list.append(name)
        
    name_counts = collections.Counter(name_list)
    # print(c)
    for name, count in name_counts.most_common():
        print(f'{name}: {count}')
        

if __name__ =='__main__':
    main()
    
'''
UNIXコマンドは以下のようになる（ムズ。。。）

cut -d " " -f 1 ./data/popular-names.txt | sort | uniq -c | sort -n  -r | head -20
cut -d " " -f 1 : ファイルをスペースで区切り（delimiter -d）、1番目のフィールド（ここでは名前）のみを切り出す。
sort | uniq: この二つのコマンドを組み合わせることで、重複を除いている（uniqは隣接する同じ要素を除くので、前処理としてsortで並べている）。sortに-cオプションをつけることで、カウントしている。
sort -n -r: 上記で得られた出力をさらにソートしている。-nで数字としてソートし、-rで逆順（reverse）でソートしている。
'''
