__author__ = 'luanvu'
import logging
import sys
from models import Topic, TopicGuestView, TopicView, TopicThanks
log=logging.getLogger(__name__)

class TopicDetail:
	def __init__(self, user, topic):
		self.topic=topic
		self.seen_count=0
        	self.thanks_count=0
       		self.seen=False
            	self.thanks=False
		self.writter=topic.user
		self.set_topic_guest_view_count()
		self.set_topic_view_count()
        	self.set_topic_thanks_count()

		if not user:
			self.seen=False
            		self.thanks=False
		else:
			try:
				topic_view=TopicView.objects.filter(topic=topic, user=user)
				if topic_view:
					self.seen=True
                		if TopicThanks.objects.filter(topic=topic, user=user):
                    			self.thanks=True
			except:
				log.debug("Unexpected error:", sys.exc_info()[0])
	def set_topic_view_count(self):
		try:
			count=TopicView.objects.filter(topic=self.topic).count()
			self.seen_count+=count
		except:
			log.debug("Unexpected error:", sys.exc_info()[0])
	def set_topic_guest_view_count(self):
		try:
			count=TopicGuestView.objects.filter(topic=self.topic).count()
			self.seen_count+=count
		except:
			log.debug("Unexpected error:", sys.exc_info()[0])
    	def set_topic_thanks_count(self):
            try:
                count=TopicThanks.objects.filter(topic=self.topic).count()
            except:
                log.debug("Unexpected error:", sys.exc_info()[0])
