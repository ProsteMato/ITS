Feature: Checkout


    Scenario: Get to the checkout
        Given a web browser is at shopping cart page
        And in shopping cart are two items
        When user clicks on "Checkout" button
        Then page with title "Checkout" is shown


    Scenario: Guest checkout
        Given a web browser is at checkout page
        And in shopping cart are two items
        When user chooses Guest Checkout radio button
        And clicks on "Continue" button
        Then Step billing details expandes


    Scenario: Billing details
        Given a web browser is at checkout page
        And Step billing details is expanded
        When user writes his personal information and adress
        And clicks on "Continue" button
        Then Step payment method expandes


    Scenario: Payment method
        Given a web browser is at checkout page
        And Step payment method is expanded
        When user accepts Terms & Conditions
        And clicks on "Continue" button
        Then Step confirm order expandes


    Scenario: Confirm Order
        Given a web browser is at checkout page
        And Step confirm order expandes
        And item in shopping cart are in confirm order steps
        And total price is same as in shopping cart
        When user clicks on "Confirm Order" button
        Then page with title "Your order has been placed!" is shown
