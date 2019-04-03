Feature: Test login

Scenario: Test Successful Login
Given I am on the login page
And I enter valid credentials
Then I should see a login successful alert

Scenario: Test Invalid Email
Given I am on the login page
And I enter an invalid email
Then I should see an invalid email message

Scenario: Test Invalid Password Attempts
Given I am on the login page
And I enter a valid email
And I enter an invalid password

Scenario: Test Need Help? Link
Given I am on the login page
And I click on the Need Help link
Then I should be taken to the FAQ page
