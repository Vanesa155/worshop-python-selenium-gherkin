Feature: Shopping Cart and Purchase

  Scenario: Add to cart and complete purchase
    Given the user is on the login page
    When the user logs in with valid credentials
    And the user adds an item to the cart
    And the item should be added to the cart
    And the user should be redirected shopping page and enters their information
    And the user completes the purchase
    Then the order should be completed successfully
