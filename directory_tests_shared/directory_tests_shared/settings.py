# -*- coding: utf-8 -*-
from datetime import datetime
from urllib.parse import urljoin

import requests
from django.conf import settings
from envparse import env
from lxml import etree


#####################################################################
# Directory Service URLs & Credentials
#####################################################################
def get_sitemap_urls(url):
    try:
        resp = requests.get(url)
        tree = etree.fromstring(resp.content)
        return [loc.text for loc in tree.findall("{*}url/{*}loc")]
    except requests.exceptions.RequestException:
        return []


SITE_MAP = env.str("SITE_MAP", default="/")
if SITE_MAP != "/":
    SITE_MAP_URLS = get_sitemap_urls(SITE_MAP)
    ADVICE_AND_MARKETS = [url for url in SITE_MAP_URLS if "/advice/" in url]
    MISC_ENDPOINTS = [url for url in SITE_MAP_URLS if "/advice/" not in url]
    if SITE_MAP_URLS:
        DOMESTIC_URL = SITE_MAP_URLS[0]
    else:
        DOMESTIC_URL = "/".join(SITE_MAP.split("/")[:-1])
else:
    DOMESTIC_URL = env.str("DOMESTIC_URL")


CMS_API_KEY = env.str("CMS_API_KEY", default="123456")
CMS_API_URL = env.str("CMS_API_URL", default="/")
CMS_API_CACHE_EXPIRE_SECONDS = env.int(
    "CMS_API_CACHE_EXPIRE_SECONDS", default=60 * 60 * 24 * 30
)  # 30 days
CMS_API_DEFAULT_TIMEOUT = env.int("CMS_API_DEFAULT_TIMEOUT", default=30)
CMS_API_SENDER_ID = env.str("CMS_API_SENDER_ID", default="directory")
CONTACT_US_URL = env.str("CONTACT_US_URL", default="/")
DIRECTORY_API_DEFAULT_TIMEOUT = env.int("DIRECTORY_API_DEFAULT_TIMEOUT", default=30)
DIRECTORY_API_KEY = env.str("DIRECTORY_API_KEY", default="123456")
DIRECTORY_API_SENDER_ID = env.str("DIRECTORY_API_SENDER_ID", default="directory")
DIRECTORY_API_HEALTH_CHECK_TOKEN = env.str(
    "DIRECTORY_API_HEALTH_CHECK_TOKEN", default="123456"
)
DIRECTORY_API_URL = env.str("DIRECTORY_API_URL", default="/")
ERP_URL = env.str("ERP_URL", default="/")
EVENTS_URL = env.str("EVENTS_URL", default="/")
EXPORT_OPPORTUNITIES_URL = env.str("EXPORT_OPPORTUNITIES_URL", default="/")
FIND_A_BUYER_URL = env.str("FIND_A_BUYER_URL", default="/")
FIND_A_SUPPLIER_URL = env.str("FIND_A_SUPPLIER_URL", default="/")
FORMS_API_KEY = env.str("FORMS_API_KEY", default="123456")
FORMS_API_SENDER_ID = env.str("FORMS_API_SENDER_ID", default="123456")
FORMS_API_URL = env.str("FORMS_API_URL", default="/")
GOV_NOTIFY_API_KEY = env.str(
    "GOV_NOTIFY_API_KEY",
    default="1234567891012345678910123456789101234567891012345678910123456789101234567891012345678910123456789101234567891012345678910",
)
PIR_GOV_NOTIFY_API_KEY = env.str(
    "PIR_GOV_NOTIFY_API_KEY",
    default="1234567891012345678910123456789101234567891012345678910123456789101234567891012345678910123456789101234567891012345678910",
)
INTERNATIONAL_URL = env.str("INTERNATIONAL_URL", default="/international/")
INVEST_URL = env.str("INVEST_URL", default="/")
ISD_URL = env.str(
    "ISD_URL", default=urljoin(INTERNATIONAL_URL, "investment-support-directory/")
)
LEGACY_CONTACT_US_URL = env.str("LEGACY_CONTACT_US_URL", default="/")
LEGACY_INVEST_URL = env.str("LEGACY_INVEST_URL", default="/")
PROFILE_URL = env.str("PROFILE_URL", default="/")
SOO_URL = env.str("SOO_URL", default="/")
SSO_API_KEY = env.str("SSO_API_KEY", default="123456")
SSO_API_URL = env.str("SSO_API_URL", default="/")
SSO_API_DEFAULT_TIMEOUT = env.int("SSO_API_DEFAULT_TIMEOUT", default=30)
SSO_API_SENDER_ID = env.str("SSO_API_SENDER_ID", default="directory")
SSO_URL = env.str("SSO_URL", default="/")


#####################################################################
# External Services
#####################################################################
BASICAUTH_PASS = env.str("BASICAUTH_PASS", default="test")
BASICAUTH_USER = env.str("BASICAUTH_USER", default="123456")

