from http.server import HTTPServer,BaseHTTPRequestHandler
import json
HOST = "192.168.56.1" 
# IP address to bind the server to (use 'localhost' for local testing)
PORT = 8080
  # Port to listen for incoming HTTP requests
class NeuralHTTP(BaseHTTPRequestHandler):
  # Handle GET requests for HTTP requests
    # how we handle to get requests from the server
    def do_GET(self):
      if self.path == "/": #Root path
          # send a http serever request 
            # Send HTTP status code (200 means "OK")
          self.send_response(200)
          # return the webpage we use this code 
          self.send_header("Contet-type","text/html")
          self.end_headers()
            # Write the response body (HTML content)
          self.wfile.write(bytes("<html><head></head><body><h1>HELLO WORLD</h1></body></html>", "utf-8"))
      elif  self.path == "/status":
        # Send HTTP status code (200 means "OK")
        self.send_response(200)
        # return the webpage we use this code 
        self.send_header("Contet-type","application/json")
        self.end_headers()
        # Write the response body (JSON content)
        self.wfile.write(bytes(json.dumps({"status": "running"}), "utf-8"))
      else:
        # Send HTTP status code (404 means "Not Found")
        self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>", "utf-8"))
    def do_POST(self):
        """Handle POST requests."""
        if self.path == "/data":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode("utf-8"))
                response = {"received": data, "status": "success"}
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(bytes(json.dumps(response), "utf-8"))
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = {"error": "Invalid JSON"}
                self.wfile.write(bytes(json.dumps(response), "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>", "utf-8"))

    def log_message(self, format, *args):
        """Override to customize logging."""
        print(f"{self.client_address[0]} - {format % args}")

server = HTTPServer((HOST, PORT), NeuralHTTP)
print(f"Starting server on {HOST}:{PORT}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
    print("Server closed")