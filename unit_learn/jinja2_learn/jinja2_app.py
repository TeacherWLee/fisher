#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from flask import Flask
from flask import render_template
from flask import flash

app = Flask(__name__)

app.config['SECRET_KEY'] = '!@##$%#$%$^%&^*&($@#$#$%$#%^%&'


@app.route('/')
def root():
    demo_parameter = 'This is a demo string define in jinja2_app.py'
    age = 30
    fruit_list = ['apple', 'orange', 'purple', 'banana', 'pear', 'melon']
    price_dict = {'apple': 5.0, 'orange': 3.0, 'banana': 2.5, 'melon': 7.5}
    flash('This is 1st flash message.')
    flash('This is 2nd flash message.')
    flash('This is an error flash message.', category='error')
    flash('This is a warning flash message.', category='warning')
    return render_template(
        'jinja2_learn.html',
        demo_parameter=demo_parameter,
        age=age,
        fruit_list=fruit_list,
        price_dict=price_dict
    )


if __name__ == '__main__':
    app.run(debug='True')
