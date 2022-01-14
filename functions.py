import json


def main_load():
    """Возвращает посты, комментарии и закладки"""
    with open('data/posts.json', encoding='utf8') as f:
        posts = json.load(f)
    with open('data/comments.json', encoding='utf8') as f:
        comments = json.load(f)
    with open('data/bookmarks.json', encoding='utf8') as f:
        bookmarks = json.load(f)
    return posts, comments, bookmarks


def posts_and_comments(posts, comments):
    """Вывод поста и соответствующих комментариев"""

    for p, post in enumerate(posts):
        pk = post.get('pk')
        users_comments = []
        for comment in comments:
            if comment.get('post_id') == pk:
                users_comments.append(comment)
        posts[p]['count_comment'] = len(users_comments)
    return posts, comments


def post_and_comment(post_id, posts, comments):
    """Вывод поста и соответствующих комментариев"""

    users_comments = []
    for post in posts:
        pk = post.get('pk')
        if post_id == pk:
            for comment in comments:
                if comment.get('post_id') == post_id:
                    users_comments.append(comment)
            return post, users_comments
    return None, users_comments



def find_post(word):
    """Поиск поста по вхождению ключевого слова в тексте поста"""
    post_list = []
    with open('data/posts.json', encoding='utf8') as f:
        posts = json.load(f)
    if word:
        for post in posts:
            if word in post['content']:
                post_list.append(post)
                #post_count = len(post_list)
    return post_list[:10]


def find_username(username):
    """Вывод постов конкретного пользователя"""
    user_posts_list = []
    with open('data/posts.json', encoding='utf8') as f:
        posts = json.load(f)
    for post in posts:
        if username in post['poster_name']:
            user_posts_list.append(post)
    return user_posts_list

