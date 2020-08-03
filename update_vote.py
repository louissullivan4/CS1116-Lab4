#!/usr/local/bin/python3

from cgi import FieldStorage
from html import escape
import pymysql as db
from os import environ
from http.cookies import SimpleCookie

result = ''
cookie = SimpleCookie()
http_cookie_header = environ.get('HTTP_COOKIE')
if not http_cookie_header:
    cookie['id'] = 1
else:
    cookie.load(http_cookie_header)
    if 'id' not in cookie:
        cookie['id'] = 1
    else:
        result = "<p>Sorry, you have already voted!</p>"
cookie['id']['expires'] = 157680000
print(cookie)
print('Content-Type: text/html')
print()

form_data = FieldStorage()
candidate = ''
if result == '':
    if len(form_data) != 0:
        try:
            candidate = escape(form_data.getfirst('candidate_name', '')).strip()
            connection = db.connect('cs1.ucc.ie', 'ls9', 'raeti', 'cs6503_cs1106_ls9')
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""SELECT * FROM candidates
                                        WHERE candidate_name = %s""", candidate)
            if cursor.rowcount == 0:
                result = '<p>Error! This candidate does not exist.</p>'
            else:
                cursor.execute("""UPDATE candidates 
                                    SET total_votes = total_votes + 1 
                                    WHERE candidate_name = %s""", candidate)
                connection.commit()
                result = '<p>Successfully submitted your vote!</p>'
            cursor.close()
            connection.close()
        except db.Error:
            result = '<p>Error! We are experiencing problems at the moment. Please call back later.</p>'

print("""
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Place your vote</title>
            </head>
            <body>
                %s
            </body>
            </html>""" % result)


