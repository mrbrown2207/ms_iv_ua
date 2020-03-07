from django.test import SimpleTestCase
from home.constants import NO_BOTS


class TestNoBots(SimpleTestCase):
    """
    Test that our array of random no bot questions is valid.
    This gives us the ability to easily add additional ones
    later. This does assume a delimiter of ' and '
    """
    def test_no_bot_questions_sum_equals_answer(self):
        for k, v in NO_BOTS.items():
            li = list(k.split(" and "))
            li = [int(i) for i in li]
            assert sum(li) == int(v)

