Feature: Check favorites

    Background:
      Given home: I am a user on emag.ro Home page

    @favorites
    Scenario: Add a product to favorites then check
      When fav: I click on first category
      When fav: Adding product to fav
      When fav: I navigate to fav
      Then fav: I check the item is in fav list
