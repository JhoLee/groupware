from django.db import connection


def selectTest():
    cursor = connection.cursor()
    query_string = "SELECT * FROM test"
    cursor.execute(query_string)
    rows = cursor.fetchall()
    posts = []
    for row in rows:
        dic = {'id': row[0], 'name': row[1]}
        posts.append(dic)

    return posts
