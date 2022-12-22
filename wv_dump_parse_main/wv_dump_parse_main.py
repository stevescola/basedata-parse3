def wv_dump_parse_main():    #can it have a null paramter?

"""
Orchestrate the download and decompression of the latest Wiki Voyage dump
Invoked functions will store the parsed XML files for each article in a single bucket/folder
Capture locale header information and article meta data into dictionaries

Parameters
----------
?

Return
------
?

"""

# Initialize variables
dump_url = 'https://dumps.wikimedia.org/enwikivoyage/latest/enwikivoyage-latest-pages-articles.xml.bz2'
dump_bucket = {path of this dump}
article_bucket = 'dump_bucket + '/' + 'raw_articles'

# Retreive and decompress latest Wiki Voyage dump file and save to a bucket with name of dump data
wv_dump_to_xml_json(...)

# Generate article meta data dictionary
extract_article_meta_data(...)

# Generate locale header data dictionary
extract_locale_header_data(...)

# Parse the dump based into individual files and extract locale header data
wv_raw_article_parse_json(...)