# BrowserStack
BROWSERSTACK_USER = env.str("BROWSERSTACK_USER", default="")
BROWSERSTACK_PASS = env.str("BROWSERSTACK_PASS", default="")
BROWSERSTACK_SERVER = env.str("BROWSERSTACK_SERVER", default="hub.browserstack.com")
BROWSERSTACK_SESSIONS_URL = "https://www.browserstack.com/automate/sessions/{}.json"
BROWSERSTACK_EXECUTOR_URL = (
    f"http://{BROWSERSTACK_USER}:{BROWSERSTACK_PASS}@{BROWSERSTACK_SERVER}/wd/hub"
)

# Mailhog
TEST_EMAIL_DOMAIN = env.str("TEST_EMAIL_DOMAIN", default="ci.uktrade.io")

#####################################################################
# Load test (locust.io) settings
#####################################################################
LOCUST_MAX_WAIT = env.int("LOCUST_MAX_WAIT", default=5000)
LOCUST_MIN_WAIT = env.int("LOCUST_MIN_WAIT", default=100)


#####################################################################
# Behave specific settings
#####################################################################
AUTO_RETRY = env.bool("AUTO_RETRY", default=True)
AUTO_RETRY_MAX_ATTEMPTS = env.int("AUTO_RETRY_MAX_ATTEMPTS", default=2)


#####################################################################
# Functional tests - specific settings
#####################################################################
USE_BASIC_AUTH = env.bool("USE_BASIC_AUTH", default=True)


#####################################################################
# Browser & BrowserStack related settings
#####################################################################
BARRED_USERS = list(filter(None, env.str("BARRED_USERS", default="").split(",")))
BROWSER = env.str("BROWSER", default="chrome")
BROWSER_CUSTOM_CAPABILITIES = env.dict("CAPABILITIES", default=None)
BROWSER_ENVIRONMENT = env.str("BROWSER_ENVIRONMENT", default="local")
BROWSER_HEADLESS = env.bool("HEADLESS", default=False)
BROWSER_RESTART_POLICY = env.str("RESTART_POLICY", default="feature")
BROWSER_TYPE = env.str("BROWSER_TYPE", default="desktop")
BROWSER_VERSION = env.str("VERSION", default=None)
BUILD_ID = env.str("CIRCLE_SHA1", default=datetime.isoformat(datetime.now()))
HUB_URL = env.str("HUB_URL", default=None)
TAKE_SCREENSHOTS = env.bool("TAKE_SCREENSHOTS", default=False)

if BROWSER_ENVIRONMENT.lower() == "remote" and (
    BROWSERSTACK_USER and BROWSERSTACK_PASS
):
    HUB_URL = BROWSERSTACK_EXECUTOR_URL


#####################################################################
# API clients settings
#####################################################################
settings.configure(
    DIRECTORY_API_CLIENT_API_KEY=DIRECTORY_API_KEY,
    DIRECTORY_API_CLIENT_BASE_URL=DIRECTORY_API_URL,
    DIRECTORY_API_CLIENT_DEFAULT_TIMEOUT=DIRECTORY_API_DEFAULT_TIMEOUT,
    DIRECTORY_API_CLIENT_SENDER_ID=DIRECTORY_API_SENDER_ID,
    DIRECTORY_CLIENT_CORE_CACHE_EXPIRE_SECONDS=CMS_API_CACHE_EXPIRE_SECONDS,
    DIRECTORY_CMS_API_CLIENT_API_KEY=CMS_API_KEY,
    DIRECTORY_CMS_API_CLIENT_BASE_URL=CMS_API_URL,
    DIRECTORY_CMS_API_CLIENT_CACHE_EXPIRE_SECONDS=CMS_API_CACHE_EXPIRE_SECONDS,
    DIRECTORY_CMS_API_CLIENT_DEFAULT_TIMEOUT=CMS_API_DEFAULT_TIMEOUT,
    DIRECTORY_CMS_API_CLIENT_SENDER_ID=CMS_API_SENDER_ID,
    DIRECTORY_CMS_API_CLIENT_SERVICE_NAME="EXPORT_READINESS",
    DIRECTORY_FORMS_API_BASE_URL=FORMS_API_URL,
    DIRECTORY_FORMS_API_API_KEY=FORMS_API_KEY,
    DIRECTORY_FORMS_API_SENDER_ID=FORMS_API_SENDER_ID,
    DIRECTORY_FORMS_API_DEFAULT_TIMEOUT=CMS_API_DEFAULT_TIMEOUT,
    DIRECTORY_SSO_API_CLIENT_API_KEY=SSO_API_KEY,
    DIRECTORY_SSO_API_CLIENT_BASE_URL=SSO_API_URL,
    DIRECTORY_SSO_API_CLIENT_DEFAULT_TIMEOUT=CMS_API_DEFAULT_TIMEOUT,
    DIRECTORY_SSO_API_CLIENT_SENDER_ID=CMS_API_SENDER_ID,
    CACHES={
        "cms_fallback": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "unique-snowflake",
        },
        "api_fallback": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "unique-snowflake",
        },
    },
)
