import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 设置代理
proxy = '220.191.64.149'
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--proxy-server = http://' + proxy)

broswer = webdriver.Chrome()
# 测试代理
broswer.get('http://httpbin.org/get')

# 输入即将收到短信的手机号码
tel = 18350137468  # guo


# tel = 13777836911


# 定位,并输入手机号码
def tel_num_try(input_tel):
    print("【目前状态】：\n定位号码输入框,并输入手机号码...")
    try:
        print("使用id定位中...")
        bot1 = broswer.find_element_by_id(input_tel)
        bot1.send_keys(tel)
    except:
        print("【id定位失败！】：\n使用class_name定位中...")
        bots2 = broswer.find_element(By.CLASS_NAME, input_tel)
        time.sleep(1)
        bots2.send_keys(tel)


# 定位并点击(方案1)
def tel_power_try_child1(btn):
    print("【当前状态】:定位元素，点击鼠标..")
    try:
        print("使用id定位中...")
        bot3 = broswer.find_element_by_id(btn)
        # bot1 = broswer.find_element_by_css_selector(btn)
        bot3.click()
        time.sleep(1)
    except Exception as e:
        print("【id定位失败！】\n 使用by_xpath定位中...")
        bots4 = broswer.find_element_by_xpath(btn)
        bots4.click()
        time.sleep(1)


# 定位并点击(方案2)
def tel_power_try_child2(btn):
    print("【当前状态】:定位元素，点击鼠标..")
    try:
        print("使用class定位中...")
        bot3 = broswer.find_element(By.CLASS_NAME, btn)
        # bot1 = broswer.find_element_by_css_selector(btn)
        bot3.click()
        time.sleep(1)
    except:
        print("【id定位失败！】\n使用CSS_SELECTOR定位中...")
        bots4 = broswer.find_element(By.CSS_SELECTOR, btn)
        bots4.click()
        time.sleep(1)


# 调用两个点击方案
def tel_power_try(btn):
    try:
        tel_power_try_child1(btn)
    except:
        tel_power_try_child2(btn)


# 模板：两步获取验证码：手机号定位，验证码定位；
def tel_get_2(url, input_tel, btn):
    # 获取地址
    broswer.get(url)
    time.sleep(1)
    # 定位手机号输入
    tel_num_try(input_tel)
    time.sleep(1)
    # 定位"获取验证码"按钮
    tel_power_try(btn)
    # broswer.close()


# 模板：三步获取验证码：into：登录定位，input_tel：手机号定位，btn：验证码定位；
def tel_get_3(url, into, input_tel, btn):
    # 获取地址
    broswer.get(url)
    time.sleep(3)
    tel_power_try(into)

    # 定位手机号输入
    tel_num_try(input_tel)

    # 定位"获取验证码"按钮
    tel_power_try(btn)


def tel_get_4(url, into, into2, input_tel, btn):
    # 获取地址
    broswer.get(url)
    tel_power_try(into)

    tel_power_try(into2)

    # 定位手机号输入
    tel_num_try(input_tel)

    # 定位"获取验证码"按钮
    tel_power_try(btn)


# # 模板：三步获取验证码：登录定位，手机号定位，验证码定位；
# def tel_get_k3(url, into, input_tel, btn):
#     # 获取地址
#     broswer.get(url)
#     # 定位手机号输入
#     tel_num_try(input_tel)
#     tel_power_try(into)
#
#     # 定位"获取验证码"按钮
#     tel_power_try(btn)

# 模板：三步获取验证码：手机定位，滑动验证码检验（变速滑动）、验证码定位；（待续）

# 模板：三步获取验证码：手机定位，图像文字识别检验（涉及太广）、验证码定位；（待续）

