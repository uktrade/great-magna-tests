# -*- coding: utf-8 -*-
"""ERP - Holding"""
from typing import List

from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Selector,
    check_for_sections,
    check_url,
    go_to_url,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service

NAME = "Holding"
SERVICE = Service.ERP
TYPE = PageType.LANDING
URL = URLs.ERP_LANDING.absolute
PAGE_TITLE = ""

SELECTORS = {
    "holding message": {
        "heading": Selector(By.CSS_SELECTOR, "#content h1"),
        "description": Selector(By.CSS_SELECTOR, "#content h1 ~ p"),
        "gov.uk links": Selector(
            By.CSS_SELECTOR, "#content p a", type=ElementType.LINK
        ),
    }
}
SELECTORS.update(common_selectors.ERP_HEADER)
SELECTORS.update(common_selectors.ERP_BETA_SHORT)
SELECTORS.update(common_selectors.ERP_FOOTER)


def visit(driver: WebDriver):
    go_to_url(driver, URL, NAME)


def should_be_here(driver: WebDriver):
    check_url(driver, URL)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)
