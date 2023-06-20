'''def strcounter(s):
    for sym in set(s): #(a - 7,a - 7,a - 7,a - 7,a - 7,a - 7,a - 7) результат без set
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count += 1
        print(f'{sym} - {count}')

strcounter('aaaaaaa') #(a - 7)'''

#O(2 ** N)
'''def strcounter(s):
    sym_dict = {}
    for sym in s:
        sym_dict[sym] = 1 + sym_dict.get(sym, 0)
    for sym, count in sym_dict.items():
        print(f'{sym} - {count}')'''
        



def strcounter(s):
    for sym in set(s):
        print(f'{sym} - {s.count(sym)}')

strcounter('aaaaaaa')

