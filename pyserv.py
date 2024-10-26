from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl


httpd = HTTPServer(('0.0.0.0', 4443), SimpleHTTPRequestHandler)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile='PATH-TO-CERT.pem', keyfile='PATH-TO-KEY.pem')

httpd.socket = ssl_context.wrap_socket (httpd.socket, server_side=True)

httpd.serve_forever()
