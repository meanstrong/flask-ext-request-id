import logging

import flask


class LogFilter(logging.Filter):
    def filter(self, record):
        if flask.has_request_context():
            if hasattr(flask.g, "request_id"):
                record.request_id = flask.g.request_id
            else:
                record.request_id = "RequestIdNotFound"
        else:
            record.request_id = "NotInRequestContext"
        return True
