from networkx.algorithms.community import greedy_modularity_communities

def detect_debate_communities(G):
    # Use greedy modularity to detect communities (each is a frozenset of user IDs)
    raw_communities = list(greedy_modularity_communities(G))
    
    # Prepare the output list: for each community, create a list of dictionaries.
    communities = []
    for community in raw_communities:
        community_list = []
        for user_id in sorted(list(community)):
            # Get the texts stored in the node (default to empty list if not present)
            texts = G.nodes[user_id].get("texts", [])
            # Create a dictionary mapping the user ID to the list of texts
            community_list.append({user_id: texts})
        communities.append(community_list)
    
    return communities

# Example usage:
# Assuming you already have a graph G populated with nodes and each node may have a 'texts' attribute.
# communities = detect_debate_communities(G)
# for community in communities:
#     print(community)
