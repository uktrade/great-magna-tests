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
    fill_out_textarea_fields,
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

NAME = "Business Objectives"
SERVICE = Service.BUILD_AN_EXPORT_PLAN
TYPE = PageType.BUILD_AN_EXPORT_PLAN
URL = URLs.GREAT_MAGNA_EXPORT_PLAN_BUSINESS_OBJECTIVES.absolute_template
PAGE_TITLE = "Business Objectives Page"

SELECTORS = {
    "business objectives": {
        "business objectives": Selector(
            By.CSS_SELECTOR,
            "#export-plan-dashboard > div:nth-child(2) > div > a > div.p-t-s.p-b-xs.p-h-xs",
        ),
        "why you want to export example": Selector(
            By.CSS_SELECTOR,
            "#objectives-reasons > div > div.learning > div.learning__buttons > button.button-example.button.button--small.button--tertiary.m-r-xxs.m-b-xs",
            # objectives-reasons > div > div.learning > div.learning__buttons.m-b-xs > button",
            type=ElementType.INPUT,
        ),
        "why you want to export": Selector(
            By.XPATH, "//textarea[@id='rationale']", type=ElementType.INPUT
        ),
        "objective text": Selector(
            By.CSS_SELECTOR,
            "#description"
            # "//body/main[@id='content']/div[@id='business-objectives-content']/section[4]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/textarea[1]"
            ,
            type=ElementType.TEXTAREA,
        ),
        "start date": Selector(
            By.CSS_SELECTOR,
            "#start_date",  # "//input[@id='start_date']"
            type=ElementType.INPUT,
        ),
        "end date": Selector(
            By.CSS_SELECTOR,
            "#end_date",  # "//input[@id='end_date']"
            type=ElementType.INPUT,
        ),
        "owner": Selector(
            By.CSS_SELECTOR,
            "#owner-0",  # "//input[@id='owner-0']"
            type=ElementType.INPUT,
        ),
        "planned review": Selector(
            By.CSS_SELECTOR,
            "#planned_reviews"
            # "//body/main[@id='content']/div[@id='business-objectives-content']/section[4]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/textarea[1]"
            ,
            type=ElementType.TEXTAREA,
        ),
        "yes checkbox": Selector(By.CSS_SELECTOR, "#section-complete > div > label"),
        "target markets research": Selector(
            By.XPATH, "//span[contains(text(),'Target markets research')]"
        ),
        "export plan home": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='business-objectives-content']/section[5]/div[1]/div[1]/div[2]/div[2]/a[1]",
        ),
        "is this opportunity right for you": Selector(
            By.XPATH, "//p[contains(text(),'Is this opportunity right for you?')]"
        ),
        "move from accidental exporting to strategic exporting": Selector(
            By.XPATH,
            "//body/main/div[2]/section[3]/div/div[2]/div/div/div/div[2]/a",
            # //*[@id=\"business-objectives-content\"]/section[4]/div/div[1]/div/a/div/p"
        ),
        "top export plan home": Selector(
            By.XPATH,
            "//body/main/div[2]/section[1]/div/div/div[2]/span/a/span"
            # business-objectives-content > section.section--intro.bg-blue-deep-90 > div > div > div.c-2-3-m.c-1-2-xl.p-t-xl.p-b-s.text-white > span > a > span"
        ),
        "open navigation": Selector(
            By.XPATH,
            "//body/main[@id='content']/div[@id='sidebar-content']/nav[@id='collapseNav']/div[1]/button[1]/i[1]",
        ),
        "nav target markets research": Selector(
            By.XPATH, "//body/main/div[1]/nav/div/ul/li[3]/a"
        ),
        "add goal": Selector(
            By.CSS_SELECTOR, "#objectives-form--objectives > div > button"
        ),
        "dashboard": Selector(By.XPATH, "//a[contains(text(),'Dashboard')]"),
        "move from accidental lesson": Selector(
            By.XPATH,
            "//body/main/div[2]/section[3]/div/div[2]/div/div/div/div[1]/button[2]",
        ),
    }
}


def visit(driver: WebDriver, *, page_name: str = None):
    go_to_url(driver, URL, page_name or NAME)


#
# def should_be_here(driver: WebDriver):
#     check_url(driver, URL, exact_match=False)


def should_be_here(driver: WebDriver):
    check_url_path_matches_template(URL, driver.current_url)


def enter_text(driver: WebDriver, element_name: str):
    text_element = find_element(driver, find_selector_by_name(SELECTORS, element_name))
    text_element.clear()
    text_element.send_keys("Automated tests")


def validate_entered_text(driver: WebDriver, element_name: str):
    text_element = find_element(driver, find_selector_by_name(SELECTORS, element_name))
    if "Automated tests" in text_element.text:
        return True
    return False


def find_and_click(driver: WebDriver, *, element_selector_name: str):
    find_and_click = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    find_and_click.click()


