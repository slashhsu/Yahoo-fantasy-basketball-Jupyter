import requests
import selenium
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

Chrome_driver_path = '/Users/xuhanling/Desktop/申請資料/work application/Yahoo fantasy/chromedriver' #指定到您放置chromedriver.exe的位置
web = 'https://login.yahoo.com/config/login?.src=fantasy&specId=usernameRegWithName&.intl=us&.lang=en-US&.done=https://basketball.fantasysports.yahoo.com/' #Yahoo Fantasy登入頁面
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"') #建議可以點選F12看request header的項目
driver = webdriver.Chrome(service=Service(Chrome_driver_path), options=chrome_options)  #打開模擬的Chrome瀏覽器
driver.maximize_window() ###最大化視窗，因為我發現某些情況下，較小的視窗會導致往下移動的JS沒有辦法執行。

driver.get(web) ###開始進入登入頁面

# Wait for the username field to be clickable, then enter the username
elem_user = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, 'username'))
)
elem_user.clear()
elem_user.send_keys('sam5348911@yahoo.com.tw')
driver.find_element(By.ID, 'login-signin').click()
time.sleep(5)
# Wait for the password field to be clickable, then enter the password
elem_pass = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'login-passwd'))
)
elem_pass.send_keys('Sh5348911!')
driver.find_element(By.ID, 'login-signin').click()
time.sleep(5)


web2 = 'https://basketball.fantasysports.yahoo.com/nba/30001/matchup?week=1' #要爬取matchup分數的地方
driver.get(web2)

for i in range(0,10):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') #到達網頁後要滾輪持續往下滑，才會出現matchup分數欄位
    time.sleep(1)
    
soup = BeautifulSoup(driver.page_source, "html.parser")  #把撈到的頁面丟給BeautifulSoup解析
pages = soup.find_all('div',class_='Ta-c Js-hidden') #找網址
names = soup.find_all('a',class_='F-link') #找隊名

soup
names
pages
###先搞定隊名
names2=[]
for n in names[38:52]:
    names2.append(n.text)

names2
###搞定對戰連結
target_pages=[]
for p in pages:
    target_pages.append(p.a['href'])
    
target_pages2 = []
for p2 in target_pages:
    target_pages2.append('https://basketball.fantasysports.yahoo.com'+p2)
target_pages2
###撈取對戰分數，左半部與右半部各抓一次。
lg1=[]
lg2=[]

for p3 in target_pages2:
    driver.get(p3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    score1 = soup.find_all('td',class_='Ta-c')
    time.sleep(5)
    
    for i in score1[0:14]:
        lg1.append(i.text)
    
    for i in score1[15:29]:
        lg2.append(i.text)

lg1
lg2
### 依序把抓到的欄位填入pandas中
# Calculate the step size for slicing based on the pattern in your example
step_size = 14
lg1_index = 0  # Initial index for lg1
lg2_index = 0  # Initial index for lg2
contest_index = 14  # Initial index for lg2

# Initialize an empty dictionary to collect the data
data = {}

# Loop through the list of team names
for i, name in enumerate(names2):
    # Check if the index is even or odd and slice from lg1 or lg2 accordingly
    if i % 2 == 0:  # if index is even, slice from lg1
        data[name] = lg1[lg1_index:lg1_index + contest_index]
        lg1_index += step_size
    else:  # if index is odd, slice from lg2
        data[name] = lg2[lg2_index:lg2_index + contest_index]
        lg2_index += step_size

len(data)
data


# Create the DataFrame from the dictionary
df1 = pd.DataFrame(data)
df1['contest'] =['FGM/A*','FG%','FGM/A*','FT%','3PTM','3PTA*','3PT%','PTS','REB','AST','ST','BLK','TO','DD']
df1 = df1[['contest','再拿胖虎我就刪遊戲', '大KD', '\U0001fae0\U0001fae0\U0001fae0', 'Suns', 'Wendy’s Burger', '你先親我一下', '鉛筆', "振德's Tip-Top Team", '創建BOMB', '啾啾啾啾啾啾啾啾', "小玖's Choice Team", 'E了個大摸', '宇宙昆', '顏立明']]

df1
### 畫畫讓圖表數據更美觀
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from math import pi

# Drop the unwanted rows
df2 = df1.drop([0, 2])
# Convert all score columns to float
df2.iloc[:, 1:] = df2.iloc[:, 1:].astype(float)
df2
df3
df3=df3.reset_index()
df3=df2.T

# Set the first row as the header
df3.columns = df3.iloc[0]

# Drop the first row now that its values are set as column names
df3 = df3.drop(df3.index[0])

# Reset the index to renumber the rows appropriately
df3 = df3.reset_index(drop=True)

transposed_df = df2.T 
transposed_df
transposed_df = transposed_df.reset_index()
transposed_df1 = transposed_df.set_index('contest')

# Set the first row as the header
transposed_df.columns = transposed_df.iloc[0]

# Drop the first row now that its values are set as column names
transposed_df = transposed_df.drop(transposed_df.index[0])

# Reset the index to renumber the rows appropriately
transposed_df = transposed_df.reset_index(drop=True)
# Drop non-numeric columns first
df_numeric = transposed_df.drop(['contest'], axis=1)
df_numeric
df_numeric.set_index('contest', inplace=True)
df_numeric=df_numeric.T
# Transpose the DataFrame to make manipulation easier
df_numeric = df_numeric.T

# Set the 'contest' row as the new index
df_numeric.index = df_numeric.loc['contest']



# Drop the now redundant 'contest' row
df_numeric = df_numeric.drop('contest')

# Transpose the DataFrame back to its original orientation
df_numeric = df_numeric.T

print(df_numeric.index)



# Apply Z-score normalization
for col in df_numeric:
    df_numeric[col] = (df_numeric[col] - df_numeric[col].min()) / (df_numeric[col].max() - df_numeric[col].min())
df3
# If you want to reattach the non-numeric columns
df_normalized_z_score = df_normalized_z_score.drop(['index'], axis=1)
df_numeric['contest'] = df3['contest']

df_normalized_z_score
df4 = df3.drop(['index'], axis=1)

# Bar Chart (Grouped)
df_numeric.plot(kind='bar', figsize=(12, 6), width=0.8)
plt.title('Grouped Bar Chart of Team Performance')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


