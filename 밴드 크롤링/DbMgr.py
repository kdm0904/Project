import pymysql as my

class DBHelper:
    '''
    맴버변수 : 커넥션 
    '''
    conn = None
    '''
    생성자 
    '''
    def __init__(self):
        self.db_init()
    '''
    맴버 함수
    '''
    def db_init(self):
        self.conn = my.connect(
                        host='localhost',
                        user='root',
                        password='jimmy4090#',
                        db='danawa',
                        charset='utf8',
                        cursorclass=my.cursors.DictCursor )
    
    def db_free(self):
        if self.conn:
            self.conn.close()

    # 검색 키워드 가져오기 => 웹에서 검색
    def db_selectKeyword(self):
        # 커서 오픈
        # with => 닫기를 처리를 자동으로 처리해준다 => I/O 많이 사용
        rows = None
        with self.conn.cursor() as cursor:
            sql  = "select * from keyword;"
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)
        return rows
        
    def db_insertCrawlingData(self, 상품명, 가격, 평점, 리뷰수, 가격비교, keyword ):
        with self.conn.cursor() as cursor:
            sql = '''
            insert into `air` 
            (상품명, 가격, 평점, 리뷰수, 가격비교, keyword) 
            values( %s,%s,%s,%s,%s,%s)
            '''
            cursor.execute(sql, (상품명, 가격, 평점, 리뷰수, 가격비교) )
        self.conn.commit()