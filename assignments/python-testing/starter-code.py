def is_passing_score(score):
    return score >= 70


def calculate_average(scores):
    # TODO: Return the average of the scores.
    # This implementation contains an incorrect bug.
    if not scores:
        raise ValueError("Scores cannot be empty")
    return sum(scores)


def letter_grade(score):
    # TODO: Validate the score and return the correct letter grade.
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
