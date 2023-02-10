import requests

def main():
    api1_url = "http://localhost:8080/"
    api2_url = "http://localhost:8080/api"

    # Make a GET request to API 1
    response = requests.get(api1_url)
    # Print the response from API 1
    print("Response from API 1:")
    print(response.text)

    # Make a GET request to API 2
    response = requests.get(api2_url)
    # Print the response from API 2
    print("Response from API 2:")
    print(response.text)

if __name__ == "__main__":
    main()