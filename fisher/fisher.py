#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from app import create_app

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


app = create_app()


if __name__ == '__main__':
    # print('url_map:')
    # print(app.url_map)
    # print('view_functions:')
    # print(app.view_functions)
    app.run(host='0.0.0.0', port=5983, debug=app.config['DEBUG'], threaded=True)


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
