# -*- coding: utf-8 -*-
from datetime import datetime
from urllib.parse import urljoin

from django.conf import settings
from envparse import env

GREAT_MAGNA_URL = env.str(
    "GREAT_MAGNA_URL", default="https://great.dev.uktrade.digital/"
)
GREAT_MAGNA_URL_LANDING = env.str(
    "GREAT_MAGNA_URL_LANDING", default="https://great.dev.uktrade.digital/dashboard"
)
# INVEST_ATLAS_URL = env.str("INVEST_ATLAS_URL",default="https://great.uat.uktrade.digital/international/")

# GREAT_MAGNA_URL = env.str("GREAT_MAGNA_URL", default="https://great-magna.dev.uktrade.digital/")
# GREAT_MAGNA_URL_LANDING = env.str("GREAT_MAGNA_URL_LANDING", default="https://great-magna.dev.uktrade.digital/dashboard")
# GREAT_MAGNA_URL = env.str("GREAT_MAGNA_URL", default="https://great-magna.staging.uktrade.digital/")
# # GREAT_MAGNA_URL_LANDING = env.str("GREAT_MAGNA_URL_LANDING",
#                                   default="https://great-magna.staging.uktrade.digital/dashboard")
# TOKEN ="https://magna-beta.great.uktrade.digital/signup?enc=gAAAAABgF-Gia1slIhrlp4r6x3BdqsFCnpp1VRANWAhb6fDX_VnPi8iDIaXNYceAq-Z7e234b77gF-_HlPmQue6L47pnvKr46xU6s22ZC-4m8En3V4uISwY="
#
# GREAT_MAGNA_URL = env.str("GREAT_MAGNA_URL", default="https://magna-beta.great.uktrade.digital/signup?enc=gAAAAABgF-Gia1slIhrlp4r6x3BdqsFCnpp1VRANWAhb6fDX_VnPi8iDIaXNYceAq-Z7e234b77gF-_HlPmQue6L47pnvKr46xU6s22ZC-4m8En3V4uISwY=")
# GREAT_MAGNA_URL_LANDING = env.str("GREAT_MAGNA_URL_LANDING", default="https://magna-beta.great.uktrade.digital/signup?enc=gAAAAABgF-Gia1slIhrlp4r6x3BdqsFCnpp1VRANWAhb6fDX_VnPi8iDIaXNYceAq-Z7e234b77gF-_HlPmQue6L47pnvKr46xU6s22ZC-4m8En3V4uISwY=")


#####################################################################
# Directory Service URLs & Credentials
#####################################################################
CMS_API_KEY = env.str("CMS_API_KEY")
CMS_API_URL = env.str("CMS_API_URL")
CMS_API_CACHE_EXPIRE_SECONDS = env.int(
    "CMS_API_CACHE_EXPIRE_SECONDS", default=60 * 60 * 24 * 30
)  # 30 days
CMS_API_DEFAULT_TIMEOUT = env.int("CMS_API_DEFAULT_TIMEOUT", default=30)
CMS_API_SENDER_ID = env.str("CMS_API_SENDER_ID", default="directory")
CONTACT_US_URL = env.str("CONTACT_US_URL")
DIRECTORY_API_DEFAULT_TIMEOUT = env.int("DIRECTORY_API_DEFAULT_TIMEOUT", default=30)
DIRECTORY_API_KEY = env.str("DIRECTORY_API_KEY")
DIRECTORY_API_SENDER_ID = env.str("DIRECTORY_API_SENDER_ID", default="directory")
DIRECTORY_API_HEALTH_CHECK_TOKEN = env.str("DIRECTORY_API_HEALTH_CHECK_TOKEN")
DIRECTORY_API_URL = env.str("DIRECTORY_API_URL")
DOMESTIC_URL = env.str("DOMESTIC_URL")
ERP_URL = env.str("ERP_URL")
EVENTS_URL = env.str("EVENTS_URL")
EXPORT_OPPORTUNITIES_URL = env.str("EXPORT_OPPORTUNITIES_URL")
FIND_A_BUYER_URL = env.str("FIND_A_BUYER_URL")
FIND_A_SUPPLIER_URL = env.str("FIND_A_SUPPLIER_URL")
FORMS_API_KEY = env.str("FORMS_API_KEY")
FORMS_API_SENDER_ID = env.str("FORMS_API_SENDER_ID")
FORMS_API_URL = env.str("FORMS_API_URL")
GOV_NOTIFY_API_KEY = env.str("GOV_NOTIFY_API_KEY")
PIR_GOV_NOTIFY_API_KEY = env.str("PIR_GOV_NOTIFY_API_KEY")
INTERNATIONAL_URL = env.str("INTERNATIONAL_URL")
INVEST_URL = env.str("INVEST_URL")
ISD_URL = env.str(
    "ISD_URL", default=urljoin(INTERNATIONAL_URL, "investment-support-directory/")
)
LEGACY_CONTACT_US_URL = env.str("LEGACY_CONTACT_US_URL")
LEGACY_INVEST_URL = env.str("LEGACY_INVEST_URL")
PROFILE_URL = env.str("PROFILE_URL")
SOO_URL = env.str("SOO_URL")
# SSO_API_KEY = env.str("SSO_API_KEY")
# SSO_API_URL = env.str("SSO_API_URL")
# SSO_API_DEFAULT_TIMEOUT = env.int("SSO_API_DEFAULT_TIMEOUT", default=30)
# SSO_API_SENDER_ID = env.str("SSO_API_SENDER_ID", default="directory")
# SSO_URL = env.str("SSO_URL")

