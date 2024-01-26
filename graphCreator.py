import networkx as nx
import matplotlib.pyplot as plt


def digraph_creator(df):
    """
    Creates directional graph and saves in folder
    :param df: Pandas dataframe containing id, text, subject, object and relation
    """
    # Creating Digraph
    graph = nx.from_pandas_edgelist(df, source="subject", target="object_",
                                    edge_attr="relation", create_using=nx.DiGraph())

    # Plotting
    plt.figure(figsize=(15, 15))
    pos = nx.spring_layout(graph, k=1)

    nx.draw(graph, pos=pos, with_labels=True, cmap=plt.cm.Dark2, node_size=2000,
            connectionstyle='arc3,rad=0.2', font_size=10)
    nx.draw_networkx_edge_labels(graph, pos=pos, label_pos=0.5,
                                 edge_labels=nx.get_edge_attributes(graph, 'relation'),
                                 font_size=10, font_color='black', alpha=0.6)
    # Preview
    # plt.show()
    # Saving
    plt.savefig('graph_db.png', bbox_inches='tight')
