

def transformCommunities(clusters):
    texts = []
    mainCluster = clusters[0]
    for tweet in mainCluster:
        usertexts = tweet.values()
        for usertext in usertexts:
            texts.extend(usertext)

    mainText = "".join(c for c in texts)

    newCluster = {}

    for tweet in mainCluster:
        for user, tweets in tweet.items():
            newCluster[user] = tweets

    return (newCluster, mainText)


    


