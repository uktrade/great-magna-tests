@Great_Magna_Tests
@lessons-page
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page
#
  Background:
    Given test authentication is done
#
   @allure.link:XOT-101
   @Great-Magna-Lessons
  Scenario:User should be able to view lesson pages for topic "How lessons can help" and click continue
#https://auth_user:wxzapfhz19!x@great-magna.staging.uktrade.digital/
    Given "Robert" visits the "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
     When "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Learn to export"
     And "Robert" decides to click on section "Get Started" on page "LearnToExport - Learn Categories"
     And "Robert" decides to click on section "How lessons can help" on page "LearnToExport - Get Started"
     And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - How lessons can help"

 @allure.link:XOT-102
   @Great-Magna-Lessons
 Scenario:User should be able to view Lesson pages for topic "How lessons can help" and click back

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    When "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Get Started" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "How lessons can help" on page "LearnToExport - Get Started"
    And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - How lessons can help"


 @allure.link:XOT-103
   @Great-Magna-Lessons
 Scenario:User should be able to view Lesson pages for topic "How lessons can help" and click back

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Get Started" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "How lessons can help" on page "LearnToExport - Get Started"
    And "Robert" decides to click on section "Top Back" on page "LearnToExport - How lessons can help"

   @allure.link:XOT-104
   @Great-Magna-Lessons
    @get_started_6
 Scenario:User should be able to view Lesson page "What youll find in each lesson" and click continue 70 times

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Get Started" on page "LearnToExport - Learn Categories"
   And "Robert" decides to click on section "What youll find in each lesson" on page "LearnToExport - Get Started"
   And "Robert" decides to click continue for maximum "70" times from page "LearnToExport - What youll find in each lesson" until it reaches "managing-exchange-rates"
