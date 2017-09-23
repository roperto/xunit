#!/usr/bin/env python


class TestCase:
    def __init__(self, name):
        self.wasRun = None
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun("test_method")
        assert not test.wasRun
        test.run()
        assert test.wasRun


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def test_method(self):
        self.wasRun = 1


TestCaseTest("test_running").run()
