import unittest
import io
from app import app


class TestCase(unittest.TestCase):

	def setUp(self):
		self.client = app.test_client()

	def test_upload_photo(self):			
		result = self.client.post('/uploader', content_type='multipart/form-data', follow_redirects=True, data=dict(photo=(io.BytesIO(b'photo'), 'test.jpg')))
		content_headers = result.headers		
		content_type = content_headers.get('Content-Disposition')
		self.assertTrue('test.jpg' in content_type)
		#self.assertTrue(result.status_code == 200)
	
if __name__ == "__main__":
    unittest.main()