# 短信轰炸机：感觉自己在犯法的边缘不断试探
class Spider_tel():
    def __init__(self):
        pass

    def TongCheng_com(self):
        url = "https://passport.58.com/reg/?path=https%3A//gz.58.com/&PGTID=0d100000-0000-33f9-63ec-9ca2641f5e25&ClickID=3"
        input_tel = 'mask_body_item_phonenum'
        btn = 'mask_body_item_getcode'
        print('【TongCheng_com】')
        tel_get_2(url, input_tel, btn)
        # # 控制滑块移动
        # try:
        #     slider_element = broswer.find_element_by_css_selector("#id")
        #     if slider_element:
        #         action_chains = ActionChains(broswer)
        #         action_chains.drag_and_drop_by_offset(slider_element, 60, 0).perform()
        # except:
        #     pass

    # def Guazi_com(self):
    #     url = "https://www.guazi.com/qinhuangdao/dazhong/"
    #     into = 'js-login-new'
    #     input_tel = "phone-login-input"
    #     btn = '.get-code'
    #     print('【Guazi_com】')
    #     tel_get_3(url, into, input_tel, btn)

    def JianShu(self):
        url = "https://www.jianshu.com/sign_up"
        input_tel = 'user_mobile_number'
        btn = 'send_code'
        print('【JianShu】')
        tel_get_2(url, input_tel, btn)

    def SuNingYiGou(self):
        url = "https://reg.suning.com/person.do?myTargetUrl=https%3A%2F%2Fwww.suning.com%2F%3Fsafp%3Dd488778a.uzD.0.acf325284e"
        url='https://passport.suning.com/ids/login?service=https%3A%2F%2Freg.suning.com%2Fauth%3FtargetUrl%3Dhttp%253A%252F%252Fwww.suning.com&method=GET'
        broswer.get(url)
        time.sleep(1)
        into = '.tab-item'
        # print(broswer.find_element_by_css_selector(into).get_attribute('innerHTML'))
        ele=broswer.find_element_by_css_selector('[class="tab-item on"]')
        # print(ele.get_attribute('href'))
        time.sleep(2)
        # js = f"window.open('{ele.get_attribute('href')}')"
        # js = f"{ele.get_attribute('href')}"
        # broswer.execute_script(js)
        # ActionChains(broswer).move_to_element(ele).click().perform()
        broswer.execute_script("arguments[0].click();", ele)
        # time.sleep(1)
        # into2='login-switch code-login'
        # broswer.find_element_by_css_selector(into2).click()
        # input_tel = "userName"
        # btn = 'send-msg'
        # print('【SuNingYiGou】')
        # tel_get_3(url, into, input_tel, btn)

    def FanKe(self):
        url = "https://www.fkw.com/reg.html"
        into = 'cancel-text'
        into2 = 'login_UersCode'
        input_tel = 'acct'
        btn = 'verifyCodeBtn'
        print('【FanKe】')
        # tel_get_2(url, input_tel, btn)
        tel_get_4(url, into, into2, input_tel, btn)

    # def WangyiYun(self):
    #     # 难啃系数3颗星
    #     url = "https://id.163yun.com/register?referrer=https://dun.163.com/dashboard&h=yd&"
    #     into = ".yidun_intelli-text"
    #     input_tel = "m-input"
    #     btn = '.m-btn'
    #     print('【WangyiYun】')
    #     tel_get_3(url, into, input_tel, btn)

    def BeiRui(self):
        url = 'https://console.oray.com/passport/register.html?fromurl=http%3A%2F%2Fdomain .oray.com%2F'
        # into = '//*[@id="tips-protocol-win"]/div/div/div/div[2]/p/ input[1]'
        broswer.get(url)
        # a=broswer.find_element_by_css_selector('[class="agree btn"]').get_attribute('innerHTML')
        a=broswer.find_element_by_css_selector('[class="agree btn"]').click()
        print(a)
        broswer.find_element_by_css_selector('[name="account"]').send_keys('12')
        broswer.find_element_by_css_selector('[name="phone"]').send_keys(tel)
        broswer.find_element_by_css_selector('[class="register-input__code btn"]').click()

        # into = 'agree btn'
        # input_tel = "mobile"
        # btn = "re-get"
        # print('【BeiRui】')
        # tel_get_3(url, into, input_tel, btn)

    def XueJia(self):
        url = "https://cn.student.com/au/adelaide?utm_source=baidu&utm_medium=cpc&utm_campaign=3_destination_au_pc&utm_content=3_adelaide_g_web_p&utm_term=adelaide%E7%A7%9F%E6%88%BF%E7%BD%91#sign-up"
        broswer.get(url)
        broswer.find_element_by_css_selector('[class="login-type-ta b-wrapper__tab__item"]').click()
        broswer.find_element_by_css_selector('[data-tid="phoneNumber"]').send_keys(tel)
        broswer.find_element_by_css_selector('[data-tid="phoneContinue"]').click()
        time.sleep(1)
        broswer.find_element_by_css_selector('[class="osl-btn osl-btn-keppel phone-input-code-field__send-code-btn"]').click()
        # input_tel = 'input-field__input'
        # btn = '.send-button__text'
        # print('【XueJia】')
        # tel_get_2(url, input_tel, btn)

    def run(self):
        # pass
        # for i in range(20):
        #     time.sleep(70)
        #     # self.TongCheng_com()
        #     self.BeiRui()
        #     print('test time: ' + str(i))
            # time.sleep(120)
        # self.Guazi_com()
        # self.JianShu()  # 需要解决滑动验证码问题
        # self.FanKe()  # 需要滑块验证(留待解决),未调试完成
        # self.SuNingYiGou()   #滑动验证1
        # self.WangyiYun()
        # self.BeiRui()
        self.XueJia()   # 未测试1


s = Spider_tel()
s.run()
