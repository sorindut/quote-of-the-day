import requests
import json
import re

url = 'https://www.lspace.org/ftp/words/pqf/pqf'
with requests.get(url=url) as r:
    content = r.text

quotes = content.split('\n\n\n')
quotes = [re.sub(r'\s\s+', ' ', re.sub(r'\s+--','\n --', item.replace('\n', ' '))).strip() for item in quotes]

json_str = json.dumps(quotes, indent=4)
with open("tp_quotes.json", "w") as f:
    f.write(json_str)
