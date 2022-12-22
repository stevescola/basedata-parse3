def extract_article_h2_sections(...):
    """
    Parse locale article into H2 sections that are written to file with the arid and section name
    Invoke parsing of H3 sections with in the each H2 sections
    Assemble the dictionary entry for each available H2 section and the available nested H3 sections
    
    
    Parameters
    ----------
    ...: ...
        ...
    
    Return
    ------
    ...

    """

    ...
  
    return ...

"""
with open(article, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            article_text = data['revision']['text']['#text']

            # Extract H2 section headers and
            h2_section_header_raw_regex = r"\n==\w+==|\n==\w+\s\w+=="
            h2_section_header_raw_list = re.findall(h2_section_header_raw_regex, str(article_text))
            print(h2_section_header_raw_list)
            h2_avail_dict = dict.fromkeys(h2_section_header_raw_list, '1')
            print(h2_avail_dict)
            
            aid = article.split('.')[0]  
            next_h2_position = 1  #initialze counter that identifies the next h2 header for regex pattern

            # Parse article into separate H2 sections
            for h2 in h2_section_header_raw_list:

                print(next_h2_position)
                print(data)

                # special condition to pick up the last h2 section, all others will be processed by the else statement 
                if next_h2_position == len(h2_section_header_raw_list):
                    print(h2)
                    print(next_h2_position)
                    clean_h2 = h2.replace('=', '')
                    h2_name = aid + "-" + clean_h2.replace(' ', '')
                    f_name = aid + '-' + h2_name + '.json'
                    print(h2_name)
                    print(f_name)
                    h2_section_regex = f"{h2}([\S\s]*?)}}"
                    h2_section = re.findall(h2_section_regex, article_text)
                    print(h2_section)

                    # Write section content to file in a folder/directory with the article id or 'aid'
                    with open(f_name, 'w') as sf:
                        sf.write(f_name)
                    sleep(1)

                else:
                    print(h2)
                    print(next_h2_position)
                    clean_h2 = h2.replace('=', '')
                    h2_name = clean_h2.replace(' ', '')
                    f_name = aid + '-' + h2_name + '.json'
                    print(f_name)
                    end_pattern = h2_section_header_raw_list[next_h2_position]
                    h2_section_regex = f"{h2}([\S\s]*?){end_pattern}"
                    h2_section = re.findall(h2_section_regex, str(article_text))
                    print(h2_section)
                    next_h2_position += 1

                    # Write section content to file in a folder/directory with the article id or 'aid'
                    with open(f_name, 'w') as sf:
                        sf.write(f_name)
                    sleep(1)
"""