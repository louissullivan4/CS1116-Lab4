#!/usr/local/bin/python3

from cgitb import enable

enable()

from cgi import FieldStorage
from html import escape
import pymysql as db

print('Content-Type: text/html')
print()

form_data = FieldStorage()
candidate = ''
result = ''
if len(form_data) != 0:
    try:
        candidate = escape(form_data.getfirst('candidate', '')).strip()
        connection = db.connect('cs1.ucc.ie', 'ls9', 'raeti', 'cs6503_cs1106_ls9')
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""SELECT * FROM candidates
                            WHERE candidate_name = %s""", candidate)
        if candidate != '':
            if cursor.rowcount == 0:
                cursor.execute("""INSERT INTO candidates
                                VALUES (%s, 0)""", candidate)
                connection.commit()
                result = '<p>Successfully inserted!</p>'
            else:
                result = '<p>Error! This candidate has already been entered.</p>'
            cursor.close()
            connection.close()
    except db.Error:
        result = '<p>Error! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Update Candidates</title>
            <link rel="stylesheet" href="styles.css"
        </head>
        <body>
            <form action="insert_candidate.py" method="post">
                <label for="candidate">Candidates: </label>
                <input type="text" name="candidate" value="%s" size="50" maxlength="50" id="candidate" />
                <input type="submit" value="Update" />
            </form>
            %s
        </body>
    </html>""" % (candidate, result))
