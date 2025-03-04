import unittest
from app.models import Sources,Articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('CNN','CNN News','Cable News Newtork that is a leader in providing news worldwide','cnn.com','general','U.S.A','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'CNN')
        self.assertEquals(self.new_source.name,'CNN News')
        self.assertEquals(self.new_source.description,'Cable News Newtork that is a leader in providing news worldwide')
        self.assertEquals(self.new_source.url,'cnn.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'U.S.A')
        self.assertEquals(self.new_source.language,'en')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('CNN','ombima','The tech scene in Africa','A look at various tech hubs in Africa ','techie.com','techie.com/7643t94.jpg','201-09-11T07:57:16Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'ombima')
        self.assertEquals(self.new_article.title,'The tech scene in Africa')
        self.assertEquals(self.new_article.description,'A look at various tech hubs in Africa')
        self.assertEquals(self.new_article.url,'techie.com')
        self.assertEquals(self.new_article.image,'techie.com/7643t94.jpg')
        self.assertEquals(self.new_article.date,'2019-09-11T07:57:16Z')