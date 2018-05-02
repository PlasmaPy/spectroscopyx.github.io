#!/usr/bin/env python
import requests as re

OUTPUT_DIR = "web/pages/"
BASE_URL = "https://raw.githubusercontent.com/PlasmaPy/SpectroscoPyx/master/"
WEB_BASE_URL = "https://raw.githubusercontent.com/PlasmaPy/spectroscopyx.github.io/src/"
PAGES = [
    {"filename": OUTPUT_DIR + "conduct.md",
     "url": BASE_URL + "CODE_OF_CONDUCT.md",
     "metadata": {
         "title": "Code of conduct",
         "slug": "conduct"}},
    {"filename": OUTPUT_DIR + "contribute.md",
     "url": BASE_URL + "CONTRIBUTING.md",
     "metadata": {
         "title": "Contribute to PlasmaPy",
         "slug": "contribute"}},
    {"filename": OUTPUT_DIR + "license.md",
     "url": WEB_BASE_URL + "LICENSE.md",
     "metadata": {
         "title": "License",
         "slug": "license"}},
    {"filename": OUTPUT_DIR + "vision.md",
     "url": BASE_URL + "vision_statement.md",
     "metadata": {
         "title": "Vision statement",
         "slug": "vision"}},
    ]


for page in PAGES:
    content = ""
    for field, tag in page["metadata"].items():
        content += "{}: {}\n".format(field, tag)

    content += "\n"
    content += re.get(page["url"]).content.decode("utf-8")
    with open(page["filename"], "w+") as f:
        f.write(content)
