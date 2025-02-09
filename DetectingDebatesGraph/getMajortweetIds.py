import json
import requests

import requests

url = "https://apis.datura.ai/twitter"


def fetchProminentTweets():
    payload = {
        "query": "(best OR worst OR future OR (better than) OR (wrong about) OR debate OR (hot take) OR (I disagree)) (crypto OR Bitcoin OR Ethereum OR Ripple OR Litecoin OR Cardano OR Polkadot OR Dogecoin OR blockchain OR defi OR nft OR web3) (bubble OR crash OR bearish OR bullish OR prices OR liquidation OR sell OR buy OR whale OR dividends OR value OR valuation OR (market cap) OR undervalued OR overvalued)",
        "lang": "en",
    
    }
    headers = {
        "Authorization": "dt_$Mg3CozdQOIt4b7brzS6kWeHT4keBaucB9Np0Cj0MqNs",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    data = response.json()
    CONVS = []
    data.sort(key = lambda x: -x["reply_count"])

    if len(data) == 0:
        raise Exception("No meaningful debates found")


    count = 0
    for tweet in data:
        if count > 2:
            break
        CONVS.append(tweet["conversation_id"])
        print(f"--------{tweet["text"]}----------++")
        count += 1
        
    return CONVS


