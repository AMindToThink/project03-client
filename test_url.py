import requests
def test_url(baseurl, userid):
    """Test if the URL is accessible for POST requests"""
    try:
        url = baseurl + f"/pdf/{userid}"
        
        # Simple test data
        test_data = {"filename": "myfile.pdf", "data":"MQ0KMg0KMw0KNA0KNQ0KNg0KNw0KOA0KOQ0KMTANCjExCjEyCjEzCjE0CjE1CjE2CjE3CjE4CjE5CjIwCjIxCjIyCjIzCg=="}
        
        import json
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Send a simple POST request
        response = requests.post(url=url, data=json.dumps(test_data), headers=headers)
        
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        
        return response.status_code < 500  # Consider it working if not a server error
    except Exception as e:
        print(f"Error testing URL: {e}")
        return False