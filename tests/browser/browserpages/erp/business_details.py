# -*- coding: utf-8 -*-
"""ERP - Business details"""
from random import choice
from types import ModuleType
from typing import List, Union

from browserpages import ElementType, common_selectors
from browserpages.common_actions import (
    Actor,
    Selector,
    check_for_sections,
    check_form_choices,
    check_radio,
    check_url,
    fill_out_input_fields,
    pick_option,
    submit_form,
)
from browserpages.erp import summary
from browserpages.erp.autocomplete_callbacks import autocomplete_uk_region
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from great_magna_tests_shared import URLs
from great_magna_tests_shared.enums import PageType, Service

NAME = "Business details"
SERVICE = Service.ERP
TYPE = PageType.FORM
URL = None
PAGE_TITLE = ""
SubURLs = {
    f"{NAME} (UK business)": URLs.ERP_BUSINESS_BUSINESS_DETAILS.absolute,
    f"{NAME} (UK importer)": URLs.ERP_IMPORTER_BUSINESS_DETAILS.absolute,
}
SubURLs = {key.lower(): val for key, val in SubURLs.items()}
NAMES = list(SubURLs.keys())


SELECTORS = {
    "form": {
        "selection form": Selector(By.CSS_SELECTOR, "#content form[method='post']"),
        "step counter": Selector(
            By.CSS_SELECTOR, "form[method=post] span.govuk-caption-l"
        ),
        "heading": Selector(By.CSS_SELECTOR, "form[method=post] h1"),
        "uk private or public limited company": Selector(
            By.ID,
            "id_business-company_type_0",
            type=ElementType.RADIO,
            is_visible=False,
            alternative_visibility_check=True,
        ),
        "other type of uk organisation": Selector(
            By.ID,
            "id_business-company_type_1",
            type=ElementType.RADIO,
            is_visible=False,
            alternative_visibility_check=True,
        ),
        "company name": Selector(
            By.ID, "id_business-company_name", type=ElementType.INPUT
        ),
        "industry": Selector(By.ID, "id_business-sector", type=ElementType.SELECT),
        "company size": Selector(
            By.ID, "id_business-employees", type=ElementType.SELECT
        ),
        "annual turnover": Selector(
            By.ID, "id_business-turnover", type=ElementType.SELECT
        ),
        "regions": Selector(
            By.ID,
            "id_business-employment_regions_autocomplete",
            type=ElementType.INPUT,
            autocomplete_callback=autocomplete_uk_region,
        ),
        "continue": Selector(
            By.CSS_SELECTOR,
            "#content > form button.govuk-button",
            type=ElementType.SUBMIT,
            next_page=summary,
        ),
    }
}
SELECTORS.update(common_selectors.ERP_HEADER)
SELECTORS.update(common_selectors.ERP_BETA)
SELECTORS.update(common_selectors.ERP_BACK)
SELECTORS.update(common_selectors.ERP_SAVE_FOR_LATER)
SELECTORS.update(common_selectors.ERP_FOOTER)


def should_be_here(driver: WebDriver, *, page_name: str = None):
    url = SubURLs[page_name]
    check_url(driver, url, exact_match=False)


def should_see_sections(driver: WebDriver, names: List[str]):
    check_for_sections(driver, all_sections=SELECTORS, sought_sections=names)


def should_see_form_choices(driver: WebDriver, names: List[str]):
    check_form_choices(driver, SELECTORS["form"], names)


def generate_form_details(actor: Actor, *, custom_details: dict = None) -> dict:
    private_or_other = choice([True, False])
    result = {
        "uk private or public limited company": private_or_other,
        "other type of uk organisation": not private_or_other,
        "company name": "AUTOMATED TESTS",
        "industry": None,
        "company size": None,
        "annual turnover": None,
        "regions": True,
    }
    if custom_details:
        result.update(custom_details)
    return result


def fill_out(driver: WebDriver, details: dict):
    form_selectors = SELECTORS["form"]
    check_radio(driver, form_selectors, details)
    pick_option(driver, form_selectors, details)
    fill_out_input_fields(driver, form_selectors, details)


def submit(driver: WebDriver) -> Union[ModuleType, None]:
    return submit_form(driver, SELECTORS["form"])
