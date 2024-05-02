from collections import deque
import timeit, time

# start = time.time()

N = 10
filename = './data/popular-names.txt'

# readlines()で全行をメモリに読み込んでから処理するやり方。メモリ効率は悪い
def tail_slow():
    with open(filename) as f:
        l = f.readlines()
        l = l[-N:]
        
        for i, line in enumerate(l):
            if i < N:
                print(line, end="")
            else:
                break
        
# dequeを用いるやりかた。こちらの方がメモリ効率が良い
def tail_fast():
    with open(filename) as f:
        last_n_lines = deque(f, N)
        
        for line in last_n_lines:
            print(line, end='')
        
        
if __name__ == "__main__":
    tail_fast()
    # tail_slow()
    
    # compare execution time
    loop = 100
    # timeit.timeit()関数に測定したいコードを渡すとnumber回実行され（デフォルトは100万回）、かかった時間が返される。
    tail_fast_res = timeit.timeit(lambda: tail_fast(), number=loop) 
    tail_slow_res = timeit.timeit(lambda: tail_slow(), number=loop)
    
    print('result of tail_fast(): ', tail_fast_res)
    print('result of tail_slow(): ', tail_slow_res)
