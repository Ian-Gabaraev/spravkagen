# This class requests Wikipedia pages, from which it then extracts
# information about the events that happened on a certain day
# and people born that day.
# The information about events and birthdays is stored separately in OrderedDict's
# and can be returned by creating and instance of the class
# and calling the respective methods:
# type(OrderedDict) object.get_events() & type(OrderedDict) object.get_birthdays()
# KuverTech. Finished Jan, 16, 2020.

from calendar_engine import Calendar
from settings import wiki_snippet_birthdays, wiki_snippet_events
from bs4 import BeautifulSoup
from collections import OrderedDict
import requests
import random
import re


class Wikipedia:
    def __init__(self, day=None):
        # We have to convert all the cyrillic text into unicode characters
        # to generate the correct link.
        self.month = Calendar().get_this_month_in_unicode()
        if not day:
            self.day = Calendar().day
        else:
            self.day = day
        # Address example: https://ru.wikipedia.org/wiki/16_января
        self.address = f"https://ru.wikipedia.org/wiki/{self.day}_{self.month}"
        # Lists to store BeautifulSoup data.
        self.events = []
        self.birthdays = []
        # These dictionaries are manipulated and returned in the end.
        self.birthdays_as_dict = {}
        self.events_as_dict = {}

    # Saves raw data to self.events
    def load_events(self):
        response = requests.get(self.address)
        source = response.text
        snippet = re.findall(wiki_snippet_events, str(source))

        soup = BeautifulSoup(str(snippet), features="html.parser")
        for element in soup.find_all('li'):
            self.events.append(element.text)

    # Saves raw data to self.birthdays
    def load_birthdays(self):
        response = requests.get(self.address)
        source = response.text
        snippet = re.findall(wiki_snippet_birthdays, str(source))

        soup = BeautifulSoup(str(snippet), features="html.parser")
        for element in soup.find_all('li'):
            self.birthdays.append(element.text)

    # The converter.
    # The raw data is processed, sanitized and ordered here.
    @staticmethod
    def raw_data_to_dict(data, temporary):
        # We need random items that we can sort later.
        random.shuffle(data)
        for element in data:
            # Regex to filter out info as 'YYYY - text'
            matched = re.findall(r'^\d{2,4}.*—.*', element)
            # re.findall() returns a list of list of matched strings.
            for hit in matched:
                # Some nested lists can be empty, we do not need them.
                if hit:
                    # Replaces that annoying Unicode character with a space.
                    # This way, we achieve the desired format
                    # year - information.
                    string = hit.replace('\xa0', ' ')
                    try:
                        key, value = string.split(' — ')
                    # In case of events, there can be some characters
                    # that are harder to filter out, so we will pass on
                    # those items of the array that contain them.
                    except ValueError:
                        pass
                    else:
                        temporary[key] = value
        # Temporary dictionary to store selected pairs.
        # It will then we passed over to OrderedDictionary.
        unordered_dictionary = {}
        # We need no more that 10 items.
        if len(temporary) >= 10:
            for _ in range(10):
                # Popped key-value pair.
                next_pair = temporary.popitem()
                unordered_dictionary[next_pair[0]] = next_pair[1]
            ordered_dictionary = OrderedDict(sorted(unordered_dictionary.items()))
        # If less that 10, get all.
        # Although this case will probably never occur.
        else:
            for _ in range(len(temporary)-1):
                next_pair = temporary.popitem()
                unordered_dictionary[next_pair[0]] = next_pair[1]
            ordered_dictionary = OrderedDict(sorted(unordered_dictionary.items()))
        return ordered_dictionary

    # Returns OrderedDict that contains pairs
    # year:birthday
    def get_birthdays(self, li = False):
        self.load_birthdays()
        self.birthdays_as_dict = self.raw_data_to_dict(self.birthdays, self.birthdays_as_dict)
        if not li:
            return self.birthdays_as_dict
        else:
            return self.ordered_dict_to_html_list(self.birthdays_as_dict)

    # Returns OrderedDict that contains pairs
    # year:event
    def get_events(self, li = False):
        self.load_events()
        self.events_as_dict = self.raw_data_to_dict(self.events, self.events_as_dict)
        if not li:
            return self.events_as_dict
        else:
            return self.ordered_dict_to_html_list(self.events_as_dict)

    @staticmethod
    def ordered_dict_to_html_list(od):
        string = ""
        for key, value in od.items():
            string += f"<li>{key} — {value}</li>"
        return string
