import os

class Config:
   	NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey=f1bd917f2a124110a6411ca788f212b8'
   	ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=f1bd917f2a124110a6411ca788f212b8'
   	NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
   	@staticmethod
   	def init_app(app):
   		pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig}
