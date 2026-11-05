from enum import Enum

class StudentAction(Enum):
    """
    ==========================================================
                    Student Actions
    ==========================================================

    Every interaction during Lecture Mode is represented
    by one of these actions.

    The frontend sends an action.

    The Lecture Engine decides what to do.
    """

    START = "START"

    CONTINUE = "CONTINUE"

    PAUSE = "PAUSE"

    RESUME = "RESUME"

    FINISH = "FINISH"

    EXPLAIN_AGAIN = "EXPLAIN_AGAIN"

    MORE_DETAIL = "MORE_DETAIL"

    SIMPLIFY = "SIMPLIFY"

    EXAMPLE = "EXAMPLE"

    MORE_EXAMPLES = "MORE_EXAMPLES"

    PREVIOUS = "PREVIOUS"

    NEXT = "NEXT"

    JUMP = "JUMP"

    STATUS = "STATUS"

    PROGRESS = "PROGRESS"

    DISCUSSION = "DISCUSSION"

    ASK_QUESTION = "ASK_QUESTION"

    QUIZ = "QUIZ"

    REVIEW = "REVIEW"

    EXIT = "EXIT"