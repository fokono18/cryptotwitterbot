
import json


from getCoversationTweets import coversationThread
from getMajortweetIds import fetchProminentTweets
from  measureInfluence import measureInfluence
from stance import analyze_user_stance, debate_analysis, triggers
from transformFemi import transformCommunities
from conversation_graph import build_conversation_graph
from debateDetection import detect_debate_communities


def main():
    # Step 1: Data Collection
    with open("second.json", "r") as datafile:
        tweets = json.load(datafile)

    
    tweets = coversationThread(fetchProminentTweets())
    print("done fetching tweets")
    # Step 2: Build Conversation Graph
    G = build_conversation_graph(tweets)
   
    
    # Step 3: Detect Debate Clusters
   
    debate_communities = detect_debate_communities(G)
    # print(debate_communities)
    # for i, community in enumerate(debate_communities, start=1):
    #     print(f"Debate Cluster {i}: {community}")


    newCluster, mainText = transformCommunities(debate_communities)
    print(mainText)
    print(newCluster)


    influences = measureInfluence(G, newCluster)
    print(influences)
    print("done with measuring influence")

  
   

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
