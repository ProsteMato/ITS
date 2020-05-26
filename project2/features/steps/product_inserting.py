import selenium
from behave import *
from re import sub
from decimal import Decimal


@step("shopping cart is empty")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    while context.driver.find_element_by_xpath("//div[@id='content']/p").text != "Your shopping cart is empty!":
        context.driver.find_element_by_css_selector("tr:nth-child(1) > .text-left .btn-danger > .fa").click()
        context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    context.driver.get("http://mys01.fit.vutbr.cz:8045")


@when("the user adds the first product on homepage to Shopping Cart")
def step_impl(context):
    context.chosen_product = context.chosen_product = context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .caption a").text
    context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .fa-shopping-cart").click()


@then("in shopping cart is chosen product")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    assert context.driver.find_element_by_link_text(context.chosen_product) is not None


@when("user open product detail of first product on homepage")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045")
    chosen_product = context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .caption a")
    context.chosen_product = chosen_product.text
    chosen_product.click()


@step("adds the product to shopping cart")
def step_impl(context):
    context.driver.find_element_by_id("button-cart").click()


@step("in shopping cart is first product of homepage")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    while context.driver.find_element_by_xpath("//div[@id='content']/p").text != "Your shopping cart is empty!":
        context.driver.find_element_by_css_selector("tr:nth-child(1) > .text-left .btn-danger > .fa").click()
        context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    context.driver.get("http://mys01.fit.vutbr.cz:8045")
    context.chosen_product = context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .caption a").text
    context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .fa-shopping-cart").click()


@when("the user adds the second product of homepage to shopping cart")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045")
    context.second_chosen_product = context.driver.find_element_by_css_selector(".product-layout:nth-child(2) .caption a").text
    context.driver.find_element_by_css_selector(".product-layout:nth-child(2) .fa-shopping-cart").click()


@then("in shopping cart are first and second product of homepage")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    assert context.driver.find_element_by_link_text(context.chosen_product) is not None
    assert context.driver.find_element_by_link_text(context.second_chosen_product) is not None


@when("user adds the first product of the homepage")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045")
    context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .fa-shopping-cart").click()


@step("in shopping cart is one item")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    while context.driver.find_element_by_xpath("//div[@id='content']/p").text != "Your shopping cart is empty!":
        context.driver.find_element_by_css_selector("tr:nth-child(1) > .text-left .btn-danger > .fa").click()
        context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    context.driver.get("http://mys01.fit.vutbr.cz:8045")
    context.chosen_product = context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .caption a").text
    context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .fa-shopping-cart").click()


@then("shopping cart have two same items")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    assert context.driver.find_element_by_css_selector("tr:nth-child(1) .form-control").get_attribute('value') == "2"


@given("a web browser is at shopping cart page")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")


@when('user writes "{number}" in text field with name quantity in product row')
def step_impl(context, number):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    context.driver.find_element_by_css_selector("tr:nth-child(1) .form-control").clear()
    context.driver.find_element_by_css_selector("tr:nth-child(1) .form-control").send_keys(number)


@step("user clicks on refresh button in product row")
def step_impl(context):
    context.driver.find_element_by_css_selector(".fa-refresh").click()


@then("the shopping cart have total price equal to chosen product")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    product_price = context.driver.find_element_by_css_selector("tbody .text-right:nth-child(6)").text
    assert context.driver.find_element_by_css_selector(".col-sm-4 tr:nth-child(4) > .text-right:nth-child(2)").text == product_price


@then("total price of shopping cart is equal to sum of first and second product")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    product_price = Decimal(sub(r'[^\d.]', '', context.driver.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-right:nth-child(6)").text))
    product_price2 = Decimal(sub(r'[^\d.]', '', context.driver.find_element_by_css_selector("tbody > tr:nth-child(2) > .text-right:nth-child(6)").text))
    total_price = product_price + product_price2
    assert Decimal(sub(r'[^\d.]', '', context.driver.find_element_by_css_selector(".col-sm-4 tr:nth-child(4) > .text-right:nth-child(2)").text)) == total_price


@then("Total price in product row is two times bigger than in unit price")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    unit_price = Decimal(sub(r'[^\d.]', '', context.driver.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-right:nth-child(5)").text))
    total_price = Decimal(sub(r'[^\d.]', '', context.driver.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-right:nth-child(6)").text))
    assert 2 * float(unit_price) == float(total_price)
