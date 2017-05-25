import datetime

from handlers.base import BaseHandler
from models.topic import Topic


class DeleteTopicsCron(BaseHandler):
    def get(self):
        dt_delete_to = datetime.datetime.now() \
                       - datetime.timedelta(days=30)

        deleted_topics = Topic.query(
            Topic.deleted == True, Topic.created <= dt_delete_to
        ).fetch()

        for topic in deleted_topics:
            topic.key.delete()
