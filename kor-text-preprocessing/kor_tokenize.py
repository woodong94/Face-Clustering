from konlpy.tag import Mecab
from khaiii import KhaiiiApi

from clean_text import clean_text


def tokenize_space(sentence):
    '''Return cleaned and tokenized sentences

    Example:
        >>> s = '1987 본 문 대통령.."그런다고 바뀌나? 함께 하면 바뀐다"'
        >>> tokenize_clean_text(s)
        ['1987', '본', '문', '대통령', '그런다고', '바뀌나', '함께', '하면', '바뀐다']
    '''
    sentence = clean_text(sentence)
    sent_tokened = [i for i in sentence.split(' ') if len(i) > 0]
    return sent_tokened


def tokenize_mecab(sentence):
    mecab = Mecab()

    sentence = clean_text(sentence)
    tagged = mecab.pos(sentence)
    result = []
    for word, tag in tagged:
        #if (tag in ['NNG', 'NNP', 'VV', 'VA']):  # 일반명사, 고유명사, 동사, 형용사 사용
        result.append(word)
    return result


def tokenize_khaiii(sentence):
    khaiii = KhaiiiApi()

    tagged = []
    for word in khaiii.analyze(sentence):
        mos = [(m.lex, m.tag) for m in word.morphs]
        tagged.extend(mos)

    result = []
    for word, tag in tagged:
        result.append(word)

    return result

if __name__ == '__main__':
    test = "WP는 자신이 코로나 감염증에 ^^^걸렸지만 회복했다고 믿는 이 현상을 해결할 방법으로 ‘항체 검사’를 지목했다."

    print("공백 단위 토큰화 결과 : {}".format(tokenize_space(test)))
    print("mecab 결과 : {}".format(tokenize_mecab(test)))
    print("khaiii 결과 : {}".format(tokenize_khaiii(test)))