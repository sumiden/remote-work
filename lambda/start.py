from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert 
import time

def lambda_handler(event, context):
    
   # if __name__ == "__main__":

        ## Seleniumが使用するWebDriver作成時のオプションを作る
        options = webdriver.ChromeOptions()
        ## オプションのバイナリロケーションにLayerで用意したheadless-chromiumのパスを指定
        options.binary_location = '/opt/headless-chrome/headless-chromium'
        ## オプションにヘッドレスモードで実行させる記述を書く
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox') # required when running as a root-user. Otherwise you would get no sand-box errors
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        ## Seleniumが使用するWebDriverを作成
        driver = webdriver.Chrome(
            ## Layerで用意したchromedriverのパスを指定
            '/opt/headless-chrome/chromedriver',
            options = options
        )
    
        driver.get('https://jisou.it-builder.jp/app/zaseki/jisou_input')
        
        # 氏名コード入力
        driver.implicitly_wait(5)
        searchElement = driver.find_element_by_id("input_employee_code")
        searchElement.send_keys('5552256')    
        driver.find_element_by_id('btnSave_2').click()
        
        # テレワーク開始クリック
        driver.implicitly_wait(5)
        driver.find_element_by_id('btnNext_1').click()
        
        # 登録クリック
        driver.implicitly_wait(5)
        driver.find_element_by_id('btnSave_2').click()
        
        # アラート処理
        driver.implicitly_wait(5)
        alert = driver.switch_to.alert
        alert.accept()
    
        time.sleep(2)
        driver.quit()
        
