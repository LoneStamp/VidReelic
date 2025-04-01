import requests


url = "https://jsonplaceholder.typicode.com/posts"


response = requests.get(url)


if response.status_code == 200:
    
    data = response.json()
    
    
    print(data[0])  
else:
    print(f"Failed to retrieve data: {response.status_code}")
