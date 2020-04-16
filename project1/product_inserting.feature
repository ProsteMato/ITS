Feature: Adding product to Shopping Cart


    Scenario: Adding product to empty Shopping Cart
        Given a web browser is at opencart homepage
        And shopping cart is empty
        When the user adds the first product on homepage to Shopping Cart
        Then in shopping cart is chosen product


    Scenario: Show and Add product to empty Shopping Cart
        Given a web browser is at opencart homepage
        And shopping cart is empty
        When user open product detail of first product on homepage
        And adds the product to shopping cart
        Then in shopping cart is chosen product
    
    
    Scenario: Adding product to non-empty Shopping Cart
        Given a web browser is at opencart homepage
        And in shopping cart is first product of homepage
        When the user adds the second product of homepage to shopping cart
        Then in shopping cart are first and second product of homepage


    Scenario: Adding product to Shopping Cart that is already in there
        Given a web browser is at opencart homepage
        And in shopping cart is first product of the homepage
        When user adds the first product of the homepage
        Then shopping cart have two same items


    Scenario: Adding product to Shopping Cart with quantity
        Given a web browser is at shopping cart page
        And in shopping cart is one item
        When user writes "2" in text field with name "quantity" in product row
        And user clicks on refresh button in product row
        Then shopping cart have two same items


    Scenario: Price of shopping cart
        Given a web browser is at opencart homepage
        And shopping cart is empty
        When the user adds the first product on homepage to Shopping Cart
        Then the shopping cart have total price equal to chosen product

    
    Scenario: Price of shopping cart when adding to non-empty shopping cart
        Given a web browser is at opencart homepage
        And is shopping cart is first product of homepage
        When user adds the second product of homepage
        Then total price of shopping cart is equal to sum of first and second product


    Scenario: Total price of shopping cart when adding through quantity
        Given a web browser is at shopping cart page
        And in shopping cart is one product
        When user writes "2" in text field with name "quantity" in product row
        And user clicks on refresh button in product row
        Then Total price in shopping cart is equal to total price in product row


    Scenario: Price of product row in shopping cart when adding through quantity
        Given a web browser is at shopping cart page
        And in shopping cart is one product
        When user writes "2" in text field with name "quantity" in product row
        And user clicks on refresh button in product row
        Then Total price in product row is two times bigger than in unit price
