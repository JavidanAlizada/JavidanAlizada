"""Refresh the Writing section of README.md from the Medium RSS feed."""
import re
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

FEED = "https://medium.com/feed/@javidanalizada99"
START, END = "<!-- ARTICLES:START -->", "<!-- ARTICLES:END -->"

req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0"})
root = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())

rows = ["| Article | Published |", "|---|---|"]
for item in root.iter("item"):
    title = item.findtext("title").replace("|", "\\|")
    link = item.findtext("link").split("?")[0]
    date = parsedate_to_datetime(item.findtext("pubDate")).strftime("%b %d, %Y")
    rows.append(f"| [{title}]({link}) | {date} |")

if len(rows) == 2:
    raise SystemExit("Feed returned no articles; leaving README unchanged")

with open("README.md", encoding="utf-8") as f:
    readme = f.read()
block = f"{START}\n" + "\n".join(rows) + f"\n{END}"
readme = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: block, readme, flags=re.S)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
