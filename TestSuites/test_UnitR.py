import unittest
from HtmlTestRunner import HTMLTestRunner
from TestCases import test_Unit
def test_suite():
    test_suite = unittest.TestCases()
    test_suite.addTest(unittest.makeSuite(TestPyTestClass))

    return test_suite

#2nd-way to run suite and report
runner = HTMLTestRunner(output="Reports",
                        report_title="My Report",
                        report_name="Test Report")
runner.run(suite())

#1st-way to run only suite
#runner=unittest.TextTestRunner()
#runner.run(suite())