from behave import *


@when('the user clicks on "Shopping Cart"')
def step_impl(context):
    context.driver.find_element_by_css_selector("a > .fa-shopping-cart").click()


@then('the following text is shown "{text}"')
def step_impl(context, text):
    assert context.driver.find_element_by_xpath("//div[@id='content']/p").text == text


@when("the user clicks on remove button in product row")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    context.driver.find_element_by_css_selector("tr:nth-child(1) > .text-left .btn-danger > .fa").click()
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")


@then("the shopping cart is empty")
def step_impl(context):
    assert context.driver.find_element_by_xpath("//div[@id='content']/p").text == "Your shopping cart is empty!"


@step("two not the same products are in shopping cart")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045")
    context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .fa-shopping-cart").click()
    context.driver.find_element_by_css_selector(".product-layout:nth-child(2) .fa-shopping-cart").click()
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")


@when("the user remove first product in shopping cart")
def step_impl(context):
    context.driver.find_element_by_css_selector("tr:nth-child(1) > .text-left .btn-danger > .fa").click()
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")


@then("total cost of shopping cart is equal to non-removed product")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")
    product_price = context.driver.find_element_by_css_selector("tbody > tr:nth-child(1) > .text-right:nth-child(6)").text
    assert context.driver.find_element_by_css_selector(".col-sm-4 tr:nth-child(4) > .text-right:nth-child(2)").text == product_price


@then("in shopping cart is one product")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then in shopping cart is one product')


@step("two same products and in shopping cart")
def step_impl(context):
    context.driver.get("http://mys01.fit.vutbr.cz:8045")
    context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .fa-shopping-cart").click()
    context.driver.find_element_by_css_selector(".product-layout:nth-child(1) .fa-shopping-cart").click()
    context.driver.get("http://mys01.fit.vutbr.cz:8045/index.php?route=checkout/cart")