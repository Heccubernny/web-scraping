# Narrowing down the space to the article in the page
#(since there are many other irrelevant elements in the page)
article = soup.find(class_="article-wrapper grid row")

# Getting the keywords section 
keyword_section = soup.find(class_="keywords-section")
# Same as: soup.select("div.article-wrapper grid row div.keywords-section")

# Getting a list of all keywords which are inserted into a keywords list in line 7.
keywords_raw = keyword_section.find_all(class_="keyword")
keyword_list = [word.get_text() for word in keywords_raw]