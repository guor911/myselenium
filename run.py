import time, os
import unittest
import HTMLTestRunner


now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
HtmlFile = "result\\" + now + "HTMLtemplate.html"

cases = []
for file_name in os.listdir(os.getcwd()+r"\testcase"):
    suite1 = unittest.TestLoader().loadTestsFromName('testcase'+'.'+file_name.split('.')[0])
    cases.append(suite1)
suite = unittest.TestSuite(cases)

with open(HtmlFile, "wb") as fp:
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u"百度测试报告",
                                           description=u"用例测试情况"
                                           )
    runner.run(suite)
    exit(0)
