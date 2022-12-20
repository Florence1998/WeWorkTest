"""添加成员页面"""
from selenium.webdriver.common.by import By

from wework_po.page.base import Base
from wework_po.page.contact_page import ContactPage
from wework_po.utils.log_util import logger


class AddMemberPage(Base):
    _INPUT_USERNAME = (By.ID, "username")
    _INPUT_ACCIT = By.ID, "memberAdd_acctid"
    _INPUT_PHONENUMBER = (By.ID, "memberAdd_phone")
    _BTN_SAVE = (By.CSS_SELECTOR, ".js_btn_save")
    """添加成员页面：填写成员资料，点击保存"""

    def fill_info(self, name, accid, phone_number):
        logger.info("添加成员页面：填写成员资料，点击保存")
        # input username,phonenumber,accid
        # 点击保存
        self.do_send_keys(name, self._INPUT_USERNAME)
        self.do_send_keys(accid, self._INPUT_ACCIT)
        self.do_send_keys(phone_number, self._INPUT_PHONENUMBER)

        # 3、点击保存
        self.do_find(self._BTN_SAVE).click()
        return ContactPage(self.driver)
