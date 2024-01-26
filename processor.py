import spacy


def process_article_for_paragraph(article_dict, article_num=0):
    """
    Process the article to extract paragraph in text
    :param article_dict: dictionary with list of articles
    :param article_num: integer article number
    :return: String of sentences joined from article
    """
    nlp = spacy.load("en_core_web_sm")

    # Process text for sentences using SpaCy
    sentences = []
    for paragraph in article_dict[f'Article_{article_num}']:
        # SpaCy sentence segmentation
        doc = nlp(paragraph)
        sentences.extend([sent.text for sent in doc.sents])
    # Dropping the dateline
    sentences = sentences[1:]

    # Convert list of sentences into a paragraph
    txt = ''.join(x for x in sentences)

    return txt
