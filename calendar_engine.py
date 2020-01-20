# Here the date format is generated
import datetime
from settings import months_by_number, GB_months_by_number, search_settings
from translator import Translate


class Calendar:
    def __init__(self):
        if not search_settings['today']:
            self.date = datetime.date.today() + datetime.timedelta(days=search_settings['delta'])
        else:
            self.date = datetime.datetime.now()
        self.day = self.date.day
        self.month = self.date.month
        self.year = self.date.year

    def search_this_date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_this_month_in_cyrillic(self):
        return months_by_number[self.month]

    def get_this_month_in_unicode(self):
        this_month_in_cyrillic = self.get_this_month_in_cyrillic()
        return Translate(cyrillic=this_month_in_cyrillic).translate_cyrillic_to_unicode()

    def get_date_locale_en_us(self):
        return "%d-%d" %(self.month, self.day)

    def get_this_month_in_english(self):
        return GB_months_by_number[self.month]
