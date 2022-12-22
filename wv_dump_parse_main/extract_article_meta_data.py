def extract_article_meta_data(...):

    """
        Extracts specific tags from each "article" in the dump and creates a dictionary that describes the article.  
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
	"is_part_of": " ",
	"article_revision_id": {						//combination the article_id and wv_revision_id
			"wv_revision_id": " ",
			"revision_timestmap": " "
	},
	"article_parent_id": " ",						// parentid
	"article_text_size": "", 						// as int; ' textbytes="" ''
}

"""