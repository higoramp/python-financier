import requests
from urllib.parse import urljoin, urlunsplit
from time import sleep
from requests.adapters import HTTPAdapter

class EasyCouchdb:

	SESSION = '_session'
	ALLDBS = '_all_dbs'
	ALLDOCS = '_all_docs'
	FIND = '_find'
	TIMEOUT = 10

	req_session = None


	def __init__(self, url):
		self.url=url
		self.SESSION_URL= urljoin(self.url, self.SESSION)
		self.ALLDBS_URL = urljoin(self.url, self.ALLDBS)
		print(self.SESSION_URL)


	def login(self, username, password):
		self.req_session=requests.session()
		self.req_session.mount(self.url, HTTPAdapter(max_retries=5))
		return self.req_session.post(self.SESSION_URL,
		 data={'name': username, 'password':password}, timeout=self.TIMEOUT)

	def all_docs(self, dbname):
		return self.req_session.get(urljoin(self.url, '/'.join([dbname,self.ALLDOCS])), timeout=self.TIMEOUT)

	def query(self, dbname, selector):
		sleep(0.5)
		print('executing query: {0}'.format(selector))
		ret=self.req_session.post(urljoin(self.url, '/'.join([dbname, self.FIND])), json=selector, timeout=self.TIMEOUT)
		print('query executed')
		return ret

	def insert(self, dbname, doc):
		sleep(0.5)
		return self.req_session.post(urljoin(self.url, dbname), json=doc, timeout=self.TIMEOUT)

	def save(self, dbname, doc):
		sleep(0.5)
		return self.req_session.put(urljoin(self.url, '/'.join([dbname, doc['_id']])), json=doc)

	def get_doc(self, dbname, id):
		sleep(0.5)
		return self.req_session.get(urljoin(self.url, '/'.join([dbname,id])), timeout=self.TIMEOUT)


