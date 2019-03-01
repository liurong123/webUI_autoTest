from pageobjects.base import Base
from selenium.webdriver.common.by import By
import time
class IndexPage(Base):
    index_page_username=(By.NAME,'username')
    index_page_pwd=(By.NAME,'password')
    index_page_login=(By.CSS_SELECTOR,'button em')

    def Login(self,username,pwd):
        self.sendkeys(username,*self.index_page_username)
        self.sendkeys(pwd,*self.index_page_pwd)
        self.clik(*self.index_page_login)
        self.jihuo()
#发帖
class FaTie(Base):
    fatie_page_button = (By.ID, "newspecial")  # 发帖
    index_page_mrbk = (By.CSS_SELECTOR, '.fl_icn a')  # 默认版块
    fatie_page_title =(By.NAME,'subject')#标题
    iframe=(By.TAG_NAME,'iframe')
    fatie_page_content=(By.TAG_NAME,'body')#发帖内容
    fabiao_button=(By.NAME,'topicsubmit')

    def fatie(self,title,content):
        self.jihuo()
        self.clik(*self.index_page_mrbk)
        self.jihuo()
        self.clik(*self.fatie_page_button)
        self.jihuo()
        self.sendkeys(title,*self.fatie_page_title)
        self.switch_to(*self.iframe)
        self.sendkeys(content,*self.fatie_page_content)
        self.jihuo()
        self.clik(*self.fabiao_button)
    def newfatie(self,title,content,new):
        self.xinmokuai=(By.LINK_TEXT,new)
        self.jihuo()
        self.clik(*self.xinmokuai)
        self.jihuo()
        self.clik(*self.fatie_page_button)
        self.jihuo()
        self.sendkeys(title,*self.fatie_page_title)
        self.switch_to(*self.iframe)
        self.sendkeys(content,*self.fatie_page_content)
        self.jihuo()
        self.clik(*self.fabiao_button)
#回帖
class HuiTie(Base):
    huitie_button=(By.ID,'post_reply')
    huitie_content=(By.ID,'postmessage')
    huitie_fabiao=(By.ID,'postsubmit')#发表回复
    def huitie(self,text):
        # self.jihuo()
        self.clik(*self.huitie_button)
        self.sendkeys(text,*self.huitie_content)
        self.jihuo()
        self.clik(*self.huitie_fabiao)
#退出
class TuiChu(Base):
    tuichu_button=(By.LINK_TEXT,'退出')
    def tuichu(self):
        self.jihuo()
        self.clik(*self.tuichu_button)
#删除帖子
class Delete(Base):
    index_page_mrbk = (By.CSS_SELECTOR, '.fl_icn a')  # 默认版块
    page_duigou =(By.NAME,'moderate[]')
    page_delete=(By.LINK_TEXT,"删除")
    page_yes=(By.NAME,'modsubmit')
    def delete(self):
        self.jihuo()
        self.clik(*self.index_page_mrbk)
        self.jihuo()
        self.clik(*self.page_duigou)
        self.clik(*self.page_delete)
        self.clik(*self.page_yes)
#增加新模块
class AddNewModule(Base):
    guanlizhongxin=(By.LINK_TEXT,'管理中心')
    time.sleep(10)
    page_luntan=(By.LINK_TEXT,'论坛')
    iframe = (By.TAG_NAME, 'iframe')
    page_addnew=(By.LINK_TEXT,'添加新版块')
    qingchu=(By.NAME,'newforum[1][]')
    page_add=(By.ID,'submit_editsubmit')
    def addNewModule(self,title):
        self.clik(*self.guanlizhongxin)
        time.sleep(2)
        self.jh(2)
        self.clik(*self.page_luntan)
        self.switch_to(*self.iframe)
        self.clik(*self.page_addnew)
        self.clear(*self.qingchu)
        self.sendkeys(title,*self.qingchu)
        self.clik(*self.page_add)
#搜索帖子
class Sousuo(Base):
    sousuo_txt=(By.ID,'scbar_txt')
    sousuo_button=(By.ID,'scbar_btn')
    sousuo_title=(By.CSS_SELECTOR,".xs3 a")
    tiezi_title=(By.ID,'thread_subject')
    def sousuo(self,title):
        self.clik(*self.sousuo_txt)
        self.sendkeys(title,*self.sousuo_txt)
        self.clik(*self.sousuo_button)
        time.sleep(5)
        self.jh(2)
        self.clik(*self.sousuo_title)
        time.sleep(5)
        self.jh(3)
        value=self.text(*self.tiezi_title)
        return value
#发表投票帖子
class FaQiTouPiao(Base):
    fatie_page_button = (By.ID, "newspecial")  # 发帖
    index_page_mrbk = (By.CSS_SELECTOR, '.fl_icn a')  # 默认版块
    page_paqitoupiao=(By.LINK_TEXT,'发起投票')
    faqi_title=(By.NAME,'subject')
    faqi_xuanxiang1=(By.XPATH,"//*[@id='pollm_c_1']/p[1]/input")
    faqi_xuanxiang2 = (By.XPATH,"//*[@id='pollm_c_1']/p[2]/input")
    faqi_content=(By.TAG_NAME,'body')
    faqibutton=(By.ID,'postsubmit')
    def faqitoupiao(self,title,choose1,choose2):
        self.clik(*self.index_page_mrbk)
        self.jihuo()
        self.clik(*self.fatie_page_button)
        self.jihuo()
        self.jihuo()
        self.clik(*self.page_paqitoupiao)
        self.sendkeys(title,*self.faqi_title)
        self.sendkeys(choose1,*self.faqi_xuanxiang1)
        self.sendkeys(choose2, *self.faqi_xuanxiang2)
        self.clik(*self.faqibutton)
        self.jihuo()
class TouPiao(Base):
    danxuan=(By.ID,'option_2')
    tijiao_button=(By.ID,'pollsubmit')#提交
    def toupiao(self):
        self.clik(*self.danxuan)
        self.clik(*self.tijiao_button)
        self.jihuo()
class HuoQu(Base):
    toupiao_zhuti=(By.ID,'thread_subject')#投票主题
    toupiao_xuanxiang1=(By.XPATH,'//label[@for="option_1"]')
    toupiao_xuanxiang2 = (By.XPATH, '//label[@for="option_2"]')
    bili1=(By.CSS_SELECTOR,'.pcht :nth-child(4) :nth-child(2)')
    bili2=(By.CSS_SELECTOR,".pcht :nth-child(2) :nth-child(2)")

    def houqu(self):
        zhuti=self.text(*self.toupiao_zhuti)
        print("发起投票的主题是：",zhuti)
        xuanxiang1=self.text(*self.toupiao_xuanxiang1)
        bili1=self.text(*self.bili1)
        print("投票的选项为：",xuanxiang1,"比例为",bili1)
        xuanxiang2=self.text(*self.toupiao_xuanxiang2)
        bili2 = self.text(*self.bili2)
        print("投票的选项为：",xuanxiang2,"比例为",bili2)



















