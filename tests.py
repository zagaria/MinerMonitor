import unittest
import monitor


class TestParser(unittest.TestCase):
	testData = {}
	testData['ShareData'] = "[14:11:52] Share accepted: 1/2 (50.00%)"

	def test_share_data(self):
		result = monitor.ShareData(self.testData['ShareData'])
		self.assertEqual(result['success'],1)
		self.assertEqual(result['all'],2)
		self.assertEqual(result['percent'],'50.00%')

if __name__ == '__main__':
    unittest.main()
