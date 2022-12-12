from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Favorites(BasePage):
    FIRST_CATEGORY_BUTTON = (By.XPATH, '(//span[@class="megamenu-list-department__department-name"])[2]')
    ELEM_TO_BE_CLICKED = (By.XPATH, '//a[@data-id="4283"]')
    ADD_TO_FAV = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[2]/button[1]/i')
    NAVIGATE_TO_FAV = (By.XPATH, '//*[@id="my_wishlist"]/span[2]')
    CHECK_FAV = (By.XPATH, '//a[@class="product-title font-semi-bold js-product-url "]')

    def click_first_category(self):
        self.hover_by_selector(*self.FIRST_CATEGORY_BUTTON)
        self.wait_and_click_elem_by_selector(*self.ELEM_TO_BE_CLICKED)

    def add_to_fav(self):
        self.driver.find_element(*self.ADD_TO_FAV).click()

    def navigate_to_fav(self):
        self.driver.find_element(*self.NAVIGATE_TO_FAV).click()

    def check_fav_list(self):
        self.driver.get("https://www.emag.ro/favorites?ref=ua_favorites")
        # expected = self.verify_element_is_displayed_by_selector(*self.CHECK_FAV)
        # actual = self.verify_element_is_displayed_by_selector(*self.CHECK_FAV)
        # self.assertEqual(expected, actual, 'Not correct')

        # if self.verify_element_is_displayed_by_selector(*self.CHECK_FAV):
        #     print('The element we are looking for is displayed')
        # else:
        #     print('The element is not displayed')



