import requests
import PostModel as pm
url = "https://jsonplaceholder.typicode.com/posts"
user_id = []
response = requests.get("https://jsonplaceholder.typicode.com/posts")#method of an requests package to get url
if response.status_code==200 or response.status_code==201:
    data = response.json()#method of an requests package to take data
    #print(data)
    posts = pm.PostModel(**data)
    print(posts)
    for i in range(len(data)):
        user_id.append(data[i]['userId'])
    print(user_id)
else:
    print("Error")