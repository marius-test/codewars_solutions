# Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw return Draw!.

## Examples(Input1, Input2 --> Output):

```text
"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
```

### Given Code

```python
def rps(p1, p2):
    #your code here
```

### Sample Tests

```python
import codewars_test as test
from solution import rps

@test.describe("rock paper scissors")
def basic_tests():
    @test.it("Player 1 wins")
    def player_1():
        test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
    @test.it("Player 2 wins")
    def player_1():
        test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
    @test.it("Draw")
    def draw():
        test.assert_equals(rps('rock', 'rock'), 'Draw!')
```
