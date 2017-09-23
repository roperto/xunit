#!/usr/bin/env python


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tear_down()
        return result

    def set_up(self):
        pass

    def tear_down(self):
        pass


class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def test_started(self):
        self.runCount += 1

    def test_failed(self):
        self.errorCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)


class WasRun(TestCase):
    def __init__(self, name):
        self.log = ""
        TestCase.__init__(self, name)

    def set_up(self):
        self.log += "set_up "

    def tear_down(self):
        self.log += "tear_down "

    def test_method(self):
        self.log += "test_method "

    def test_broken_method(self):
        raise Exception


class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert ("set_up test_method tear_down " == test.log)

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert ("1 run, 1 failed" == result.summary())

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert ("1 run, 1 failed" == result.summary())


TestCaseTest("test_template_method").run()
TestCaseTest("test_result").run()
TestCaseTest("test_failed_result").run()
TestCaseTest("test_failed_result_formatting").run()
