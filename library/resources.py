from flask import abort


class Resources(dict):
    def get_context(self, name):
        try:
            return self[name]
        except KeyError:
            abort(404)