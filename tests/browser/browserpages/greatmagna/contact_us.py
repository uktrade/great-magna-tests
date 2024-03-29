import logging
import random
import time
from types import ModuleType
from typing import List, Union

from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Actor,
    Selector,
    assertion_msg,
    check_for_sections,
    check_if_element_is_not_present,
    check_if_element_is_visible,
    check_random_radio,
    check_url,
    fill_out_email_address,
    fill_out_input_fields,
    find_element,
    find_elements,
    find_selector_by_name,
    go_to_url,
    is_element_present,
    pick_option,
    submit_form,
    take_screenshot,
    wait_for_page_load_after_action,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service
from great_magna_tests_shared.utils import check_url_path_matches_template

NAME = "Contact us Page"
SERVICE = Service.GREATMAGNA
TYPE = PageType.DASHBOARD
URL = URLs.GREAT_MAGNA_CONTACT_US.absolute
PAGE_TITLE = "Contact us Page"

SELECTORS = {
    "contact us": {
        "please give detail": Selector(By.CSS_SELECTOR, 'textarea[id="id_comment"]'),
        "first name": Selector(By.CSS_SELECTOR, "#id_given_name"),
        "last name": Selector(By.CSS_SELECTOR, "#id_family_name"),
        "contact email": Selector(By.CSS_SELECTOR, "#id_email"),
        "tick": Selector(By.CSS_SELECTOR, "#id_terms_agreed-label"),
        "submit": Selector(By.CSS_SELECTOR, 'button[class="button button--large"]'),
    },
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL, exact_match=False)


def find_and_click_change_link(driver: WebDriver, element_selector_name: str):
    change_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    change_link.click()


def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["form"])


def fills_out_submit(driver: WebDriver):
    driver.find_element_by_css_selector("#id_comment").clear()
    driver.find_element_by_css_selector("#id_comment").send_keys("Automated Tests")
