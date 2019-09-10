# -*- coding: UTF-8 -*-
from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can(self):
        '''verificação da home page'''
        self.browser.get('http://localhost:8000')
        self.assertIn('Django',self.browser.title)
        '''self.fail('Finish Test')'''

if __name__ == '__main__':
    unittest.main()
