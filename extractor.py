import spacy
import textacy
import pandas as pd


def extract_sub_rel_obj(txt):
    """
    Extracts subject, object and relation from text
    :param txt: String containing paragraph from article
    :return df: Pandas dataframe containing id, text, subject, relation and object
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(txt)

    # List of sentences in text
    lst_docs = [sent for sent in doc.sents]

    dic = {"id": [], "text": [], "subject": [], "relation": [], "object_": []}

    for n, sentence in enumerate(lst_docs):
        lst_generators = list(textacy.extract.subject_verb_object_triples(sentence))
        for sent in lst_generators:
            subj = " ".join(map(str, sent.subject))
            obj = " ".join(map(str, sent.object))
            relation = " ".join(map(str, sent.verb))
            dic["id"].append(n)
            dic["text"].append(sentence.text)
            dic["subject"].append(subj.lower())
            dic["object_"].append(obj.lower())
            dic["relation"].append(relation.lower())

    # Create Dataframe of dictionary
    df = pd.DataFrame(dic)
    return df
