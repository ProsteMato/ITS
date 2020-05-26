Feature: Deleting from Shopping Cart


    Scenario: Shopping cart is empty
        Given a web browser is at opencart homepage
        And shopping cart is empty
        When the user clicks on "Shopping Cart"
        Then the following text is shown "Your shopping cart is empty!"


    Scenario: Delete product from Shopping Cart
        Given a web browser is at shopping cart page
        And in shopping cart is one item
        When the user clicks on remove button in product row
        Then the shopping cart is empty


    Scenario: Delete product from Shopping Cart with quantity
        Given a web browser is at shopping cart page
        And in shopping cart is one item
        When user writes "0" in text field with name quantity in product row
        And user clicks on refresh button in product row
        Then the shopping cart is empty


    Scenario: Price of shopping cart when user deletes one of two not the same products
        Given a web browser is at shopping cart page
        And two not the same products are in shopping cart
        When the user remove first product in shopping cart
        Then total cost of shopping cart is equal to non-removed product


    Scenario: Products in shopping cart when user deletes product with two quantity
        Given a web browser is at shopping cart page
        And two same products and in shopping cart
        When the user clicks on remove button in product row
        Then the shopping cart is empty
