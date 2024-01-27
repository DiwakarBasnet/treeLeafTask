from scraping_THT import extract_article_links, extract_article_text
from processor import process_article_for_paragraph
from extractor import extract_sub_rel_obj
from graphCreator import digraph_creator
from qaSession import qa_session

############################################################################
"""
Scraping The Himalayan Times and creating list of articles
"""
online_link = 'https://thehimalayantimes.com/'
article_links = extract_article_links(online_link)

Article = {}
if article_links:
    # Put article texts in a dictionary
    for index, link in enumerate(article_links):
        Article[f'Article_{index}'] = extract_article_text(link)
else:
    print("No article links found.")
# print(Article)

############################################################################
"""
Process article for sentences
"""
paragraph = process_article_for_paragraph(Article, article_num=0)
# print(paragraph)

############################################################################
"""
Extract subject, object and relationship from paragraph
"""
df = extract_sub_rel_obj(paragraph)
# print(df.head())

############################################################################
"""
Create Directional graph
"""
graph = digraph_creator(df)
# print(graph.edges.data())

############################################################################
qa_session(graph)
