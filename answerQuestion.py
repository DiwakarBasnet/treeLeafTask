from traverseGraph import find_related_nodes


def answer_question(graph, question):
    """
    Answer the question
    :param graph: Networkx Digraph
    :param question: String of user asked question that contains subject and relationship
    :return find_related_nodes: Function call for finding nodes related to subject through relationship
    """
    tokens = question.lower().split()

    # Initialize variables to store relevant information
    query_subject = None
    query_relationship = None

    # Identify the subject and relationship from the question
    for token in tokens:
        if token in graph.nodes:
            query_subject = token
        elif token in [data[2]['relation'] for data in graph.edges.data()]:
            query_relationship = token

    # If subject and relationship are identified, find related nodes
    if query_subject and query_relationship:
        return find_related_nodes(graph, query_subject, query_relationship)
    else:
        # return query_subject, query_relationship
        return "Sorry, I couldn't identify the relevant information in the question."
