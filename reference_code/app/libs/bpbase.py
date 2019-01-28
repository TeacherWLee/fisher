from flask.helpers import url_for

__author__ = 'bliss'

from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


class ApiBlueprint(object):
    def __init__(self, name):
        self.name = name
        self.deferred = []

    def route(self, rule, **options):
        def wrapper(f):
            self.deferred.append((f, rule, options))
            return f
        return wrapper

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            # url_prefix = '/' + self.name
            url_prefix = '/' + self.name

        for f, rule, options in self.deferred:
            endpoint = self.name+'+'+options.pop("endpoint", f.__name__)
            # endpoint = options.pop("endpoint", f.__name__)
            # print(url_for(endpoint))
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)