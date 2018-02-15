from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Firefox(executable_path=r'C:\Users\pruthvi\Downloads\geckodriver.exe')

def get_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


def clear_cache(driver, timeout=60):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')

    # wait for the button to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(get_clear_browsing_button)

    # click the button to clear the cache
    get_clear_browsing_button(driver).click()

    # wait for the button to be gone before returning
    wait.until_not(get_clear_browsing_button)

for i in range(50):
	try:
		clear_cache(driver)
		driver.get("https://strawpoll.com/#####");

		driver.implicitly_wait(3) # seconds

		#WebElement radioBtn1 = driver.find_element_by_id("check5");
		driver.execute_script("document.getElementById('check#').click()")
		driver.execute_script("document.getElementById('votebutton').click()")
	except:
		continue
driver.close()
#((JavascriptExecutor) driver).executeScript("arguments[0].checked = true;", radioBtn1);



