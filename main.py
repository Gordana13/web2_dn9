#!/usr/bin/env python
import webapp2

from handlers.base import MainHandler, CookieAlertHandler
from handlers.topics import TopicAddHandler, TopicShowHandler, TopicDeleteHandler
from handlers.comments import CommentAddHandler, AllUserCommentsHandler, CommentDeleteHandler
from tasks.email_new_comment import EmailNewCommentWorker
from crons.delete_topics import DeleteTopicsCron
from crons.delete_comments import DeleteCommentsCron

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="cookie-alert-page"),
    webapp2.Route('/topic/add', TopicAddHandler),
    webapp2.Route('/topic/show/<topic_id:\d+>', TopicShowHandler, name="topic_show"),
    webapp2.Route('/topic/show/<topic_id:\d+>/comment/add', CommentAddHandler),
    webapp2.Route('/topic/<topic_id:\d+>/delete', TopicDeleteHandler),
    webapp2.Route('/user-comments', AllUserCommentsHandler),
    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker),
    webapp2.Route('/cron/delete-topics', DeleteTopicsCron),
    webapp2.Route('/comment/<comment_id:\d+>/delete', CommentDeleteHandler),
    webapp2.Route('/cron/delete-comments', DeleteCommentsCron),
], debug=True)
