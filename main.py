from email_engine import Postman
from settings import subscribers
from settings import email_tweaks
import article_engine

if __name__ == '__main__':
    article_object = article_engine.Article()
    article_as_html = article_object.as_html

    for subscriber_email in subscribers:
        postman_object = Postman(subscriber_email, email_tweaks['intro'], article_as_html)
        postman_object.deliver_article()
