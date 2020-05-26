import re

def remove_brackets(string, left_paren_type, right_paren_type):
    '''Remove brackets (parentheses) and their contents within a string
    Args :
        left_paren_type = '[','(' etc
        right_paren_type = ']', ')' etc
    Example:
        >>> s = '[abababab] kdk[sbsbsb]dkdk'
        >>> remove_brackets(s,'[',']')
        'kdkdkdk'
    '''
    # 여러 괄호 처리
    while (left_paren_type in string):
        # 괄호 있다면
        if right_paren_type in string:
            ## 괄호 시작과 끝 index 저장
            parenthesis_index = []

            for index, char in enumerate(string):
                # print(index,char)
                if char == left_paren_type:
                    parenthesis_index.append(index)
                elif char == right_paren_type:
                    parenthesis_index.append(index)
                else:
                    pass

            ## 괄호 시작과 끝 index 저장
            start = parenthesis_index[0]
            end = parenthesis_index[1]

            substring_to_delete = string[start:end + 1]
            string = string.replace(substring_to_delete, '').strip()

    return string


def clean_text(sentence):
    '''Return cleaned sentences

    Example:
        >>> s = '박세용 기자(psy05@sbs.co.kr)☞ [SBS 2017 대선] 나는 이런 대통령을 원한다!☞'
        >>> clean_text(s)
        '박세용 기자 나는 이런 대통령을 원한다'
    '''
    # bracket과 내부 내용 제거
    sentence = remove_brackets(sentence, '[', ']')
    sentence = remove_brackets(sentence, '(', ')')
    sentence = remove_brackets(sentence, '{', '}')
    # 특수 문자 제거
    sent_clean = re.sub('[-■=+,#/\?:“”^$*\"※~&%ㆍ☞!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', sentence)
    # multiple space 제거
    sent_clean = re.sub(' +', ' ', sent_clean)
    sent_clean = " ".join(sent_clean.split())
    sent_clean = sent_clean.strip()

    return sent_clean

if __name__ == '__main__':
    print(clean_text('''
    WP는 자신이 코로나 감염증에 ^^^걸렸지만 회복했다고 믿는 이 현상을 해결할 방법으로 ‘항체 검사’를 지목했다. 
    실제로 코로나바이러스 항체가 자신의 몸 안###에 있는지 검사해봐야, 
    자신의 믿음이 옳은 것인지 그른 것인지를@@@ 알 수 있다는 것이다. 
    그러나 코로나 감염증에 걸렸다가 %%%완치 판정을 받더라도 재확진 판정을 받는 경우 등이 있어 전문가들은 항체가 있더라도 
    100% 코로나 감염증에 다시 걸리지 않는 것은 아니라고 지적한다.

    [이옥진 기자 june12@chosun.com]
    <Copyrights ⓒ 조선일보 & chosun.com, 무단 전재 및 재배포 금지>

    '''))