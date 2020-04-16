Feature: Searching product


    Scenario: Show product detail
        Given a web browser is at opencart homepage
        When user clicks on first product on homepage
        Then page with product detail is shown


    Scenario: Title of product detail
        Given a web browser is at opencart homepage
        When user clicks on product "Canon EOS 5D"
        Then page with title "Canon EOS 5D" is shown


    Scenario: Search product
        Given a web browser is at opencart homepage
        When user searchs for product "iPhone"
        Then page with products related to searched product are shown.


    Scenario: Show Tablets category
        Given a web browser is at opencart homepage
        When user clicks on "Tables" category
        Then page with title "Tablets" is shown


    Scenario: Show sub-category
        Given a web browser is at opencart homepage
        When user clicks on "MP3 Players"
        And chooses first sub-category
        Then page with title of chosen sub-category is shown
    