Feature: Select Visualization

As a user, select a visualization type and a dataset associated to user account and display a visualization

Scenario: User successfully creates a visualization
  Given user is logged in with username testuser and password testpass
  When user accesses /app/visualize/
  When user selects visualization type karma_by_sub
  And user types in dataset thisisbillgates
  And user clicks visualize
  Then display visualization

Scenario: User selects an invalid dataset handle
  Given user is logged in with username testuser and password testpass
  When user accesses /app/visualize/
  And user selects visualization type karma_by_sub
  And user types in dataset invalid_dataset
  And user clicks visualize
  Then display error
