"""
Package for the import and decompression of the latest Wiki Voyage dump and parsing/saving of individual locale articles in XML files.

Functions
---------
wv_dump__parse_main.py
wv_dump_to_xml_json.py
extract_article_meta_data.py
extract_locale_header_data.py
wv_raw_article_parse_json.py


"""

import json
import os
from pprint import pprint
import urllib
import wv_dump_main

