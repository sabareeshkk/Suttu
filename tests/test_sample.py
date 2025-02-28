from werkzeug.serving import run_simple

def application(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return [b"Hello, World!"]

if __name__ == "__main__":
    run_simple("localhost", 8000, application)