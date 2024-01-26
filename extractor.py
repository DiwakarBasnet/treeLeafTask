import spacy
import textacy
import pandas as pd


def extract_sub_rel_obj(txt):
    """
    Extracts subject, object and relation from text
    :param txt: String containing paragraph from article
    :return: Pandas dataframe containing id, text, subject, relation and object
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(txt)

    # List of sentences in text
    lst_docs = [sent for sent in doc.sents]

    dic = {"id": [], "text": [], "subject": [], "relation": [], "object_": []}

    for n, sentence in enumerate(lst_docs):
        lst_generators = list(textacy.extract.subject_verb_object_triples(sentence))
        for sent in lst_generators:
            subj = "_".join(map(str, sent.subject))
            obj = "_".join(map(str, sent.object))
            relation = "_".join(map(str, sent.verb))
            dic["id"].append(n)
            dic["text"].append(sentence.text)
            dic["subject"].append(subj)
            dic["object_"].append(obj)
            dic["relation"].append(relation)

    # Create Dataframe of dictionary
    df = pd.DataFrame(dic)
    return df
