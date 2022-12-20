"""用例层，只关心业务"""

from wework_po.page.login_page import LoginPage


class TestWeWork(object):
    def setup(self):
        """登录页面：用户登录"""
        self.home = LoginPage().login()
        # mock 测试数据
        from faker import Faker
        fake = Faker('zh_CN')
        self.name = fake.name()
        self.phone_number = fake.phone_number()
        self.accid = fake.ssn()

    def teardown(self):
        # 退出浏览器
        self.home.do_quit()

    # 首页：添加成员
    def test_homepage_add_member(self):
        """企业微信主页面：点击添加成员"""
        """添加成员页面：填写成员资料，点击保存"""
        """通讯录页面：获取操作结果"""
        tips = self.home \
            .click_add_member() \
            .fill_info(self.name, self.accid, self.phone_number) \
            .get_tips()
        assert "保存成功" == tips

    # 通讯录页面：添加成员
    def test_contact_page_add_member(self):
        """企业微信主页面：点击通讯录"""
        """通讯录页面：点击添加成员"""
        """添加成员页面：填写成员资料，点击保存"""
        """通讯录页面：获取操作结果"""
        tips = self.home \
            .click_contact() \
            .contact_click_add_member() \
            .fill_info(self.name, self.accid, self.phone_number) \
            .get_tips()
        assert "保存成功" == tips

    # 通讯录页面：添加部门
    def test_contact_page_add_part(self):
        """企业微信主页面：点击通讯录"""
        """通讯录页面：点击添加部门"""
        """添加部门页面：填写部门信息，点击保存"""
        """通讯录页面：获取操作结果"""
        tips = self.home \
            .click_contact() \
            .click_add_part() \
            .fill_part_info("测试认证处1") \
            .get_tips()
        assert "新建部门成功" == tips