def enter_business_objectives_details(
    driver: WebDriver,
    position: str,
    objectives: str,
    owner: str,
    plannedreviews: str,
    element_selector_name: str,
):
    # every call of this function, click on Add Goal
    find_and_click(driver, element_selector_name="Add goal")
    time.sleep(1)
    objective_div_element_xpath = (
        "//body/main/div[2]/section[4]/div/div[2]/div/div/fieldset"
        + "["
        + position
        + "]"
    )
    objective_text_ele_xpath = objective_div_element_xpath + "div/div[1]/div/textarea"
    # //body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[1]/div/div/div[2]
    # //body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[1]/div/div/div[2]/div[4]/ul
    month_down_btn = driver.find_element_by_xpath(
        "//body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[1]/div/div/div[2]"
    )
    month_down_btn.click()
    driver.implicitly_wait(5)
    month_down_element = driver.find_element_by_xpath(
        "//body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[1]/div/div/div[2]/div[4]/ul"
    )
    li_elements = month_down_element.find_elements_by_tag_name("li")
    logging.debug("list elements")
    logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements) - 1)
    random_li_element = li_elements[random_number]
    logging.debug(random_number)
    logging.debug(random_li_element.tag_name)
    logging.debug(random_li_element)
    time.sleep(2)

    year_down_btn = driver.find_element_by_xpath(
        "//body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[2]/div/div/div[2]"
    )
    year_down_btn.click()
    driver.implicitly_wait(5)
    year_down_element = driver.find_element_by_xpath(
        "//body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[2]/div/div/div[2]/div[4]/ul"
    )
    li_elements = year_down_element.find_elements_by_tag_name("li")
    logging.debug("list elements")
    logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements) - 1)
    random_li_element = li_elements[random_number]
    logging.debug(random_number)
    logging.debug(random_li_element.tag_name)
    logging.debug(random_li_element)
    time.sleep(2)
    # //body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[2]/div/div/div[2]
    # //body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[2]/div/div/div[2]/div[4]/ul
    del_btn_ele_xpath = objective_div_element_xpath + "div/div[5]/button"
    find_and_select_random_month_list(driver, element_selector_name)
    find_and_select_random_year_list(driver, element_selector_name)
    # month_ele_xpath = objective_div_element_xpath + "/div[1]/div[2]/div[1]/div/div[2]/input"
    # year_ele_xpath = objective_div_element_xpath + "/div[1]/div[2]/div[2]/div/div[2]/input"
    owner_ele_xpath = objective_div_element_xpath + "/div/div[3]/div/div[2]/input"
    planned_reviews_ele_xpath = objective_div_element_xpath + "/div/div[4]/div/textarea"

    driver.find_element_by_xpath(objective_text_ele_xpath).send_keys(objectives)
    # driver.find_element_by_xpath(month_ele_xpath).send_keys(startdate)
    # driver.find_element_by_xpath(year_ele_xpath).send_keys(enddate)
    driver.find_element_by_xpath(owner_ele_xpath).send_keys(owner)
    driver.find_element_by_xpath(planned_reviews_ele_xpath).send_keys(plannedreviews)

    time.sleep(1)
    # input_field_selectors = SELECTORS["business objectives"]
    # input_details_dict = {"start date": startdate, "end date":enddate, "owner":owner}
    # fill_out_input_fields(driver, input_field_selectors, input_details_dict)
    #
    # text_area_details_dict = {"objective text": objectives, "planned review": plannedreviews}
    # fill_out_textarea_fields(driver, input_field_selectors, text_area_details_dict)


def find_and_select_random_month_list(driver: WebDriver, element_selector_name: str):
    drop_down_btn = driver.find_element_by_xpath(
        "//body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[1]/div/div/div[2]"
    )
    drop_down_btn.click()
    driver.implicitly_wait(5)
    drop_down_element = driver.find_element_by_xpath(
        "//body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[1]/div/div/div[2]/div[4]/ul"
    )
    li_elements = drop_down_element.find_elements_by_tag_name("li")
    logging.debug("list elements")
    logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements) - 1)
    random_li_element = li_elements[random_number]
    logging.debug(random_number)
    logging.debug(random_li_element.tag_name)
    logging.debug(random_li_element)
    time.sleep(2)


def find_and_select_random_year_list(driver: WebDriver, element_selector_name: str):
    drop_down_btn = driver.find_element_by_xpath(
        "//body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[2]/div/div/div[2]"
    )
    drop_down_btn.click()
    driver.implicitly_wait(5)
    drop_down_element = driver.find_element_by_xpath(
        "//body/main/div[2]/section[4]/div/div[2]/div/div/fieldset/div/div[2]/fieldset/div/div[2]/div/div/div[2]/div[4]/ul"
    )
    li_elements = drop_down_element.find_elements_by_tag_name("li")
    logging.debug("list elements")
    logging.debug(li_elements)
    random_number = 0
    if len(li_elements) > 2:
        random_number = random.randint(1, len(li_elements) - 1)
    random_li_element = li_elements[random_number]
    logging.debug(random_number)
    logging.debug(random_li_element.tag_name)
    logging.debug(random_li_element)
    time.sleep(2)


