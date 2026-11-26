import runpy

import pytest


module = runpy.run_path("starter-code.py")
is_passing_score = module["is_passing_score"]
calculate_average = module["calculate_average"]
letter_grade = module["letter_grade"]


def test_passing_score():
    assert is_passing_score(70) is True
    assert is_passing_score(69) is False


@pytest.mark.parametrize(
    ("score", "expected"),
    [(95, "A"), (85, "B"), (75, "C"), (65, "D"), (55, "F")],
)
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_letter_grade_rejects_invalid_scores(score):
    with pytest.raises(ValueError):
        letter_grade(score)


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90


def test_calculate_average_rejects_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])
