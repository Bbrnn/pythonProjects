import requests

def ota_update(update_url, version):
    endpoint = "https://a39rr0bwou5roo-ats.iot.eu-north-1.amazonaws.com/api/otaupdate"
    payload = {
        "updateUrl": update_url,
        "version": version
    }

    # Logging key steps
    print("Starting OTA update process")
    print(f"Update URL: {update_url}")
    print(f"Version: {version}")

    # Sending OTA update request to the remote device
    response = requests.post(endpoint, json=payload)

    # Check the response from the device
    if response.status_code == 200:
        print("OTA update initiated successfully.")
        print(f"Response: {response.json()}")
    else:
        print(f"Failed to initiate OTA update. Status code: {response.status_code}")
        print(f"Response: {response.text}")

# Example usage
ota_update("http://http.update.com/download", "1")

