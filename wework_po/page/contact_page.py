"""通讯录页面"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from wework_po.page.add_part_page import AddPartPage
from wework_po.page.base import Base
from wework_po.utils.log_util import logger
from wework_po.utils.web_util import click_exception


class ContactPage(Base):
    __TEXT_TIPS = By.ID, "js_tips"
    __BTN_ADD_MEMBER = (By.LINK_TEXT, "添加成员")

    """通讯录页面：获取操作结果"""

    def get_tips(self):
        # 获取添加成功提示
        logger.info("通讯录页面：获取操作结果")
        result = self.do_find(self.__TEXT_TIPS).text
        return result

    """通讯录页面：点击添加成员"""
    def contact_click_add_member(self):
        logger.info("通讯录页面：点击添加成员")
        WebDriverWait(self.driver, 10).until(click_exception(*self.__BTN_ADD_MEMBER))
        from wework_po.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    """通讯录页面：点击添加部门"""
    def click_add_part(self):
        logger.info("通讯录页面：点击添加部门")
        # 1.点击【+】
        self.driver.find_element(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        # 2.点击 添加部门
        self.driver.find_element(By.LINK_TEXT, "添加部门").click()
        return AddPartPage(self.driver)

