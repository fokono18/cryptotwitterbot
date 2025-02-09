
import json


from stance import analyze_user_stance, debate_analysis, triggers
from transformFemi import transformCommunities
from conversation_graph import build_conversation_graph
from debateDetection import detect_debate_communities


def main():
    # Step 1: Data Collection
    with open("second.json", "r") as datafile:
        tweets = json.load(datafile)

    # Step 2: Build Conversation Graph
    G = build_conversation_graph(tweets)

    
    counter = 1
    # for node, attr in G.nodes(data=True):
    #     print(f"{counter}.  {node}, {attr}")
    #     counter +=  1

    # print("\nEdges in Graph:")
    # for u, v, attr in G.edges(data=True):
    #     print(f"{u} -> {v} with attributes {attr}")
    

    
    # Step 3: Detect Debate Clusters
   
    debate_communities = detect_debate_communities(G)
    # print(debate_communities)
    # for i, community in enumerate(debate_communities, start=1):
    #     print(f"Debate Cluster {i}: {community}")


    newCluster, mainText = transformCommunities(debate_communities)
    print(mainText)
    print(newCluster)
  
   

    topic, summary = debate_analysis(mainText)
    stances = analyze_user_stance(newCluster,topic)
    trigger = triggers(mainText)

    print("Debate Topic:")
    print(topic)
    print("\nDebate Summary:")
    print(summary)
    print("\nDebate Triggers:")
    print(trigger)
    print("\nUser Stances:")
    for user, stance in stances.items():
        print(f"{user}: {stance}")

    

if __name__ == "__main__":
    main()
