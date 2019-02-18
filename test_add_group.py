import time, unittest
from selenium.webdriver.firefox.webdriver import WebDriver


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(8)

    def test_add_group(self):
        success = True
        wd = self.wd
        wd.get("http://localhost")
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("test")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("test")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("test")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()