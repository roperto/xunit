#!/usr/bin/env python


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()

    def set_up(self):
        pass

    def tear_down(self):
        pass


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


class TestCaseTest(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.test = None

    def test_template_method(self):
        self.test = WasRun("test_method")
        self.test.run()
        assert ("set_up test_method tear_down " == self.test.log)


TestCaseTest("test_template_method").run()
