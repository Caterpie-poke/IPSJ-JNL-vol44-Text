import re


def regularize(txt):
    txt = re.sub(r'[ 　\t\n]', '', txt)
    txt = re.sub(r'[.。．]', '。\n', txt)
    txt = re.sub(r'[,、，]', '、', txt)
    txt = re.sub(r'([†]|(\([0-9a-zA-Z:]*\))+)', '\n', txt)
    txt = re.sub(r'\[[ 　]*[0-9]*[ 　]*\]', '', txt)
    txt = re.sub(r'^。\n', '', txt)  # 効かない（ToT)
    return txt


def replace_dakuten(s,pos):
    daku = {
        'か': 'が',
        'き': 'ぎ',
        'く': 'ぐ',
        'け': 'げ',
        'こ': 'ご',
        'さ': 'ざ',
        'し': 'じ',
        'す': 'ず',
        'せ': 'ぜ',
        'そ': 'ぞ',
        'た': 'だ',
        'ち': 'ぢ',
        'つ': 'づ',
        'て': 'で',
        'と': 'ど',
        'は': 'ば',
        'ひ': 'び',
        'ふ': 'ぶ',
        'へ': 'べ',
        'ほ': 'ぼ',
        'カ': 'ガ',
        'キ': 'ギ',
        'ク': 'グ',
        'ケ': 'ゲ',
        'コ': 'ゴ',
        'サ': 'ザ',
        'シ': 'ジ',
        'ス': 'ズ',
        'セ': 'ゼ',
        'ソ': 'ゾ',
        'タ': 'ダ',
        'チ': 'ヂ',
        'ツ': 'ヅ',
        'テ': 'デ',
        'ト': 'ド',
        'ハ': 'バ',
        'ヒ': 'ビ',
        'フ': 'ブ',
        'ヘ': 'ベ',
        'ホ': 'ボ',
    }
    s.find(r'[゛゜]')

def main():
    path = './01/IPSJ-JNL4401001.txt'
    with open(path, 'r', encoding='utf_16_le') as f_in:
        s = f_in.read()
        s = re.sub(r'[゙]', '゛', s)  # 濁点の全角化
        s = re.sub(r'[゚]', '゜', s)  # 半濁点の全角化
        s = re.sub(r'[.。．]', '。', s)
        s = re.sub(r'[,、，]', '、', s)
        with open('./temp.txt', 'w', encoding='utf-8') as f_out:
            f_out.write(s)


if __name__ == "__main__":
    main()
