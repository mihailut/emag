from behave import *


@when('fav: I click on first category')
def step_impl(context):
    context.favorites.click_first_category()


@when('fav: Adding product to fav')
def step_impl(context):
    context.favorites.add_to_fav()


@when('fav: I navigate to fav')
def step_impl(context):
    context.favorites.navigate_to_fav()


@then('fav: I check the item is in fav list')
def step_impl(context):
    context.favorites.check_fav_list()
