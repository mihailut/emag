from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    TOTAL_PRICE_BIG = (By.XPATH, '//*[@id="cartProductsPage"]/div[1]/div[1]/div/div[3]/p/span[1]')
    TOTAL_PRICE_SMALL = (By.XPATH, '//*[@id="cartProductsPage"]/div[1]/div[1]/div/div[3]/p/sup')
    STERGE_LINK = (By.XPATH, '//a[contains(text(), "Sterge")]')
    COSUL_TAU_ESTE_GOL_MSG = (By.XPATH, '//div[text()="Cosul tau este gol"]')
    CHECKOUT_BTN = (By.XPATH, '(//a[@href="/cart/checkout"])[1]')

    def verify_total_price(self, expected_price):
        big = self.driver.find_element(*self.TOTAL_PRICE_BIG).text
        small = self.driver.find_element(*self.TOTAL_PRICE_SMALL).text
        print(small)
        actual = big + small
        self.assertEqual(actual, expected_price, "Price is incorrect")

    def click_sterge_link(self):
        self.wait_and_click_elem_by_selector(*self.STERGE_LINK)

    def verify_empty_cart_msg(self):
        self.verify_element_is_displayed_by_selector(*self.COSUL_TAU_ESTE_GOL_MSG)

    def click_checkout_btn(self):
        self.wait_and_click_elem_by_selector(*self.CHECKOUT_BTN)










