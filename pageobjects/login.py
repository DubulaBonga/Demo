# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from selenium.webdriver.common.by import By
from toolium.pageelements import *
from toolium.pageobjects.page_object import PageObject
import time


class BaseInitialPageObject(PageObject):
    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper=None, wait=False)
        self.username = None

    def wait_until_loaded(self, **kwargs):
        """Wait until page is loaded

        :param **kwargs:
        :returns: initial page object
        """
        self.username.wait_until_visible(20)
        return self


class InitialPageObject(BaseInitialPageObject):
    def __init__(self):
        super().__init__()
        self.username = InputText(By.ID, 'UserName')
        self.email = InputText(By.ID, 'Email')
        self.password = InputText(By.ID, 'Password')
        self.confirm_password = InputText(By.ID, 'ConfirmPassword')
        self.register_btn = Button(By.XPATH, "/html/body/div[3]/header/div[2]/a[2]")
        self.next_button = Button(By.CLASS_NAME, 'modal-button_next')

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.driver.get('{}/login'.format(self.config.get('Test', 'url')))
        return self

    def register_button(self):
        """ Fill login form and submit it

        :param user: dict with username and password values
        :returns: secure area page object instance
        """
        self.register_btn.click()

    def register(self, ):
        self.username.text = 'username'
        self.email.text = 'email'
        self.password.text = 'password'
        self.confirm_password.text = 'confirm_password'
        self.next_button.click()
        time.sleep(5)

