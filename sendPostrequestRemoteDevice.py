import requests
import json

def send_post_request(update_url, version):
    endpoint = "a39rr0bwou5roo-ats.iot.eu-north-1.amazonaws.com"
    api_path = "/api/otaupdate"
    url = f"https://{endpoint}{api_path}"

    payload = {
        "updateUrl": update_url,
        "version": version
    }

    try:
        # Sending POST request
        response = requests.post(url, json=payload)

        # Print debug information
        print(f"Request URL: {url}")
        print(f"Request Payload: {payload}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
update_url = "http.update.com/download"
version = "0.0.4"
send_post_request(update_url, version)
