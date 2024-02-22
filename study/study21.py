import urllib.request

def fetch_webpage(url):
    try:
        with urllib.request.urlopen(url) as response:
            webpage_content = response.read().decode("utf-8")
            print("Webpage Content:")
            print(webpage_content)
    except Exception as e:
        print(f"Failed to fetch webpage content. Error: {e}")

def main():
    url = input("Enter the URL of the webpage: ")
    fetch_webpage(url)

if __name__ == "__main__":
    main()