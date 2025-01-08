from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from insert import Inserting

class StoryBerries:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--disable-extensions")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        # options.add_argument('--disable-images')  
        options.add_argument("--start-maximized")
        options.add_argument('--enable-unsafe-swiftshader')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-software-rasterizer")
        

        self.service = Service("D:\Hackaton\\third_hackathon\pars_story\chromedriver-win64\chromedriver.exe")
        self.options = options
        self.driver = None
        self.wait = None
        self.insert = Inserting()
    def setup_driver(self):
        self.driver = webdriver.Chrome(options=self.options, service=self.service)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.wait = WebDriverWait(self.driver, 8)

    def open_url(self, url):
        self.driver.get(url)
    
    def close_driver(self):
        if self.driver:
            self.driver.quit()


    def pars_story(self, url):
        insert_data = {}
        self.setup_driver()                         

        try:
            self.open_url(url=url)
            category = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/header/h1').get_attribute('textContent')
            insert_data['category_name'] = category
            try: 
                pages_bar = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/div/div/ul')
                count_page= len(pages_bar.find_elements(By.TAG_NAME, 'li'))
            except: 
                count_page = 2

            for index in range(1, count_page):  
                cards_fairy_tail = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/section/div/div/div').find_elements(By.CSS_SELECTOR, '.column.post-column.small-mb-2.large-mb-4.hor-sep-b')
                for sub_index in range(1, len(cards_fairy_tail)+1):
                    '''Парсинг данных сказок и категорию'''
                    try:
                        initial_picture = self.wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div/div[2]/section/div/div/div/div[{sub_index}]/article/figure/a/img'))).get_attribute('src')
                        insert_data['initial_picture']= initial_picture
                    except:
                        continue
                    age_category = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/section/div/div/div/div[{sub_index}]/article/div/div[1]/a[2]').get_attribute('textContent')
                    insert_data['age_category']= age_category[4::]
                    title_for_link=self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/section/div/div/div/div[{sub_index}]/article/div/h2/a')
                    title = title_for_link.get_attribute('textContent')
                    insert_data['title'] = title
                    subtitle =self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/section/div/div/div/div[{sub_index}]/article/div/div[2]/p').get_attribute('textContent')
                    insert_data['subtitle'] = subtitle

                    '''Переход к странице сказки'''
                    link_for_fairy_tail_page = title_for_link.get_attribute('href')
                    self.driver.execute_script(f"window.open('{link_for_fairy_tail_page}','_blank');")
                    self.driver.switch_to.window(self.driver.window_handles[1])

                    '''Парсит весь текст и количеству читаемости'''
                    story_reads = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/article/div/div[1]/div[1]/span[3]').get_attribute('textContent')
                    insert_data['story_reads']=story_reads
                    texts = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/article/div/div[1]')
                    text_filter_by_p = texts.find_elements(By.TAG_NAME, 'p')
                    text = ''
                    for i in text_filter_by_p:
                        text += i + '/n'
                    
                    insert_data['text'] = text

                    '''Переход к странице автора'''
                    author_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div/article/footer/div[2]/div[3]/div/span/span/a'))).get_attribute('href')
                    self.driver.execute_script(f"window.open('{author_link}','_blank');")
                    self.driver.switch_to.window(self.driver.window_handles[2])

                    '''Парсинг страницы автора'''
                    author_photo = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div[1]/div/header/img').get_attribute('src')
                    insert_data['author_photo'] = author_photo
                    author_name = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div[1]/div/header/h1/span').get_attribute('textContent')
                    insert_data['author_name'] = author_name
                    author_bio = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div[1]/div/div[1]/div/div/p').get_attribute('textContent')
                    insert_data['author_bio'] = author_bio
                    self.insert.insert_stories_category(insert_data)

                    '''Назад к главному меню'''
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    time.sleep(1)
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                try:
                    next_page = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/nav/div/div/ul/li[{index}]/a')
                    next_page.click()
                except:
                    pass

            
        except Exception as e:
                print(f"Ошибка при обработке песен автора: {e}")


    def run(self):
        result = self.pars_story(url='https://www.storyberries.com/category/fairy-tales/famous-fairy-tales/')
        urls = [
            'https://www.storyberries.com/category/fairy-tales/russian-fairy-tales/',
            'https://www.storyberries.com/category/fairy-tales/scottish-fairy-tales/',
            'https://www.storyberries.com/category/fairy-tales/japanese-fairy-tales/',
            'https://www.storyberries.com/category/fairy-tales/aesops-fables/',
            'https://www.storyberries.com/category/fairy-tales/norse-myths-and-fairy-tales/',
            'https://www.storyberries.com/category/fairy-tales/oscar-wilde-fairy-tales/',
            'https://www.storyberries.com/category/fairy-tales/chinese-fairy-tales/',
            'https://www.storyberries.com/category/fairy-tales/french-fairy-tales/',
            'https://www.storyberries.com/category/fairy-tales/english-fairy-tales/',
            'https://www.storyberries.com/category/fairy-tales/hans-christian-andersen-fairy-tales/',
            'https://www.storyberries.com/category/fairy-tales/brothers-grimm-fairy-tales/',
            'https://www.storyberries.com/category/fairy-tales/famous-fairy-tales/',
        ]
        return result


if __name__ == "__main__":
    news = StoryBerries()
    result = news.run()
    print(result)
