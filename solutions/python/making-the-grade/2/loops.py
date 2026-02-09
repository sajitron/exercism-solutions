"""Functions for organizing and calculating student exam scores."""

PASS_THRESHOLD = 40

def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    rounded_scores = []

    for score in student_scores:
        rounded_scores.append(round(score))

    return rounded_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    
    failed_student_scores = []

    for score in student_scores:
        if score <= 40:
            failed_student_scores.append(score)

    return len(failed_student_scores)


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best_students = []

    for score in student_scores:
        if score >= threshold:
            best_students.append(score)

    return best_students


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    odd_increment = (highest - (PASS_THRESHOLD + 1)) // 4
    even_increment = ((highest - (PASS_THRESHOLD + 1)) // 4) + 1
    iterator = highest
    
    grade_thresholds = []

    for number in range(1, 5):
        if highest % 2 != 0 or number == 1:
            lower_threshold = iterator - odd_increment
            grade_thresholds.append(lower_threshold)
            iterator = lower_threshold
        else:
            lower_threshold = iterator - even_increment
            grade_thresholds.append(lower_threshold)
            iterator = lower_threshold

    grade_thresholds.reverse()
    return grade_thresholds
        

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    ranking = []

    for index, score in enumerate(student_scores):
        student_name = student_names[index]
        student_position = index + 1
        student_rank = str(student_position) + ". " + student_name + ": " + str(score)
        ranking.append(student_rank)

    return ranking


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    highest = []
    for student_score in student_info:
        if student_score[1] == 100:
            highest = student_score
            break

    return highest
