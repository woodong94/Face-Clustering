import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud

'''(주의) python 파일명을 wordcloud.py 으로 저장하면 import 에러가 발생한다'''

def generate_circular_wordcloud(text):
    """Returns circle shape Word Cloud
    Example:
        text(str): "데이터 데이터 분석 프로젝트" 처럼 단일 스트링 ..
    """

    n_size = 1000

    # mask circle
    x, y = np.ogrid[:n_size, :n_size]
    mask = (x - (n_size/2)) ** 2 + (y - (n_size/2)) ** 2 > (n_size/2*0.96) ** 2
    circle_mask = 255 * mask.astype(int)

    # word cloud
    wordcloud = WordCloud(max_font_size=200,
                          font_path='/Library/Fonts/NanumSquareExtraBold.ttf',
                          background_color="white",
                          width=n_size,
                          height=n_size,
                          max_words=100,
                          mask=circle_mask,  # circular mask
                          colormap='Paired')

    wordcloud.generate(text)

    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.show()

if __name__ == '__main__':
    # 아무 뉴스 기사 긁어옴
    generate_circular_wordcloud('''
    탈루의심사례 부동산 취득자금 중 70%가 '빚''

    미성년 자녀, 부모 돈으로 서울·제주 주택 여러 채 매입도

    (세종=연합뉴스) 신호경 기자 = 고가 아파트를 샀거나 비싼 전세를 얻은 사람들 가운데 편법 증여 등이 의심되는 500여명이 강도 높은 세무조사를 받는다.

    국세청은 최근 부동산 거래 과정에서 자금 출처가 분명하지 않고 탈세 혐의가 확인된 517명에 대해 세무조사에 들어갔다고 7일 밝혔다.

    이번 대상에는 우선 국세청의 자체 조사 결과, 가족 등으로부터 편법 증여받은 자금으로 서울·수도권 등의 고가 아파트를 사거나 비싼 전세를 얻은 것으로 드러난 146명이 포함됐다.

    아울러 국토교통부·행정안전부·금융위원회 등 정부 부처와 지방자치단체들이 '서울 부동산 거래 신고내용 합동조사' 후 세 차례에 걸쳐 국세청에 통보한 2천여건의 탈세의심자료(1차 532건·2차 670건·3차 835건)를 바탕으로 선정된 탈루 혐의자 279명도 조사 대상이다.
    ''')