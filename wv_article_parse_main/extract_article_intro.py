def extract_article_intro(...):
    """
    Extract all content in an article that comes before the first H2 section
    Writes non-JSON elements to file called '{arid}-intro.txt'
    
    Parameters
    ----------
    ...: ...
        ...
        
    Return
    ------
    ...: ...
        ...
    
    """

    
    return 
    


"""
   
    # open raid file in the directory; contains entire article
    f = open({raid_path/raid_name})  #update
    data = json.load(f)
    article_intro_regex = r"\{'([\S\s]*?)=="
    article_intro_section_raw = re.findall(article_intro_regex, str(data))
    article_intro_section_raw=json.dumps(article_intro_section_raw)
    
    # Write non-JSON metadata elements to file called '{raid}-intro'
    intro_text_regex = r"..."
    intro_text_raw = re.findall(intro_text_regex, article_intro_section_raw)
    intro_file = str(raid_name.split('.')[0]) + 'intro.txt'
    #write intro_file into raid_path
    
    # Extract article metadata elements and create a dictionary entry
    raid_metadata = {}
    article_header['article_id'] =  data['id']
    article_header['article_title'] = data['title']
    article_header['revision_id'] = data['revision']['id']
    article_header['revision_timestamp'] = data['revision']['timestamp']
    article_header['revision_article_parentid'] = data['revision']['parentid']
    #article_header['revison_size'] = data['text']['@bytes']

"""