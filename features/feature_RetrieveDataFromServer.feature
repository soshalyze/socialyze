Feature: Retrieve Data From Server

As a user
I want to fetch data from a social media server

  Scenario: get a comment dataset
    Given user is logged in with username testuser and password testpass
    When user accesses /app/fetch/
    When user select reddit
    And user selects content comment
    And user enter thisisbillgates
    And user enters 10
    And send fetch request
    Then display /app/visualize/

  Scenario: get no dataset because of an invalid username
    Given user is logged in with username testuser and password testpass
    When user accesses /app/fetch/
    When user select reddit
    And user selects content comment
    And user enter ithinkidontexistdsfjvnsdjfghn
    And user enters 10
