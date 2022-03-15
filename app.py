#!/usr/bin/env python
"""A simple Python Flask-based Job Callback server.
Just prints the content of messages sent to the /job-callback endpoint.
"""
from datetime import datetime
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
    The payload is expected contain a JSON structure, which we print
    before returning 200. If there's no payload we return 400.
    """
    payload = request.get_json(force=True)
    if not payload:
        abort(400)

    timestamp = datetime.utcnow().replace(microsecond=0)
    print(f'\n--> {request.method} /{request.endpoint} [{timestamp} (UTC)]')
    _PP.pprint(payload)

    return '', 200
