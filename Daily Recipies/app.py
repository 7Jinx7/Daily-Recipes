from flask import Flask, render_template
import requests

app = Flask(__name__)

def fetch_reddit_posts():
    # URL subreddit API endpoint 
    url = "https://www.reddit.com/r/recipes/top.json?t=day&limit=1"  # Fetch top 1 post every day

    # Browser request
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Request to Reddit API
    response = requests.get(url, headers=headers)

    # Request confirmation
    if response.status_code == 200:
        data = response.json() 
        posts = []

        # Loop through the posts and extract title and URL
        for post in data['data']['children']:
            title = post['data']['title']
            link = f"https://www.reddit.com{post['data']['permalink']}"
            posts.append({'title': title, 'link': link})

        return posts
    else:
        return None

@app.route("/")
def index():
    # Fetch the post from Reddit
    posts = fetch_reddit_posts()

    # Check if post fetched successfully
    if posts:
        return render_template("index.html", posts=posts)
    else:
        return render_template("index.html", posts=None)

if __name__ == "__main__":
    app.run(debug=True)




