# coding:utf-8
import unittest
import os
import HTMLTestRunner

# 用例路径
case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'case')#获取当前目录下的case目录

#报告存放路径
report_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'report')#获取当前目录下的report目录

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_case())

    #html报告文件路径
    report_abspath = os.path.join(report_path, 'result.html')
    fp = open(report_abspath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'我的测试报告',
                                           description=u'描述的位置')
    runner.run(all_case())
    fp.close()
