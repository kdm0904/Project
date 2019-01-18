class ItemInfo:
    상품명 = ''
    가격 = ''
    평점 = ''
    리뷰수 = ''
    가격비교 = ''

    #생성자
    def __init__(self, 상품명, 가격, 평점, 리뷰수, 가격비교):
        self.상품명 = 상품명
        self.가격 = 가격
        self.평점 = 평점
        self.리뷰수 = 리뷰수
        self.가격비교 = 가격비교