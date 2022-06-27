# %%
from selenium import webdriver
import time 
import requests
from selenium.webdriver.chrome.options import Options

# %%
# 西武線URL
option = Options()
option.add_argument('--headless')
driver=webdriver.Chrome(options=option)
url='https://www.seiburailway.jp/railwayinfo/' 
driver.get(url)
time.sleep(2)

# %%
# 西武線運行情報
elem=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/main/div/div/div/div/div[2]/div/div/div/div/div')
elem_text=elem.text
train_info=elem_text.replace('\n', ',')
driver.quit()

# %%
# line token
def line(me):
    line_notify_token = "#トークン"
    line_notify_api='https://notify-api.line.me/api/notify'
    message = '\n'+me
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)

# %%
# 西武線情報LINEテキスト
text = '西武線の運行情報\n>'+ train_info
line(text)

# %%



