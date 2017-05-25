from google.appengine.ext import ndb
from google.appengine.api import mail
from google.appengine.api import taskqueue


class Comment(ndb.Model):
    content = ndb.TextProperty()
    author_email = ndb.StringProperty()
    topic_id = ndb.IntegerProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)

    @staticmethod
    def create(text, user, topic):
        new_comment = Comment(
            content=text,
            author_email=user.email(),
            topic_id=int(topic.key.id()),
        )
        new_comment.put()

        taskqueue.add(
            url="/task/email-new-comment",
            params={
                "topic_author_email": topic.author_email,
                "topic_title": topic.title,
                "topic_id": topic.key.id()
            }
        )


        return new_comment
