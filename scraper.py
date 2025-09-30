import requests
from bs4 import BeautifulSoup
from datetime import datetime 
import os
import pandas as pd


def fetch_latest_post(url="https://www.jedha.co/blog"):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Récupérer tous les <p> à l'intérieur des balises <article>
    parsed_titles = [p.get_text(strip=True) for p in soup.select("article p")]

    return parsed_titles



def log_posts(posts):
    # Define the directory
    directory = "./posts"
    
    # Check if the directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Get the current time
    now = datetime.now()
    
    # Create a DataFrame from the posts
    df = pd.DataFrame({"Posts": posts, "Extracted_Date": [now for _ in range(len(posts))]})
    
    # Save the DataFrame to a CSV file in the specified directory
    df.to_csv(f"{directory}/posts-{now.strftime('%Y-%m-%d_%H-%M-%S')}.csv", index=False)
    
    return "Logged latest posts"


if __name__ == "__main__":
    latest_posts = fetch_latest_post()
    log_posts(latest_posts)
    print(f"Logged {len(latest_posts)} Articles.")
