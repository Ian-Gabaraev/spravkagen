# Dictionary of people that receive daily messages.

search_settings = {
    'today': False,
    'delta': 1,
    'brief results': True,
}

# subscribers = {
#     "Creator": "y.gabaraev@spuntiknews.com",
#     "Andrei Tadtaev": None,
#     "Alexandra Alborova": None,
#     "Karina Gagloeva": None,
#     "Lana Chibirova": None,
# }


subscribers = [
    'iangabaratti@icloud.com'
]


cyrillic_to_unicode = {
    'а': '%d0%b0', 'б': '%d0%b1', 'в': '%d0%b2', 'г': '%d0%b3',
    'д': '%d0%b4', 'е': '%d0%b5', 'ж': '%d0%b6', 'з': '%d0%b7',
    'и': '%d0%b8', 'й': '%d0%b9', 'к': '%d0%ba', 'л': '%d0%bb',
    'м': '%d0%bc', 'н': '%d0%bd', 'о': '%d0%be', 'п': '%d0%bf',
    'р': '%d1%80', 'с': '%d1%81', 'т': '%d1%82', 'у': '%d1%83',
    'ф': '%d1%84', 'х': '%d1%85', 'ц': '%d1%86', 'ч': '%d1%87',
    'ш': '%d1%88', 'щ': '%d1%89', 'ъ': '%d1%8a', 'ы': '%d1%8b',
    'ь': '%d1%8c', 'э': '%d1%8d', 'ю': '%d1%8e', 'я': '%d1%8f',
    'ё': '%d1%91'
}

months_by_number = {
    1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
    5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
    9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
}

GB_months_by_number = {
    1: 'january', 2: 'february', 3: 'march', 4: 'april',
    5: 'may', 6: 'june', 7: 'july', 8: 'august',
    9: 'september', 10: 'october', 11: 'november', 12: 'december'
}

email_tweaks = {
    "intro": "Hello from Kuver Tech!",
    "subject": "SpravkaGen. Ваша ежедневная справка.",
    "master_email": "spravkagen@kuver.tech",
    "password": "atizurifki",
    "SMTP": "mail.kuver.tech",
    "port": 25,
}

# Regex's to extract raw HTML from Wikipedia page source.
wiki_snippet_events = '<h2>.*id="События">События[\n\W\w]*id="Родились">Родились<\/span>'
wiki_snippet_birthdays = "<h2>.*id=\"Родились\">Родились[\n\W\w]*id=\"Скончались\">Скончались<\/span"
