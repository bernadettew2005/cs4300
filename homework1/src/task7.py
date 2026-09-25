# Task 7: Package Management

import requests

# send a request to the url and return the response status code
def get_website_status(url):
    response = requests.get(url) # send GET request to url, save response
    return response.status_code

def main():
    url = "https://example.com"
    status = get_website_status(url)

    print(f"Status Code: {status}")

if __name__ == "__main__":
    main()