import random
from collections import defaultdict
def main():
    N=20 # 生成する個数 

    T=set() # 変数 # 左辺に登場するものはすべて変数 / そうでないものはすべて終端記号
    grammer = defaultdict(list)

    with open('grammer.txt','r') as f:
        for line in f:
            if line.strip()=='' or line.startswith('#'):
                continue
            left = line.split('->')[0].strip()
            right = line.split('->')[1].strip()
            grammer[left].append(right)
            T.add(left)
    
    for key in grammer.keys():
        grammer[key].sort(key=lambda right: len([x for x in right if x in T])) #変数の数が少ない順
    
    already_output=set()
    for _ in range(N):
        string='S'
        while True:
            if all([s not in T for s in string]):#すべて終端記号
                if string not in already_output:
                    already_output.add(string)
                    print(string)
                    # assert string.count('a') == string.count('b')
                #print('-----')
                break
            
            T_idxs=[i for i,s in enumerate(string) if s in T]
            idx=random.choice(T_idxs)

            if len(string)>10:# stringが十分に長くなりそうになったら終端記号優先モードに
                rpl=grammer[string[idx]][0]
            else:
                rpl=random.choice(grammer[string[idx]])
            if rpl=="_":
                rpl=""

            string=string[:idx]+rpl+string[idx+1:]

            #print(string)

if __name__ == "__main__":
    main()