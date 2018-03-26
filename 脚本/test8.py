#coding:utf-8
import os
import json
import unittest
# from .HTMLTestRunner import HTMLTestRunner
# from .configHttp import ConfigHttp
from nose_parameterized import parameterized
from ddt import ddt, file_data,unpack
# data=['TC_INT_1','TC_INT_2','TC_INT_3','TC_INT_4']
# case_id=run_temp.objects.values()
# print(case_id)

# case_id=['TC_INT_1','TC_INT_2','TC_INT_3','TC_INT_4']

# if os.path.isfile('interface/cases.txt'):
# fp = open('interface/cases.init', 'r')
# content = fp.read()
# case_id = content.split("\n")
# fp.close()


# else:
@ddt
class interfaceTest(unittest.TestCase):

    # test=ConfigHttp()

    @file_data('cases.json')
    def test_case(self, case_id):
            print('用例id是',case_id)
            # self.test.run(case_id)
            assert 1==9



if __name__ == '__main__':

    # suite= unittest.TestSuite()
    # suite.addTests(unittest.makeSuite(interfaceTest))
    # fp = open('report.html', 'wb')
    # runner = unittest.TextTestRunner(stream=fp, title='接口测试报告:', description='用例测试报告')
    # runner.run(suite)


    suite = unittest.TestLoader().loadTestsFromTestCase(interfaceTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

