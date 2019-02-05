#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from flask import Flask
from bp import bp

app = Flask(__name__)
app.register_blueprint(bp)


@bp.route('/unit_learn')
def test():
    return 'unit_learn'


@app.route('/test2')
def test2():
    return 'test2'

# @test_blue_print.route('/gg')
# def test_blue_print():
#     return 'test_blue_print'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5983, debug=False)

