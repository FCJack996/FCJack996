import requests
print('nihao')

url = 'https://www.baidu.com'
page_text = requests.get(url=url).text
print(page_text)
