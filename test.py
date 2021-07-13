try:
    from app import app
    from database import geocode_table
    import unittest

except Exception as e:
    print('Some models are missing {}'.format(e))

class FlaskTest(unittest.TestCase):

    # Check for response 200
    def test_index(self):
        """
        GIVEN a flask app for testing
        WHEN the '/' page is request (GET)
        THEN check that the response is valid
        """
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code,200)
        assert b"Moscow Ring Road Distance Finder" in response.data
        assert b"search address" in response.data

    def test_new_item(self):
        """
        GIVEN a geocode_table database
        WHEN a new geocode_table is created
        THEN check the name, longitude, latitude and distance fields are definec correctly
        """
        new_item = geocode_table(name="address_content",
                                    longitude=42.123456,
                                    latitude=0.123456,
                                    distance=123456)
        assert new_item.name == "address_content"
        assert new_item.longitude == 42.123456
        assert new_item.latitude ==  0.123456
        assert new_item.distance == 123456

    def test_index_page_post(self):
        """
        GIVEN a Flask app for testing
        WHEN the '/' page is posted to (POST)
        THEN check that a '200' status code is returned
        """
        tester = app.test_client(self)
        response = tester.post('/',data = dict(search_address = "paris"), follow_redirects=True)
        print("post response code : ",response.status_code)
        self.assertEqual(response.status_code,200)
        assert b"Moscow Ring Road Distance Finder" not in response.data

        
if __name__ == "__main__":
    unittest.main()