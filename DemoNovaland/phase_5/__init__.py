import psycopg2
from otree.api import *
from datetime import *
from datetime import time
import datetime
import time

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'phase_5'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Waiting_Site(Page):
    @staticmethod
    def is_displayed(player: Player):
        Zeit = 18 * 60 * 60
        ProgrammTagZeit = (datetime.now().time().hour * 60 * 60) + (
                datetime.now().time().minute * 60) + datetime.now().time().second
        differenz = Zeit - ProgrammTagZeit
        if differenz > 0:
            return True
        else:
            return False

class Phase_5_Page_1(Page):
    pass


class Phase_5_Page_2(Page):
    pass


class Phase_5_Page_3(Page):
    pass


class Phase_5_Page_4(Page):
    pass


class Phase_5_Page_5(Page):
    pass


class Phase_5_Page_6(Page):
    pass


class Phase_5_Page_7(Page):
    pass


class Phase_5_Page_8(Page):
    pass


class Phase_5_Page_9(Page):
    pass


class Phase_5_Page_10(Page):
    pass


class Phase_5_Page_11(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
