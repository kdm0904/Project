import time
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
# 명시적 대기를 위해 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Item import ItemInfo

# 사전에 필요한 정보를 로드 => 디비혹스 쉘, 베치 파일에서 인자로 받아서 세팅
main_url = 'http://www.danawa.com/' 
keyword  = '공기청정기'
item_list = []


# 윈도우용
driver = wd.Chrome(executable_path='chromedriver.exe')

# 사이트 접속 (get)
driver.get(main_url)

# 자료 검색
driver.find_element_by_id('AKCSearch').send_keys(keyword)
driver.find_element_by_css_selector('button.btn_search_submit').click()


for page in range(1, 3):
    try:
        # 자바스크립트 구동하기
        driver.execute_script("getPage(%s); return false;" % page)
        time.sleep(1)
        print("%s 페이지 이동" % page)
        #################################
        # 상품명, 가격, 별점, 리뷰수
        prod_item = driver.find_elements_by_css_selector('.product_list>li')

        for li in prod_item:
            print ('상품명', li.find_element_by_css_selector('.prod_main_info>.prod_info>.prod_name>a').text)
            print ('가격', li.find_element_by_css_selector('.prod_main_info>.prod_pricelist>ul>li>.price_sect>a').text)
            print ('평점', li.find_element_by_css_selector('.point_num').text)
            print ('리뷰수', li.find_element_by_css_selector('.cnt_opinion>a').text)
            print ('가격비교', li.find_element_by_css_selector('.chk_sect').text)

        # 데이터 모음
            obj = ItemInfo( 
                li.find_element_by_css_selector('.prod_main_info>.prod_info>.prod_name>a').text,
                li.find_element_by_css_selector('.prod_main_info>.prod_pricelist>ul>li>.price_sect>a').text,
                li.find_element_by_css_selector('.point_num').text,
                li.find_element_by_css_selector('.cnt_opinion>a').text,
                li.find_element_by_css_selector('.chk_sect').text
            )
            item_list.append(obj)

    except Exception as e1:
        pass

print ( item_list, len(item_list))

item_list.to_csv('다나와_크롤링결과_utf8.csv', encoding = 'UTF-8')