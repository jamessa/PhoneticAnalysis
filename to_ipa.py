from pypinyin import pinyin, Style

# fixme: 目前的用regex取代的方式有很大的問題，因為符號取代錯誤，
# 因此還是用lex and yacc比較好
print(pinyin('此', style=Style.IPA))
assert('tsʰɨ' == pinyin('此', style=Style.IPA)[0][0])


with open('hsbdmj.txt', 'r') as f:
    for line in f:
        p = pinyin(line, errors='ignore', style=Style.IPA)
        # print(line)
        # print(p)

