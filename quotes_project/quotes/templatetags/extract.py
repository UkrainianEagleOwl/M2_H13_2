from django import template


from ..models import Author
from ..utils import get_mongo_db

register = template.Library()


def get_author_fullname(author):
    try:
        author = Author.objects.get(pk=author.pk)
        if author:
            return author.fullname
        else:
            return ""
    except Author.DoesNotExist:
        return "Anonymous"


def get_author_id(author):
    try:
        author = Author.objects.get(pk=author.pk)
        if author:
            return author.pk
        else:
            return ""
    except Author.DoesNotExist:
        return "Anonymous"


register.filter("author_name", get_author_fullname)
register.filter("author_id", get_author_id)
