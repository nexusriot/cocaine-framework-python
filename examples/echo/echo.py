#!/usr/bin/env python
import msgpack
from cocaine.decorators import http

from cocaine.worker import Worker
from cocaine.logging import Logger

__author__ = 'EvgenySafronov <division494@gmail.com>'

log = Logger()


def echo(request, response):
    message = yield request.read()
    log.debug('Message received: \'{0}\'. Sending it back ...'.format(message))
    response.write(msgpack.dumps(message))
    response.close()


@http
def echo2(request, response):
    message = yield request.read()
    log.debug('Message received: \'{0}\'. Sending it back ...'.format(message))
    response.write_head(200, [('Content-type', 'text/plain')])
    response.write('Ok')
    # response.write(msgpack.dumps(message))
    response.close()

W = Worker()
W.run({'doIt': echo, 'doIt2': echo2})
