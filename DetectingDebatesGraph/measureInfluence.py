import math

import requests


def normalized_log(x, max_value):
    """
    Normalize a value x using a logarithmic scale capped at max_value.
    Returns a value between 0 and 1.
    """
    return min(math.log10(x + 1) / math.log10(max_value + 1), 1)

def extractUserNames(G, maincluster):
    nodes = G.nodes(data=True)
    nodes_map = {}
    for node in nodes:
        if node[0] not in maincluster:
            continue
        nodes_map[node[0]] = node[1]["username"]

    return nodes_map


def getUser(name):
    url = "https://apis.datura.ai/twitter"
    payload = {
        "query": f"from:{name}",
        
    }
    headers = {
        "Authorization": "dt_$Mg3CozdQOIt4b7brzS6kWeHT4keBaucB9Np0Cj0MqNs",
        "Content-Type": "application/json"
    }

    
    response = requests.request("POST", url, json=payload, headers=headers)
    data = response.json()
    if not data:
        return 0
    
    return data[0]["user"]






def compute_importance(user):
    """
    Compute an importance score for a user based on:
      - followers_count (max threshold: 10,000; weight: 50)
      - statuses_count (max threshold: 5,000; weight: 20)
      - favourites_count (max threshold: 1,000; weight: 10)
      - listed_count (max threshold: 10; weight: 10)
      - verified status (if verified or is_blue_verified, bonus: weight 10)

    The function returns a score between 0 and 100.
    """
    # Define maximum thresholds for normalization
    max_followers = 10000
    max_statuses = 5000
    max_favourites = 1000
    max_listed = 10

    # Define weights for each metric
    weight_followers = 60
    weight_statuses = 20
    weight_favourites = 10
    weight_listed = 10
    weight_verified = 10

    # Normalize each metric using the provided thresholds.
    norm_followers = normalized_log(user.get('followers_count', 0), max_followers)
    norm_statuses = normalized_log(user.get('statuses_count', 0), max_statuses)
    norm_favourites = normalized_log(user.get('favourites_count', 0), max_favourites)
    
    # For listed_count we use a simple linear normalization (cap at 1)
    norm_listed = min(user.get('listed_count', 0) / max_listed, 1)

    # If the user is verified or blue verified, add a bonus of 1 (which will be multiplied by the weight)
    verified_bonus = 1 if user.get('verified', False) or user.get('is_blue_verified', False) else 0

    # Compute the total weighted score
    score = (
        weight_followers * norm_followers +
        weight_statuses * norm_statuses +
        weight_favourites * norm_favourites +
        weight_listed * norm_listed +
        weight_verified * verified_bonus
    )

    return score


def measureInfluence(G, mainCluster):
    user_map = extractUserNames(G, mainCluster)
    influences = {}

    for id, name in user_map.items():
        if not name:
            influences[id] = "Not able to Calculate"
            continue

        user = getUser(name)
        if user == 0:
            influences[id] = "Not able to Calculate"
            continue
        importance = compute_importance(user)
        influences[id] = importance

    return influences, user_map
        




# # Example usage with the sample data:
# if __name__ == "__main__":
#     sample_user = {
#         "id": "1191162644",
#         "url": "https://x.com/StanciuIonutVal",
#         "name": "Stanciu Vali",
#         "username": "StanciuIonutVal",
#         "created_at": "Sun Feb 17 21:06:04 +0000 2013",
#         "description": "Join #wam. Enjoy $WAM. Nice.",
#         "favourites_count": 128,
#         "followers_count": 2300000,
#         "listed_count": 0,
#         "media_count": 0,
#         "statuses_count": 179,
#         "verified": False,
#         "is_blue_verified": False,
#         "entities": {
#             "description": {
#                 "urls": []
#             }
#         },
#         "can_dm": False,
#         "can_media_tag": True,
#         "location": "Târgoviște, Romania",
#         "pinned_tweet_ids": ["1347803187537993728"]
#     }

#     importance_score = compute_importance(sample_user)
#     print(f"User Importance Score: {importance_score:.2f} / 100")
