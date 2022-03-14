#!/usr/bin/env python
"""A simple Python Flask-based Job Callback server.
Just prints the content of messages sent to the /job-callback endpoint.
"""
import logging
import pprint

from flask import Flask, abort, request

app = Flask(__name__)

_PP = pprint.PrettyPrinter(indent=2)

# Disable distracting logging...
log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True


@app.route('/job-callback', methods=['PUT'])
def job_callback():
    """Handles callback PUT messages.
    The payload is expected to be a JSON payload.
    """
    data = request.get_json(force=True)
    if not data:
        abort(400)

    print(f'--> {request.method} /{request.endpoint}')
    _PP.pprint(data)

    return {}
