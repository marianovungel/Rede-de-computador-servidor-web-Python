import os

try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from socketServer import TCPServer as Server
except ImportError:
    from http.server import HTTPServer as Server
    from http.server import SimpleHTTPRequestHandler as Handler

PORT = int(os.getenv('PORT', 8080))

os.chdir('static')

httpd = Server(("", PORT), Handler)

try:
    print("Servidor na porta: %i" %PORT)
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()