# Reverse words

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

## Example

```text
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```

### Given Code

```python
def reverse_words(text):
    pass #go for it
```

### Sample Tests

```python
import codewars_test as test
from solution import reverse_words

@test.describe("Sample Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god', "Input: 'The quick brown fox jumps over the lazy dog.'")
        test.assert_equals(reverse_words('apple'), 'elppa', "Input: 'apple'")
        test.assert_equals(reverse_words('a b c d'), 'a b c d', "Input: 'a b c d'")
        test.assert_equals(reverse_words('  double  spaced  words  '), '  elbuod  decaps  sdrow  ', "Input: '  double  spaced  words  '")
```
