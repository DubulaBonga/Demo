Feature: Registration

  Scenario Outline: Registration Process
    Given the home page is open
    When the user clicks the register button
    And the user logs in with username "<username>", email "<email>", password "<password>" and confirm "<confirm password>"
    
    Examples:
      | username  |         email         | password  | confirm password |
      | tomsmith  | bongadubula@gmail.com | Heron@88% | P2ssword1        |

