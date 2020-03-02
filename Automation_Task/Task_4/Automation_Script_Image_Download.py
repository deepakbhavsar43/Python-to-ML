from urllib.request import urlopen

if __name__ == "__main__":
    with open("007.jpg","wb") as f:
        f.write(urlopen("https://www.google.com/favicon.ico").read())