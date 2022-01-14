from flask import Flask, render_template, request

from functions import *

posts, comments, bookmarks = main_load()
posts, comments = posts_and_comments(posts, comments)

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_id>')
def id_post(post_id):
    post, comment = post_and_comment(post_id, posts, comments)
    if post:
        return render_template('post.html', post=post, comments=comment)
    return "Не найдено постов", 404


@app.route('/search')
def search_post():
    word = request.args.get('word')
    find_posts = find_post(word)
    return render_template('search.html', posts=find_posts, posts_count=len(find_posts))


@app.route('/users/<username>')
def search_username(username):
    find_posts = find_username(username)
    return render_template('user-feed.html', posts=find_posts)

app.run()