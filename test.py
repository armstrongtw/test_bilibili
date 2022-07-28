# -*- coding = utf-8 -*-

import numpy as np
import pandas as pd

from urllib.request import urlopen
import requests

url = 'http://www.baidu.com'
r = urlopen(url)

# 添加headers
# headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
# r = requests.get('https://www.baidu.com/', headers=headers)

print(r)
# print(r.status_code)
with open('mybaidu.html', mode='w') as f:
    f.write(r.read().decode('utf-8'))
