from pypinyin import pinyin, Style


def xiaohe(c: str):
    sheng ={
        'sh': 'u',
        'ch': 'i',
        'zh': 'v',
    }

    yun = {
        'iu': 'q',
        'ei': 'w',
        'e': 'e',
        'uan': 'r',
        've': 't',
        'ue': 't',
        'un': 'y',
        'u': 'u',
        'i': 'i',
        'uo': 'o',
        'o': 'o',
        'ie': 'p',
        'a': 'a',
        'iong': 's',
        'ong': 's',
        'ai': 'd',
        'en': 'f',
        'eng': 'g',
        'ang': 'h',
        'an': 'j',
        'ing': 'k',
        'uai': 'k',
        'iang': 'l',
        'uang': 'l',
        'ou': 'z',
        'ia': 'x',
        'ua': 'x',
        'ao': 'c',
        'v': 'v',
        'ui': 'v',
        'in': 'b',
        'iao': 'n',
        'ian': 'm',
    }

    if len(c) <= 2:
        return c
    elif c.startswith(('ch', 'zh', 'sh')):
        s, y = c[:2], c[2:]
        return sheng[s] + yun[y]
    else:
        s, y = c[:1], c[1:]
        return s+yun[y]
    return


def daqian(c: str):
    table = {
        'ㄇ': 'a',
        'ㄖ': 'b',
        'ㄏ': 'c',
        'ㄎ': 'd',
        'ㄍ': 'e',
        'ㄑ': 'f',
        'ㄕ': 'g',
        'ㄘ': 'h',
        'ㄛ': 'i',
        'ㄨ': 'j',
        'ㄜ': 'k',
        'ㄠ': 'l',
        'ㄩ': 'm',
        'ㄙ': 'n',
        'ㄟ': 'o',
        'ㄣ': 'p',
        'ㄆ': 'q',
        'ㄐ': 'r',
        'ㄋ': 's',
        'ㄔ': 't',
        'ㄧ': 'u',
        'ㄒ': 'v',
        'ㄊ': 'w',
        'ㄌ': 'x',
        'ㄗ': 'y',
        'ㄈ': 'z',
        'ㄅ': '1',
        'ㄉ': '2',
        'ˇ': '3',
        'ˋ': '4',
        'ㄓ': '5',
        'ˊ': '6',
        '˙': '7',
        'ㄚ': '8',
        'ㄞ': '9',
        'ㄢ': '0',
        'ㄦ': '-',
        'ㄤ': ';',
        'ㄝ': ',',
        'ㄡ': '.',
        'ㄥ': '/',
    }

    r = ''
    for p in c:
        r+=table[p]
    return r

def shuangmabopomofo(c):
    table = {
        'ㄅ': 'b',
        'ㄆ': 'p',
        'ㄇ': 'm',
        'ㄈ': 'f',
        'ㄉ': 'd',
        'ㄊ': 't',
        'ㄋ': 'n',
        'ㄌ': 'l',
        'ㄍ': 'g',
        'ㄎ': 'k',
        'ㄏ': 'h',
        'ㄐ': 'j',
        'ㄑ': 'q',
        'ㄒ': 'x',
        'ㄓ': 'a',
        'ㄔ': 'v',
        'ㄕ': 'o',
        'ㄖ': 'r',
        'ㄗ': 'w', # z
        'ㄘ': 'c',
        'ㄙ': 's',
        'ㄚ': 'a',
        'ㄛ': 'o',
        'ㄜ': 'e',
        'ㄝ': 'p',
        'ㄞ': 'h',
        'ㄟ': 'w',
        'ㄠ': 's',
        'ㄡ': 'r',
        'ㄢ': 'k',
        'ㄣ': 'd',
        'ㄤ': 'j',
        'ㄥ': 'f',
        'ㄦ': 'l',
        'ㄧ': 'i',
        'ㄧㄚ': 'x',
        'ㄧㄝ': 'p',
        'ㄧㄠ': 'n',
        'ㄧㄡ': 'b',
        'ㄧㄢ': 'm',
        'ㄧㄣ': 'v',
        'ㄧㄤ': 'x',
        'ㄧㄥ': 'g',
        'ㄨ': 'u',
        'ㄨㄚ': 'x',
        'ㄨㄛ': 'o',
        'ㄨㄞ': 'g',
        'ㄨㄟ': 'v',
        'ㄨㄢ': 't',
        'ㄨㄣ': 'z',
        'ㄨㄤ': 'c',
        'ㄨㄥ': 'l',
        'ㄩ': 'y',
        'ㄩㄝ': 'q',
        'ㄩㄢ': 'k',
        'ㄩㄣ': 'd',
        'ㄩㄥ': 'f',  # l
    }

    fake_yun={
        'ㄓ': 'a',
        'ㄔ': 'v',
        'ㄕ': 'o',
        'ㄖ': 'r',
        'ㄗ': 'z',
        'ㄘ': 'c',
        'ㄙ': 's',
    }
    zero_sheng={
        'ㄧ': 'i',
        'ㄨ': 'u',
        'ㄩ': 'y',
        'ㄚ': 'a',
        'ㄛ': 'o',
        'ㄜ': 'e',
        'ㄝ': 'p',
        'ㄞ': 'h',
        'ㄟ': 'w',
        'ㄠ': 's',
        'ㄡ': 'r',
        'ㄢ': 'k',
        'ㄣ': 'd',
        'ㄤ': 'j',
        'ㄥ': 'f',
        'ㄦ': 'l',
    }
    p = c.strip('ˊˇˋ˙')
    if len(p)==1:  # 虛韻母：ㄓㄔㄕㄖ　ㄗㄘ厶 這些可以獨存的聲母（其實是韻母省略）要多打一個虛韻母「ㄭ」在後，ㄭ放在I鍵上，用 emoji: 😬 表示，因爲發音時嘴形類似。
        if p in fake_yun.keys():
            return 'i'+table[p]
        elif p in zero_sheng.keys():
            return 'e'+table[p]
        else:
            raise ValueError
    else:
        return table[p[:1]]+table[p[1:]]

with open('hsbdmj.txt', 'r') as f:
    for line in f:
        p = pinyin(line, errors='ignore', style=Style.BOPOMOFO)
        for ch in p:
            c = ch[0]
            # print(c, end=' ')
            # print(xiaohe(c), end='')
            # print(daqian(c), end=' ')
            print(shuangmabopomofo(c), end='')