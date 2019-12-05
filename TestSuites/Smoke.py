import pytest
from TestCases import test_job
import HtmlTestRunner
from builtins import dir
import os
import time
import unittest
import allure

suite1=unittest.loader.findTestCases(test_job)
testrunner=unittest.TestRunner()
testrunner.run(suite1)
f=open('Result.html','w')
testrunner=HtmlTestRunner(stream=f,title="Autmation Result",description="Test Automation")
testrunner.run(suite1)
if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\reports'))