# 📘 Assignment: Python Testing with pytest

## 🎯 Objective

Practice writing and running automated tests in Python with pytest by checking normal cases, edge cases, and fixing bugs in a grade-calculation utility.

## 📝 Tasks

### 🛠️ Write Basic Tests

#### Description
Use pytest assertions to test whether individual functions return the expected values.

#### Requirements
Completed program should:

- Add tests in `test-starter-code.py` for the `is_passing_score()` function.
- Verify that a score of 70 is passing.
- Verify that a score of 69 is not passing.
- Run the suite with `pytest test_starter_code.py`.

Example assertion:

```python
assert is_passing_score(70) is True
```

### 🛠️ Cover Edge Cases

#### Description
Use parametrized tests to check a function across several inputs and test validation behavior.

#### Requirements
Completed program should:

- Use `pytest.mark.parametrize` to test at least four letter-grade boundaries.
- Verify that `letter_grade(90)` returns `"A"` and `letter_grade(80)` returns `"B"`.
- Raise `ValueError` when `letter_grade()` receives a score below 0 or above 100.
- Test both invalid ranges with `pytest.raises`.

### 🛠️ Debug a Function

#### Description
Run the complete test suite and fix the implementation until every test passes.

#### Requirements
Completed program should:

- Inspect the failing test output instead of changing tests to hide failures.
- Fix `calculate_average()` so it returns the correct average for a list of numbers.
- Fix `letter_grade()` so it follows standard descending grade boundaries.
- Pass all tests in `test-starter-code.py`.
