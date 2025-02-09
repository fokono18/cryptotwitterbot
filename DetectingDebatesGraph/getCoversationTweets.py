import json
import requests




def coversationThread(CONVS):
    url = "https://apis.datura.ai/twitter"
    payload = {
        "query": f"conversation_id:{CONVS[1]}",
        "sort": "Top"
    }

    headers = {
        "Authorization": "dt_$Mg3CozdQOIt4b7brzS6kWeHT4keBaucB9Np0Cj0MqNs",
        "Content-Type": "application/json"
    }

    tot = []
    for i in range(10):

        response = requests.request("POST", url, json=payload, headers=headers)

        data = response.json()
        tot.extend(data)
        print(i)

    return tot


# with open("second.json", "w") as json_file:
#     json.dump(tot, json_file, indent=4)

