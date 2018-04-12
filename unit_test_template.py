import unittest
#from <module to test> import func1,class1,class2...

class test_test(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass

    def test_sample(self):
    	"""doc string"""
        self.assertEqual(1, 1)
		#assertTrue(a, Message)
		#assertFalse(a, Message)
		#assertEqual(a, b, Message)
		#assertNotEqual(a, b, Message)
		#assertIs(a, b, Message)
		#assertIsNot(a, b, Message)
		#assertIsNone(a, Message)
		#assertIsNotNone(a, Message)
		#assertIsInstance(a,b,M)
		#assertIsNotInstance(a, b, Message)
		#assertGreater(a, b, Message)
		#assertLess(a, b, Message)
		#assertGreaterEqual(a, b, Message)
		#assertLessEqual(a, b, Message)
		#assertAlmostEqual(a, b, n, Message)
		#assertNotAlmostEqual(a, b, n, Message)
		#assertItemsEqual(a, b, Message)

if __name__ == '__main__':
	unittest.main()
		