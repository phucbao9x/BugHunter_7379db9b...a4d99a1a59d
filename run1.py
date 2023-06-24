from config import WebBase
import config
from random import randint
from poc import POC_ORDERS, BeautifulSoup

end = config.base1end
start = config.base1start

f = open('jjt.csv', 'wb')

f.write(b'name;address;phone;id;money;time')

for i in range(start, end+1):
    link = WebBase.join(config.url, config.base1, i)

    dataCrawling = config.requests.get(
        link, headers=config.headers, cookies=config.cookies
    )
    print(f'>> Link: {link} status: {dataCrawling.status_code}', end=" ")
    if dataCrawling.status_code != 404:
        content = dataCrawling.content.decode('utf-8')
        HTMLDOM = BeautifulSoup(content, "html5lib")
        data = POC_ORDERS(HTMLDOM)
        # Get all
        name = data['name']
        address = data['address']
        phone = data['phone']
        id = i
        money = data['money']
        time = data['time']
        data = f'\n{name.decode()};{address.decode()};{phone.decode()};{id};{money.decode()};{time.decode()}'
        f.write(data.encode())
    print('Success!!')
f.close()