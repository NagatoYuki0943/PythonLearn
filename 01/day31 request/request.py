'''
发送请求

'''

import requests


if __name__ == "__main__":
    # 参数2数据
    response = requests.get('url', params={'name':'xiaoming', 'age':15})
    # 得到结果
    response.json()

    response = requests.post('url', data={'name':'xiaoming', 'age':15})
    response.json()