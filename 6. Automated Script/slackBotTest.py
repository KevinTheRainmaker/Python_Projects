import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2037120074375-2048826409029-DCYN4SugUnl8Ru0vl1uvFv2p"

post_message(myToken,"#bot","체온측정 확인 필요")
