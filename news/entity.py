__author__ = 'luanvu'
import logging
import sys
from news.models import News, NewsView, NewsGuestView
log=logging.getLogger(__name__)

class NewsDetail:
	def __init__(self, user, news):
		self.news=news
		self.seen_count=0
		self.writter=news.manager.user
		self.set_news_guest_view_count()
		self.set_news_view_count()
		if not user:
			self.seen=False
		else:
			try:
				news_view=NewsView.objects.filter(news=news, user=user)
				if news_view:
					self.seen=True
			except:
				log.debug("Unexpected error:", sys.exc_info()[0])
	def set_news_view_count(self):
		try:
			count=news_view=NewsView.objects.filter(news=self.news).count()
			self.seen_count+=count
		except:
			log.debug("Unexpected error:", sys.exc_info()[0])
	def set_news_guest_view_count(self):
		try:
			count=news_view=NewsGuestView.objects.filter(news=self.news).count()
			self.seen_count+=count
		except:
			log.debug("Unexpected error:", sys.exc_info()[0])
