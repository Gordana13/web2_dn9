from google.appengine.api import mail

from handlers.base import BaseHandler


class EmailNewCommentWorker(BaseHandler):
    def post(self):
        topic_author_email = self.request.get("topic_author_email")
        topic_title = self.request.get("topic_title")
        topic_id = self.request.get("topic_id")

        mail.send_mail(
            sender="rok.povsic@gmail.com",
            to=topic_author_email,
            subject="Your topic received a new comment",
            body="""Topic with title %s has a new comment.

        <a href='/topic/show/%s'>Link to the topic</a>"""
                 % (topic_title, topic_id)
        )
