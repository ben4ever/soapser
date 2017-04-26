import logging
import sys

from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

from soapser.soap import app


logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    stream=sys.stdout)
logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
make_server('localhost', 8000, WsgiApplication(app)).serve_forever()
