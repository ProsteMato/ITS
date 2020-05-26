from behave import *
from selenium.webdriver.common.keys import Keys


@given("a web browser is at opencart homepage")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/")


@when("user clicks on first product on homepage")
def step_impl(context):
    context.product_name = context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .caption a").text
    context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .caption a").click()


@when('user clicks on product "{product_name}"')
def step_impl(context, product_name):
    context.driver.find_element_by_link_text(product_name).click()


@then("page with product detail is shown")
def step_impl(context):
    product_detail_name = context.driver.find_element_by_css_selector("h1").text
    assert product_detail_name == context.product_name


@then('page with title "{page_title}" is shown')
def step_impl(context, page_title):
    assert context.driver.title == page_title


@when('user searches for product "{product_name}"')
def step_impl(context, product_name):
    search_bar = context.driver.find_element_by_name("search")
    search_bar.send_keys(product_name)
    search_bar.send_keys(Keys.ENTER)
    context.chosen_product = product_name


@then("page with products related to searched product are shown")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then page with products related to searched product are shown.')


@when('user clicks on "{category_name}" category')
def step_impl(context, category_name):
    context.driver.find_element_by_link_text(category_name).click()


@step("chooses first sub-category")
def step_impl(context):
    context.sub_category = context.driver.find_element_by_css_selector(".open .list-unstyled:nth-child(1) > li:nth-child(1) > a").text
    context.driver.find_element_by_css_selector(".open .list-unstyled:nth-child(1) > li:nth-child(1) > a").click()


@then("page with of first sub-category is shown")
def step_impl(context):
    assert context.sub_category[:-4] == context.driver.title


@then("page with products related to searched product are shown.")
def step_impl(context):
    assert context.driver.find_element_by_css_selector("h1").text == "Result for product: " + context.chosen_product
