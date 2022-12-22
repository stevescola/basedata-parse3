def extract_locale_header_data(...):

    """
        Extracts specific tags from each "article" in the dump and creates a dictionary that describes the locale which is topic of the article.  
        See the defined schema.
        
        Parameters
        ----------
        ...
        ...
        
        Returns
        -------
        Single dictionary that includes a series of items that describe each locale
    """

...

return ...

    """
    SCHEMA

    "article_id": " " {								// as int?
        "article_title": " ",
        "locale_type": " ",							// options: ["continent", "region", "city", "district", "park", "airport"]
        "article_rating": " ",						// options: ["outline", "usable", "guide"]; this will change as the article is improved
        "is_part_of": " ",							// currently extract article title of the parent
        "locale_geo": {
            "locale_lat": " ",
            "locale_long": " "
        }
    }
    """
