from selenium import webdriver

from wework_po.utils.log_util import logger


class Base:
    _BASE_URL = ""

    def __init__(self, base_driver=None):
        """初始化driver 如果存在，复用driver ，如果不存在 创建一个driver"""
        if base_driver:
            # 复用driver
            self.driver = base_driver
        else:
            # 为None
            # 创建一个driver
            # 第一步：创建一个driver实例变量
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

        if not self.driver.current_url.startswith("http"):
            # 不以http 开头则打开_base_url
            self.driver.get(self._BASE_URL)

    def do_find(self, by, value=None):
        """查找单个元素"""
        if value:
            return self.driver.find_element(by, value)
        else:
            # (By.ID,"")
            return self.driver.find_element(*by)

    def do_finds(self, by, value=None):
        """查找多个元素"""
        # (By.ID,"")
        if value:
            return self.driver.find_elements(by, value)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self, text, by, value=None):
        """输入文本"""
        ele = self.do_find(by, value)
        ele.clear()
        ele.send_keys(text)

    def do_quit(self):
        self.driver.quit()