import random
from collections import defaultdict
def main():
    T=set() # 変数 # 左辺に登場するものはすべて変数 / そうでないものはすべて終端記号
    grammer = defaultdict(list)

    with open('grammer.txt','r') as f:
        for line in f:
            left = line.split('->')[0].strip()
            right = line.split('->')[1].strip()
            grammer[left].append(right)
            T.add(left)
    
    already_output=set()
    for _ in range(20):
        string='S'
        while True:
            if all([s not in T for s in string]):#すべて終端記号
                if string not in already_output:
                    already_output.add(string)
                    print(string)
                #print('-----')
                break
            
            T_idxs=[i for i,s in enumerate(string) if s in T]
            idx=random.choice(T_idxs)

            rpl=random.choice(grammer[string[idx]])
            if rpl=="_":
                rpl=""

            string=string[:idx]+rpl+string[idx+1:]

            #print(string)

if __name__ == "__main__":
    main()