#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from flask import Flask


app = Flask(__name__)
app.config.from_object('config')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5983, debug=app.config['DEBUG'])


'''
@app.route('/hello')
def hello():
    return 'Hello world.'

    return '<html></html>'

    headers = {
        'content-type': 'text/plain',
        'location': 'https://www.bing.com'
    }
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response

    return '<html></html>', 301, headers
'''
