from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import win32gui
import win32con
import time


class com():
    def __init__(self,driver=None):
        if driver:
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def find_ele_click(self,ele):
        self.driver.find_element_by_xpath(self.wait(ele)).click()


    def wait(self,ele):
        WebDriverWait(self.driver,20,1).until(EC.presence_of_element_located((By.XPATH,ele)))
        return ele


    def find_text(self,ele):
        self.driver.find_element_by_xpath(ele).text()


    def open(self,url):
        self.driver.get(url)


    def windos(self,ele):
        self.driver.execute_script('arguments[0].scrollIntoView();', ele)


    def scroll(self,y):
        self.driver.execute_script(f"window.scrollBy({0},{y})")


    def find_ele_send(self,ele,text):
        # if finder == "xpath":
        self.driver.find_element_by_xpath(self.wait(ele)).send_keys(text)
        # elif finder == "id":
        #     self.driver.find_element_by_id(self.wait(ele)).send_keys(text)
        # elif finder == "css":
        #     self.driver.find_element_by_css_selector(self.wait(ele)).send_keys(text)
        # else:
        #     print('err')


    def get_text(self,ele):
        self.driver.find_element_by_xpath(ele).get_attribute('value')


    def clear(self,ele):
        self.driver.find_element_by_xpath(ele).clear()


    def close(self,close):
        if close:
            self.driver.quit()
        else:
            self.driver.quit()


    def upload(self,ele,file):

        self.driver.find_element_by_xpath(ele).click()
        time.sleep(1)
        dialog = win32gui.FindWindow('#32770', u'打开') #系统弹窗
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None,file)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    def time(self,s):
        if type(s) == str:
            time.sleep(int(s))
        elif type(s) == int:
            time.sleep(s)
        else:
            return '格式错误'