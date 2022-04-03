import requests

api_key = "1aca2f603ca8b4d9d78c01412837f3fe7e582"
url = "https://DemoNovaland.herokuapp.com/InitializeParticipant/"
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)