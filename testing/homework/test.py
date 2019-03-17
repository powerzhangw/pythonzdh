# -*- coding: UTF-8 -*-
import requests

session = requests.session()
session.headers[
    'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
session.headers['Content-type'] = 'application/x-www-form-urlencoded'
# print(res.text)
# session.headers['x-udid'] = 'ACCha1aUqA6PTsEjcylWGx8HHM3feFPytFg=|1544611343'
res = session.post('https://www.zhihu.com/udid', data='')
print(res.text)
res = session.get('http://www.zhihu.com/api/v3/oauth/captcha?lang=en')
print(res.text)
session.headers['x-zse-83'] = '3_1.1'
print(session.cookies)
print(session.headers)
res = session.post('https://www.zhihu.com/api/v3/oauth/sign_in',
                   data='ToOk0KPwMtBtNXtzltBlMKpxBduq0PQzppOk0KPwMtBtNX0x1hBlMK6z0p9a01AzwLAlMK-pNsauCle2hdQwQGohEobaMc8k-9uxA-dyUXeuD6dpisaxMxP2NlfuKx8k1OQz82LkQcraOs8k1cbkKG5xU6v4NsqxsdAzMLP1PxNa058lw2bl6P_kToQvKkuxwpQw80_l0xQvTobl-cNw6dKk0xbbRoQwmkepNKpxMtvr6TQxolBlMK6w02RdP6uypDBjHxPwclbf0lA1kXQ1QGohSwr_Ogrkj18lOOolLo9a0_vzwpR10ptyOxNa0oA1u2R1N6d1clbf0-v3lXd2I601BxNa0_8k1-8lLCoxLcQb00rwigemAD_lScbuQwNwmwux8DKwclbf90QvlTuxDtPw')
print(res.text)
