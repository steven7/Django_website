from selenium import webdriver

import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox

		
	def tearDown(self):
		self.browser.quit()


	def test_can_start_a_list_and_retrieve_it_later(self):
		#
		browser.get('http://localhost:8000')

		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

	"""docstring for NewVisitorTest"""
	def __init__(self, arg):
		super(NewVisitorTest, self).__init__()
		self.arg = arg
		

if __name__ == '__main__':
	unittest.main( )
 

# assert 'To-Do' in browser.title


# assert 'Django' in browser.title

# browser.quit()