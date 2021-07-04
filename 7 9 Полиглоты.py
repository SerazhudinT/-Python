fin = open('/Users/Serazhudin/PycharmProjects/pythonProject/input.txt', 'r', encoding='utf8')

N = int(fin.readline())

all_lang = set()
inter_lang = set()

for i in range(N):
    M = int(fin.readline())
    
    cur_langs = set()
    
    for j in range(M):
        lang = fin.readline().split()[0]
                
        all_lang.add(lang)
        
        cur_langs.add(lang)
        
    if i == 0:
        inter_lang = cur_langs
    else:
        inter_lang &= cur_langs

print(len(inter_lang))
print('\n'.join(inter_lang))

print(len(all_lang))
print('\n'.join(all_lang))

