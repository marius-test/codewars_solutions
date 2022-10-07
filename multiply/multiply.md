# Multiply

This code does not execute properly. Try to figure out why.

## Given Code

```python
def multiply(a, b):
    a * b
```

## Sample Tests

```python
import codewars_test as test
from solution import multiply

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(multiply(2,1), 2)
```
