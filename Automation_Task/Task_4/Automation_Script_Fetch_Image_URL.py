# Automation script which fetch URL of all images using Beautiful Soup.
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


class ImageUrl:
    def findIngeUrl(self):
        url = "https://www.amazon.in/b/ref=s9_acss_bw_cg_1_2a1_w?node=18529989031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=K79SFEC7NV0Y45S9Q31Q&pf_rd_t=101&pf_rd_p=ed4dd095-8b4e-43cd-9635-57d3aa24e151&pf_rd_i=18529986031"
        html = urlopen(url)
        bs = BeautifulSoup(html, "lxml")
        images = bs.findAll("img", src=re.compile(".*"))
        return images


if __name__ == "__main__":
    obj1 = ImageUrl()
    result = obj1.findIngeUrl()
    for img in result:
        if "src" in img.attrs:
            print(img.attrs["src"])
