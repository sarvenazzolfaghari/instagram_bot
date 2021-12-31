from selenium import webdriver
import time

username = '_nature_in_pic'
password = '28082808'
tag = 'designer'
count = 3

driver = webdriver.Chrome('D:\python\MyProject\project4\chromedriver.exe')
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)

acc = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN._4Yzd2 > div > div > button.aOOlW.bIiDR')
acc.click()
time.sleep(5)

enter_username = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
enter_username.send_keys(username)
time.sleep(5)
enter_password = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
enter_password.send_keys(password)
time.sleep(5)

login_botton = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3)')
login_botton.click()

'''
time.sleep(5)
notif = driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
notif.click()
'''

time.sleep(5)
driver.get('https://www.instagram.com/explore/tags/{}/'.format(tag))

time.sleep(5)
i = 0
while i < count:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    time.sleep(5)
    post = driver.find_element_by_css_selector('#react-root > section > main > article > div.EZdmt > div > div > '
                                               'div:nth-child(2) > div:nth-child(2) > a > div > div._9AhH0')
    post.click()

    time.sleep(8)
    followt = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div > '
                                                  'div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div > div > '
                                                  'section.ltpMr.Slqrh > span.fr66n > button').click()
    time.sleep(10)
    exit_post = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.'
                                                    'qJPeX.fm1AK.TxciK.yiMZG > button > div > svg').click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
    time.sleep(0.2)

    '''
    text = followt.text
    if text == 'Follow':
        follow = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div > '
                                                     'div.Igw0E.IwRSH.eGOV_._4EzTm > div > div.UE9AK > div > header >'
                                                     ' div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button')
        follow.click()
        time.sleep(5)
        exit_post = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.'
                                                        'qJPeX.fm1AK.TxciK.yiMZG > button > div > svg').click()

    else:
        exit_post = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.'
                                                        'qJPeX.fm1AK.TxciK.yiMZG > button > div > svg').click()
'''
    i += 1
print("done :)))))))))))))))", count)
driver.close()
