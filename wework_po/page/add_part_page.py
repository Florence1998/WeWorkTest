"""添加部门页面"""
from selenium.webdriver.common.by import By

from wework_po.page.base import Base
from wework_po.utils.log_util import logger


class AddPartPage(Base):
    __INPUT_PART_NAME = (By.XPATH, "//*[@name='name']")
    __SELECT_DEPART = (By.CSS_SELECTOR, ".js_parent_party_name")
    __OPT_DEPART = (By.XPATH, "//div[@class='inputDlg_item']//a[text()='翟羽佳科技有限公司']")
    __BTN_CONFIRM = (By.XPATH, "//a[text()='确定']")
    """添加部门 页面：填写部门 信息，点击保存"""

    def fill_part_info(self, part_name):
        logger.info("添加部门 页面：填写部门 信息，点击保存")
        # 1 输入 部门名称
        self.do_send_keys(part_name, self.__INPUT_PART_NAME)
        # 2 点击 所属部门
        self.do_find(self.__SELECT_DEPART).click()
        # 3 选择 翟羽佳科技有限公司
        self.do_find(self.__OPT_DEPART).click()
        # 4 点击 确定
        self.do_find(self.__BTN_CONFIRM).click()
        from wework_po.page.contact_page import ContactPage
        return ContactPage(self.driver)
