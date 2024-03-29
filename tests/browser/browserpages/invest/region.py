# -*- coding: utf-8 -*-
"""Regional page."""
import logging
from typing import List

from browserpages import common_selectors
from browserpages.common_actions import (
    Selector,
    assertion_msg,
    check_for_sections,
    check_url,
    go_to_url,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service

NAME = "Region"
NAMES = [
    "London",
    "North of England",
    "Northern Ireland",
    "Scotland",
    "South of England",
    "Midlands",
    "Wales",
]
SERVICE = Service.INTERNATIONAL
TYPE = PageType.REGION
URL = URLs.INTERNATIONAL_REGIONS.absolute
PAGE_TITLE = "Invest in Great Britain - "


SubURLs = {
    "london": URLs.INTERNATIONAL_REGIONS_LONDON.absolute,
    "north of england": URLs.INTERNATIONAL_REGIONS_NORTH_ENGLAND.absolute,
    "northern ireland": URLs.INTERNATIONAL_REGIONS_NORTHERN_IRELAND.absolute,
    "scotland": URLs.INVEST_REGIONS_SCOTLAND.absolute,
    "south of england": URLs.INTERNATIONAL_REGIONS_SOUTH_ENGLAND.absolute,
    "midlands": URLs.INTERNATIONAL_REGIONS_MIDLANDS.absolute,
    "wales": URLs.INTERNATIONAL_REGIONS_WALES.absolute,
}


SELECTORS = {
    "regional breadcrumbs": {
        # "great.gov.uk international": Selector(
        #     By.CSS_SELECTOR, "nav.breadcrumbs ol > li:nth-child(1) > a"
        # ),
        # "about the uk": Selector(
        #     By.CSS_SELECTOR, "nav.breadcrumbs ol > li:nth-child(2) > a"
        # ),
        # "regions": Selector(
        #     By.CSS_SELECTOR, "nav.breadcrumbs ol > li:nth-child(3) > a"
        # ),
    },
    "expanding your business": {
        "itself": Selector(By.CSS_SELECTOR, "#content > section:nth-child(4)"),
    },
    "related opportunities": {
        "itself": Selector(By.CSS_SELECTOR, "#content > section:nth-child(5)"),
    },
    "strategic markets": {
        "itself": Selector(By.CSS_SELECTOR, "#content > section:nth-child(6)"),
    },
    "case study": {
        "itself": Selector(By.CSS_SELECTOR, "#content > section:nth-child(7)"),
    },
}
SELECTORS.update(common_selectors.INTERNATIONAL_HEADER_WO_LANGUAGE_SELECTOR)
SELECTORS.update(common_selectors.INTERNATIONAL_HERO)
SELECTORS.update(common_selectors.ERROR_REPORTING)
SELECTORS.update(common_selectors.INTERNATIONAL_FOOTER)


def visit(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name] if page_name else URL
    go_to_url(driver, url, page_name or NAME)


def should_be_here(driver: WebDriver, *, page_name: str):
    url = SubURLs[page_name.lower()] if page_name else URL
    check_url(driver, url)
    logging.debug("All expected elements are visible on '%s' page", PAGE_TITLE)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def clean_name(name: str) -> str:
    return name.split(" - ")[1].strip()


def should_see_content_for(driver: WebDriver, region_name: str):
    source = driver.page_source
    region_name = clean_name(region_name)
    logging.debug("Looking for: {}".format(region_name))
    with assertion_msg(
        "Expected to find term '%s' in the source of the page %s",
        region_name,
        driver.current_url,
    ):
        assert region_name.lower() in source.lower()


def should_see_following_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)
