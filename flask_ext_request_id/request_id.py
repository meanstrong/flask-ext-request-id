import uuid

import flask


class RequestId(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        @app.before_request
        def before_request():
            if flask.has_request_context() and not hasattr(flask.g, "request_id"):
                flask.g.request_id = uuid.uuid4().hex

    @property
    def current_id(self):
        if flask.has_request_context() and hasattr(flask.g, "request_id"):
            return flask.g.request_id
        return None
