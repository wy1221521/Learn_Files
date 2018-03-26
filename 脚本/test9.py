#coding:utf-8
import os
import json
import unittest

from nose_parameterized import parameterized
from HTMLTestRunner import HTMLTestRunner
from ddt import ddt, data,file_data,unpack
from django.conf import settings
case_id={'name1':'TC_INT_1','name2':'TC_INT_2','name3':'TC_INT_3'}
# @ddt
# class interfaceTest(unittest.TestCase):
#     @data(case_id)
#     def test_case(self, case_id):
#             print(case_id)
#             assert 1==2
#
#
# if __name__ == '__main__':
#     result_file = 'report2.html'
#     fp = open(result_file, 'wb')
class interfaceTest(unittest.TestCase):

    @parameterized.expand(case_id)
    def test_add(self, name, a, b, c):
        self.assertEqual(a + b, c)

    #
    # suite = unittest.TestLoader().loadTestsFromTestCase(interfaceTest)
    # runner = HTMLTestRunner(stream=fp, title='接口测试报告:' + case_id['name2'], description='用例测试报告')
    # runner.run(suite)
if __name__ == '__main__':

    result_file='report.html'
    fp = open(result_file, 'wb')
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(interfaceTest))
    runner = HTMLTestRunner(stream=fp, title='接口测试报告:' + case_id['name2'], description='用例测试报告')
    runner.run(suite)

