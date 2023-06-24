from bs4 import BeautifulSoup
import config

def POC_FindName(HTMLDOM) -> bytes:
    classTextUpperCase = HTMLDOM.find_all(
        attrs={
            'class' : config.class1
        }
    )
    for i in classTextUpperCase:
        try:
            __tmp_htmldom = BeautifulSoup(i.prettify(), 'html5lib')
            return __tmp_htmldom.find('b').contents[0].replace('\n', '').replace('\t', '').strip().encode()
        except:
            pass
    return b''

def POC_FindAddressAndPhone(HTMLDOM) -> set[bytes]:
    classTextUpperCase = HTMLDOM.find_all(
        attrs={
            'class' : config.class2
        }
    )
    phone = None
    address = None
    for tag in classTextUpperCase:
        __tmp = BeautifulSoup(tag.prettify(), 'html5lib')
        if __tmp.find('i', attrs={
            'class' : config.class3
        }):
            address = __tmp.find('span').contents[0].replace('\n', '').replace('\t', '').strip().encode()
        elif __tmp.find('i', attrs={
            'class' : config.class4
        }):
            phone = __tmp.find('span').contents[0].replace('\n', '').replace('\t', '').strip().encode()
    return address, phone

def POC_FindTotalMoney(HTMLDOM) -> bytes:
    for i in HTMLDOM.find_all(
        attrs={
            'class' : config.class5
        }
    ):
        try:
            __tmp_htmldom_content = i.contents[0].replace('\n', '').replace('\t', '').strip()
            if __tmp_htmldom_content.encode() != b'T\xe1\xbb\x95ng ti\xe1\xbb\x81n': return __tmp_htmldom_content.encode()
        except: pass
    return b''

def POC_FindTimeBuy(HTMLDOM):
    try:
        __tmp = BeautifulSoup(HTMLDOM.find_all(attrs={ 'class' : config.class6 })[0].prettify(), 'html5lib')
        __time : str= __tmp.find('span', attrs={'class': config.class7}).contents[0].replace('\n', '').replace('\t', '').strip()
        while __time.count('  ') > 0: __time = __time.replace('  ', ' ')
        __time = __time.replace(' ', '~')
        return __time.encode()
    except:
        return b''
    
def POC_ORDERS(HTMLDOM):
    add, phone = POC_FindAddressAndPhone(HTMLDOM)
    money = POC_FindTotalMoney(HTMLDOM)
    time = POC_FindTimeBuy(HTMLDOM)
    return {
        'name' : POC_FindName(HTMLDOM),
        'address' : add,
        'phone' : phone,
        'money' : money,
        'time' : time,
    }