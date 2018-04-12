# -*-coding:utf-8 -*-
from models import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, sys
import unittest
import HTMLTestRunner


class bokeyuan(unittest.TestCase):
    def setUp(self):
        self.browser = driver.browser()
        self.browser.get("https://www.cnblogs.com/")
        self.browser.maximize_window()

    def testbokeyuan1(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'zzk_q')))
        self.browser.find_element_by_id("zzk_q").send_keys("找博客")
        # self.browser.find_element_by_xpath("input[@]onclick='zzk_go'").click()
        time.sleep(3)

    def testbokeyuan2(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, 'zzk_q')))
        self.browser.find_element_by_id("zzk_q").send_keys("再次博客")
        # self.browser.find_element_by_xpath("input[@]onclick='zzk_go'").click()
        time.sleep(3)

    def tearDown(self):
        self.browser.quit()


# if __name__ == "__main__":
#     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#     suite1 = unittest.TestLoader().loadTestsFromTestCase('Baidu')
#     suite = unittest.TestSuite([suite1])
#     HtmlFile = "result\\" + now + "HTMLtemplate.html"
#     with open(HtmlFile, "wb") as fp:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                                title=u"百度测试报告",
#                                                description=u"用例测试情况"
#                                                )
#         runner.run(suite)

