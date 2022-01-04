import requests

def culltyShorten(url):

    api_key = 'CREAT AN API KEY IN CULLTY WEBSITE AND PUT IT HERE'

    # preferred name in the URL
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
    # or
    # api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name=some_unique_name"
    # make the request
    response = requests.get(api_url)
    if response.status_code != 200:
        return "Server Failed"
    data = response.json()["url"]
    if data["status"] == 7:
        # OK, get shortened URL
        shortened_url = data["shortLink"]
        #print("Shortened URL:", shortened_url)
        return shortened_url
    else:
        #print("[!] Error Shortening URL:", data)
        return "Error"