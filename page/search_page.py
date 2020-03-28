import os, sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())

from base.base_action import BaseAction

class SearchPage(BaseAction):

    # 搜索按钮
    search_button = By.ID, "com.android.settings:id/search"
    # 搜索框
    input_text_view = By.ID, "android:id/search_src_text"
    # 返回按钮
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def click_search(self):
        self.click(self.search_button)

    def input_content(self, text):
        self.input_text(self.input_text_view, text)

    def click_back(self):
        self.click(self.back_button)