# def delete_all_business_objectives(driver: WebDriver, position: str):
#     objective_div_element_xpath = "//body/main[@id='content']/div[@id='business-objectives-content']/section[4]/div[1]/div[2]/div[2]/div[1]/div" + "[" + position + "]"
#     del_btn_ele_xpath = objective_div_element_xpath + "/div[2]/button[1]"
#
#     driver.find_element_by_xpath(del_btn_ele_xpath).click()
#     time.sleep(1)


# def enter_trip_details(driver: WebDriver, position: str, trip_name: str):
#     # every call of this function, click on Add Goal
#     find_and_click(driver, element_selector_name="Add a trip")
#     time.sleep(2)
#     document_div_element_xpath = "/html/body/main/div[2]/section[6]/div/div[2]/div/div[2]/table/tbody/tr" + "[" + position + "]"
#     document_text_ele_xpath = document_div_element_xpath + "/td/div/textarea"
#     driver.find_element_by_xpath(document_text_ele_xpath).send_keys(trip_name)
#     time.sleep(2)


def delete_all_business_objectives(driver: WebDriver, del_button_position: str):
    # 1,3,5,7,......
    # objective_div_element_xpath = "//body/main/div[2]/section[4]/div/div[2]/div[2]/div/div" + "[" + position + "]"
    # objective_text_ele_xpath = objective_div_element_xpath + "/div[1]/div[1]/div[1]/textarea[1]"
    # del_btn_ele_xpath = objective_div_element_xpath + "/div[2]/button[1]"
    # start_date_ele_xpath = objective_div_element_xpath + "/div[1]/div[2]/div[1]/div/div[2]/input"
    # end_date_ele_xpath = objective_div_element_xpath + "/div[1]/div[2]/div[2]/div/div[2]/input"
    # owner_ele_xpath = objective_div_element_xpath + "/div[1]/div[3]/div[1]/div[2]/input[1]"
    # planned_reviews_ele_xpath = objective_div_element_xpath + "/div[1]/div[4]/div[1]/textarea[1]"

    objective_text_area_element_index = int(del_button_position)
    # //body/main/div[2]/section[4]/div/div[2]/div[2]/div/div[5]/div[1]/div[1]/div/textarea
    objective_text_area_element_x_path = (
        "//body/main/div[2]/section[4]/div/div[2]/div[2]/div/div"
        + "["
        + str(objective_text_area_element_index)
        + "]"
        + "/div[1]/div[1]/div/textarea"
    )
    objective_text_area_text_exists = True
    time.sleep(2)
    # logging.debug(objective_text_area_element_index)
    # logging.debug(objective_text_area_element_x_path)
    try:
        objective_text_area_text = driver.find_element_by_xpath(
            objective_text_area_element_x_path
        ).text
        if objective_text_area_text == None or len(objective_text_area_text) <= 0:
            objective_text_area_text_exists = False
    except Exception as e:
        logging.error(e)
        objective_text_area_text_exists = False
    # /html/body/main/div[2]/section[4]/div/div[2]/div[2]/div/div[15]/div[2]/button/i
    # /html/body/main/div[2]/section[4]/div/div[2]/div[2]/div/div[5]/div[2]/button/i
    # /html/body/main/div[2]/section[4]/div/div[2]/div[2]/div/div[1]/div[2]/button/i
    # del_button_position: 5,4,3,2,1
    objective_div_element_xpath = (
        "//body/main/div[2]/section[4]/div/div[2]/div[2]/div/div"
        + "["
        + del_button_position
        + "]"
    )
    del_btn_ele_xpath = objective_div_element_xpath + "/div[2]/button"
    driver.find_element_by_xpath(del_btn_ele_xpath).click()
    # logging.debug("del_button_position " + str(del_button_position))
    # time.sleep(2)
    if objective_text_area_text_exists == True:
        driver.implicitly_wait(1)
        # 12,13,14,15.......
        # 12 + (1 - 1), 12 + (2 - 1), 12 + (3 - 1), 12 + (4 - 1),.........
        # /html/body/div[16]/div/div/div/div[2]/div[2]/button[1]/i
        # /html/body/div[13]/div/div/div/div[2]/div[2]/button[1]
        delete_msg_yes_index = int(12 + (int(del_button_position) - 1))
        delete_message_yes_element_xpath = (
            "//body/div"
            + "["
            + str(delete_msg_yes_index)
            + "]"
            + "/div/div/div/div[2]/div[2]/button[1]"
        )
        logging.debug(delete_message_yes_element_xpath)
        delete_message_yes_element = driver.find_element_by_xpath(
            delete_message_yes_element_xpath
        )
        delete_message_yes_element.click()
        # time.sleep(1)
    else:
        logging.debug(
            "objective_text_area_text_exists is False for del_button_position "
            + str(del_button_position)
        )


def check_section_complete_yes(driver: WebDriver, element_selector_name: str):
    check_yes_link = find_element(
        driver, find_selector_by_name(SELECTORS, element_selector_name)
    )
    check_yes_link.click()
