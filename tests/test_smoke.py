"""
Smoke test
"""
import pytest
from selenium.webdriver.common.by import By


def test_product_view_sku(browser):
    """
    Test case WERT-1
    """
    url = "https://testqastudio.me"
    browser.get(url=url)

    element = browser.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()

    x_path_table = '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a'
    element = browser.find_element(By.XPATH, value=x_path_table)
    element.click()

    sku = browser.find_element(By.CLASS_NAME, value="sku")

    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"

@pytest.mark.smoke
def test_smoke(browser):
    """
    Test case SMK-1
    """
    url = "https://testqastudio.me"
    browser.get(url=url)
    