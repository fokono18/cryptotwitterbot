
import json


from getCoversationTweets import coversationThread
from getMajortweetIds import fetchProminentTweets
from  measureInfluence import measureInfluence
from stance import analyze_user_stance, analyze_user_take, debate_analysis, triggers
from transformFemi import transformCommunities
from conversation_graph import build_conversation_graph
from debateDetection import detect_debate_communities


def main():
    # Step 1: Data Collection

    
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
   


    influences, user_map = measureInfluence(G, newCluster)
    # print(influences)
    print("done with measuring influence")

  
   

    topic, summary = debate_analysis(mainText)
    stances = analyze_user_stance(newCluster,topic)
    userTakes = analyze_user_take(newCluster,topic)
    trigger = triggers(mainText)

    # print("Debate Topic:")
    # print(topic)
    # print("\nDebate Summary:")
    # print(summary)
    # print("\nDebate Triggers:")
    # print(trigger)
    # print("\nUser Stances:")
    # for user, stance in stances.items():
    #     print(f"{user}: {stance}")

    # for user, take in userTakes.items():
    #     print(f"{user}: {take}")

    
    userDetail = []
    for user in stances.items():
        new = {}
        new["username"] = user_map[user]
        new["confidence"] = influences[user]
        new["argument"] = userTakes[user]
        new["stance"] = stances[user]
        userDetail.append(new)
        

    response = {
        "title": topic,
        "description": summary,
        "userStances": userDetail
    }

    print(response)

if __name__ == "__main__":
    main()
