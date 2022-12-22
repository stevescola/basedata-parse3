def wv_dump_to_xml_json(...):
    """
    Retrieve 'latest' file from Wiki Voyage dump site and decompress it
    
    Parameters
    ----------
    dump_url: str
       Persistent Wiki Voyage URL for the latest dump file 
       
    dump_bucket: str
       Location where the decompressed will be stored
       
    Returns
    -------
    Complete dump in JSON format with "redirect" articles removed
    """
    
    # Retrieve dump file and save in dump_bucket
    if not os.path.isfile(dump_url.split('/')[-1]):
        urllib.request.urlretrieve(dump_url, dump_url.split('/')[-1])
    
    # Decompress dump file and save decompressed xml file to dump bucket
    from bz2 import BZ2Decompressor
    
    decompressed = ('.').join(url.split('/')[-1].split('.')[:-1])

    if not os.path.isfile(decompressed):
        with open(decompressed, 'wb') as new_file, open(dump_url.split('/')[-1], 'rb') as file:
            decompressor = BZ2Decompressor()
            for data in iter(lambda : file.read(100 *1024), b''):
                ##latest_dump_xml.write(decompressor.decompress(data))  ###can it include the dump timestamp?

                    ## latest_dump_xml = 'enwikivoyage_latest_pages_articles.xml'
                    ## save in dump_bucket

   # Convert the xml dump to an ordered dictionary in JSON
    if not os.path.isfile('wikivoyage_latest_articles_text.json'):
    import sys
    !{sys.executable} -m pip install xmldict
    
    import xmltodict
    
    with open('enwikivoyage-latest-pages-articles.xml', encoding = 'utf8') as fd:
        doc = xmltodict.parse(fd.read())
        
    data = doc['mediawiki']['page']
    print('To process %s records' %len(data))
    del doc

   
    
    
    return ...