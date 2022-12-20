"""企业微信主页面"""
from selenium.webdriver.common.by import By

from wework_po.page.add_member_page import AddMemberPage
from wework_po.page.base import Base
from wework_po.page.contact_page import ContactPage
from wework_po.utils.log_util import logger


class HomePage(Base):
    __BTN_ADDMEMBER = (By.CSS_SELECTOR, ".index_service_cnt_item_title")
    __MENU_CONTACT = (By.ID, "menu_contacts")
    """企业微信主页面：点击添加成员"""

    def click_add_member(self):
        # 点击【添加成员】
        logger.info("企业微信主页面：点击添加成员")
        self.do_find(self.__BTN_ADDMEMBER).click()
        return AddMemberPage(self.driver)

    """企业微信主页面：点击通讯录"""
    def click_contact(self):
        logger.info("企业微信主页面：点击通讯录")
        self.do_find(self.__MENU_CONTACT).click()
        return ContactPage(self.driver)


