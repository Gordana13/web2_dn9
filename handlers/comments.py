import cgi

from google.appengine.api import users
from google.appengine.api import memcache

from handlers.base import BaseHandler
from models.comment import Comment
from models.topic import Topic


class CommentAddHandler(BaseHandler):
    def post(self, topic_id):
        csrf_token_from_form = self.request.get("csrf_token")

        csrf_memcache_result = memcache.get(csrf_token_from_form)
        if not csrf_memcache_result:
            return self.write("You are an attacker.")

        user = users.get_current_user()
        if not user:
            return self.write("You are not logged in.")

        text = cgi.escape(self.request.get("text"))

        topic = Topic.get_by_id(int(topic_id))
        new_comment = Comment.create(text, user, topic)

        return self.write("Comment created successfully.")


class AllUserCommentsHandler(BaseHandler):
    def get(self):
        comments = Comment.query(Comment.deleted == False).fetch()
        topics = Topic.query().fetch()
        params = {"comments": comments, "topics": topics}

        return self.render_template("user-comments.html", params)


class CommentDeleteHandler(BaseHandler):
    def post(self, comment_id):
        comment = Comment.get_by_id(int(comment_id))
        comment.deleted = True
        comment.put()

        return self.redirect_to("topic_show", topic_id=comment.topic_id)