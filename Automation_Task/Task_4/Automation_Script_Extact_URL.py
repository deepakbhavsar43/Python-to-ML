import re
import webbrowser

file = 'Data.txt'

with open(file, 'r', encoding='utf-8') as f:
    for ln in f:
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', ln)
        print(urls)
for url in urls:
    webbrowser.open_new_tab(url)