#####################################################################
# External Services
#####################################################################
BASICAUTH_PASS = env.str("BASICAUTH_PASS", default="Testing@123!")
BASICAUTH_USER = env.str("BASICAUTH_USER", default="santoshtesting10008+888@gmail.com")

# BrowserStack
BROWSERSTACK_USER = env.str("BROWSERSTACK_USER", default="")
BROWSERSTACK_PASS = env.str("BROWSERSTACK_PASS", default="")
BROWSERSTACK_SERVER = env.str("BROWSERSTACK_SERVER", default="hub.browserstack.com")
BROWSERSTACK_SESSIONS_URL = "https://www.browserstack.com/automate/sessions/{}.json"
BROWSERSTACK_EXECUTOR_URL = (
    f"http://{BROWSERSTACK_USER}:{BROWSERSTACK_PASS}@{BROWSERSTACK_SERVER}/wd/hub"
)

# SSO
SSO_API_KEY = env.str(
    "SSO_API_KEY",
    default="P6rjCi85RMen95D2G&4cS6QkkDNAOydjZS8oDUN@Hk^pbfH%JNMI%%26$a7p4QMM9&bs9bHu9xGSOn7a#iX*Ji9K1P4E5dwwgtLR",
)
SSO_API_URL = env.str("SSO_API_URL")
SSO_API_DEFAULT_TIMEOUT = env.int("SSO_API_DEFAULT_TIMEOUT", default=30)
SSO_API_SENDER_ID = env.str("SSO_API_SENDER_ID", default="directory")
SSO_URL = env.str("SSO_URL")

# Mailhog
TEST_EMAIL_DOMAIN = env.str("TEST_EMAIL_DOMAIN", default="ci.uktrade.io")
#####################################################################
# Load test (locust.io) settings
#####################################################################
LOCUST_MAX_WAIT = env.int("LOCUST_MAX_WAIT", default=2000)  # 5000
LOCUST_MIN_WAIT = env.int("LOCUST_MIN_WAIT", default=5)  # 100

#####################################################################
# Behave specific settings
#####################################################################
AUTO_RETRY = env.bool("AUTO_RETRY", default=False)  # True
AUTO_RETRY_MAX_ATTEMPTS = env.int("AUTO_RETRY_MAX_ATTEMPTS", default=1)  # 2

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
TAKE_SCREENSHOTS = env.bool("TAKE_SCREENSHOTS", default=True)  # default=False)

if BROWSER_ENVIRONMENT.lower() == "remote" and (
    BROWSERSTACK_USER and BROWSERSTACK_PASS
):
    HUB_URL = BROWSERSTACK_EXECUTOR_URL

######################################################################
# Email Server
#######################################################################
TEST_EMAIL_DOMAIN = env.str("TEST_EMAIL_DOMAIN", default="ci.uktrade.io")

DEV_GMAIL_HOST = "imap.gmail.com"
# Sign_Up feature Test data
EMAIL_SEARCH_SUBJECT = "Your confirmation code for great.gov.uk"
EMAIL_SEARCH_CRITERIA = "Your confirmation code is "
EMAIL_FETCH_COUNT = 1
CONFIRMATION_CODE_LENGTH = 5

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
    # DIRECTORY_CMS_API_CLIENT_SENDER_ID="Great-Magna",
    DIRECTORY_CMS_API_CLIENT_SENDER_ID=CMS_API_SENDER_ID,
    DIRECTORY_CMS_API_CLIENT_SERVICE_NAME="EXPORT_READINESS",
    DIRECTORY_FORMS_API_BASE_URL=FORMS_API_URL,
    DIRECTORY_FORMS_API_API_KEY=FORMS_API_KEY,
    DIRECTORY_FORMS_API_SENDER_ID=FORMS_API_SENDER_ID,
    DIRECTORY_FORMS_API_DEFAULT_TIMEOUT=CMS_API_DEFAULT_TIMEOUT,
    DIRECTORY_SSO_API_CLIENT_API_KEY=SSO_API_KEY,
    DIRECTORY_SSO_API_CLIENT_BASE_URL=SSO_API_URL,
    # DIRECTORY_SSO_API_CLIENT_DEFAULT_TIMEOUT=30,
    # DIRECTORY_SSO_API_CLIENT_SENDER_ID="Great-Magna",
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
