from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    u1 = User(first_name="u1", last_name="u1")
    u2 = User(first_name="u2", last_name="u2")
    u3 = User(first_name="u3", last_name="u3")
    u1.save()
    u2.save()
    u3.save()
    
    b1 = Blog(title="blog1", author=u1)
    b2 = Blog(title="blog2", author=u1)
    b1.save()
    b2.save()
    
    b1.subscribers.add(u1, u2)
    b2.subscribers.add(u2)
    
    t1 = Topic(title="topic1", blog=b1, author=u1)
    t2 = Topic(title="topic2_content", blog=b1, author=u3, created="2017-01-01")
    t1.save()
    t2.save()
    
    t1.likes.add(u1, u2, u3)


def edit_all():
    pass


def edit_u1_u2():
    pass


def delete_u1():
    pass


def unsubscribe_u2_from_blogs():
    pass


def get_topic_created_grated():
    return Topic.objects.filter(created__gt='2018-01-01')


def get_topic_title_ended():
    return Topic.objects.filter(title__endswith="content")


def get_user_with_limit():
    return User.objects.filter().order_by('-id')[:2]


def get_topic_count():
    return Topic.objects.annotate(topic_count=Count("blog"))


def get_avg_topic_count():
    # not sure?
    return Topic.objects.annotate(Avg("blog"))


def get_blog_that_have_more_than_one_topic():
    return Blog.objects.annotate(topic_count=Count("topic")).filter(topic_count__gt=0)


def get_topic_by_u1():
    return Topic.objects.filter(author__first_name="u1")


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass
