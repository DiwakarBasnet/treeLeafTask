def find_related_nodes(graph, start_node, relationship_type):
    """
    Find nodes related to the node through a specific relationship
    :param graph: Networkx Digraph
    :param start_node: String extracted from sentence which is present as node in digraph
    :param relationship_type: String type of relationship extending start_node
    :return related_nodes: List of nodes that relate to start_node through relationship_type
    """
    related_nodes = []
    for successor in graph.successors(start_node):
        for edge_data in graph.get_edge_data(start_node, successor).values():
            if edge_data == relationship_type:
                related_nodes.append(successor)
    return related_nodes
