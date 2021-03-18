import uuid

from flask import g, request, has_request_context


class RequestId(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("REQUEST_ID_HEADER_NAME", "X-REQUEST-ID")

        @app.before_request
        def before_request():
            if has_request_context() and not hasattr(g, "request_id"):
                request_id = request.headers.get(app.config["REQUEST_ID_HEADER_NAME"])
                if request_id is None:
                    g.request_id = uuid.uuid4().hex
                else:
                    g.request_id = request_id

    @property
    def current_id(self):
        if has_request_context() and hasattr(g, "request_id"):
            return g.request_id
        return None
