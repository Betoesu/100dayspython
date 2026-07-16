from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:num>')
def real_post(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_posts = response.json()
    post = all_posts[num - 1]
    title = post["title"]
    subtitle = post["subtitle"]
    body = post["body"]

    return render_template("post.html", post_num=num, title=title, subtitle=subtitle, body=body)

if __name__ == "__main__":
    app.run(debug=True)
