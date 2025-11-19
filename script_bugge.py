import requests
import pandas as pd

def load_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    response.raise_for_status() 
    
    data = response.json()
    df = pd.DataFrame(data)
    print(df.head())

if __name__ == '__main__':
    load_data()
