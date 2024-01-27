from answerQuestion import answer_question


def qa_session(graph):
    """
    Creates a question answer session in terminal
    :param graph: Networkx Digraph
    """
    print("Welcome to the QA session. Type 'exit' to end the session.")
    while True:
        question = input("Ask question: ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break

        print("Answer:", answer_question(graph, question))
