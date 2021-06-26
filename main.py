"""
    Vaaranan Yogalingam
    2021-06-26
    Basic Python Web Scraper
"""
import urllib.request

def main():
    webUrl = urllib.request.urlopen("http://google.com")
    html_code = webUrl.read()
    print(html_code)

if __name__ == "__main__":
    main()
