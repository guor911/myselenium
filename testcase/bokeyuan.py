# -*-coding:utf-8 -*-
from selenium import webdriver
import time, sys
import unittest
import HTMLTestRunner


class bokeyuan(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("http://www.baidu.com")
        self.browser.maximize_window()
        assert '百度一下，你就知道' in self.browser.title

    def testbokeyuan1(self):
        print('first')
        self.browser.find_element_by_id("kw").send_keys("我找百度")
        self.browser.find_element_by_id("su").click()
        # time.sleep(3)
        # assert 'firefox' is self.browser.name

    def testbokeyuan2(self):
        print('second')
        self.browser.find_element_by_id("kw").send_keys("再次百度")
        self.browser.find_element_by_id("su").click()
        # time.sleep(3)

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

