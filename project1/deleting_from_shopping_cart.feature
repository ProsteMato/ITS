Feature: Deleting from Shopping Cart


    Scenario: Shopping cart is empty
        Given a web browser is at opencart homepage
        And schopping cart is empty
        When the user clicks on "Shopping Cart"
        Then the following text is shown "Your shopping cart is empty!"


    Scenario: Delete product from Shopping Cart
        Given a web browser is at shopping cart page
        And shopping cart contains one product
        When the user clicks on remove button in product row
        Then the shopping cart is empty


    Scenario: Delete product from Shopping Cart with quantity
        Given a web browser is at shopping cart page
        And shopping cart contains one product
        When user writes "0" in text field with name "quantity" in product row
        And user clicks on refresh button in product row
        Then the shopping cart is empty


    Scenario: Price of shopping cart when user deletes one of two not the same products
        Given a web browser is at shopping cart page
        And two not the same products and in shopping cart
        When the user clicks on remove button in one of the product rows
        Then total cost of shopping cart is equal to non-removed product


    Scenario: Products in shopping cart when user deletes one of two not the same products
        Given a web browser is at shopping cart page
        And two not the same products are in shopping cart
        When the user clicks on remove button in one of the products row
        Then in shopping cart is one product


    Scenario: Products in shopping cart when user deletes product with two quantity
        Given a web browser is at shopping cart page
        And two same products and in shopping cart
        When the user clicks on remove button in the product row
        Then the shopping cart is empty
