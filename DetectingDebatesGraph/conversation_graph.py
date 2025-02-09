
import networkx as nx


def add_text_to_node(graph, user_id, text):
    """
    Append the given text to the 'texts' list for a node.
    Only append if the text is not already present.
    """
    if user_id in graph.nodes:
        if "texts" in graph.nodes[user_id]:
            if text not in graph.nodes[user_id]["texts"]:
                graph.nodes[user_id]["texts"].append(text)
        else:
            graph.nodes[user_id]["texts"] = [text]
    else:
        # If node doesn't exist, add it with the text list.
        graph.add_node(user_id, texts=[text])

def populate_graph_from_tweet(tweet, graph):
    """
    Given a tweet (as a dict) and a NetworkX DiGraph, this function adds nodes and edges
    based on the tweet's structure. It adds:
      - A node for the tweeting user (with tweet text appended).
      - A "reply" edge if the tweet is a reply.
      - A "quote" edge if the tweet is a quote tweet, and adds the quoted tweet text.
    """
    # Extract the tweeting user's info
    user_info = tweet.get("user", {})
    tweeting_user_id = user_info.get("id")
    tweeting_username = user_info.get("username")

 
    tweet_text = tweet.get("text", "")
    
    if tweeting_user_id is None:
        # Without a tweeting user id, we cannot proceed.
        return

    # Add or update the tweeting user's node
    if tweeting_user_id not in graph:
        graph.add_node(tweeting_user_id,
                       username=tweeting_username,

                       texts=[tweet_text])
    else:
        add_text_to_node(graph, tweeting_user_id, tweet_text)
    
    # --- Process a Reply ---
    reply_user_id = tweet.get("in_reply_to_user_id")
    if reply_user_id:
        if reply_user_id not in graph:
            graph.add_node(reply_user_id, username="", texts=[])
        graph.add_edge(tweeting_user_id, reply_user_id, type="reply")
    
    # --- Process a Quote Tweet ---
    if tweet.get("is_quote_tweet") and tweet.get("quote"):
        quoted_tweet = tweet["quote"]
        quoted_user = quoted_tweet.get("user", {})
        quoted_user_id = quoted_user.get("id")
        quoted_username = quoted_user.get("username")
        quoted_name = quoted_user.get("name")
        quoted_text = quoted_tweet.get("text", "")
        
        if quoted_user_id:
            if quoted_user_id not in graph:
                graph.add_node(quoted_user_id,
                               username=quoted_username,
                               name=quoted_name,
                               texts=[quoted_text])
            else:
                add_text_to_node(graph, quoted_user_id, quoted_text)
            graph.add_edge(tweeting_user_id, quoted_user_id, type="quote")

def build_conversation_graph(tweet_list):
    """
    Processes a list of tweet dictionaries and returns a populated directed graph.
    """
    G = nx.DiGraph()
    for tweet in tweet_list:
        populate_graph_from_tweet(tweet, G)
    return G
