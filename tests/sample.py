from  src.suttu import Suttu, request

from werkzeug.serving import run_simple

app = Suttu()

@app.route("/hello", methods=["GET"])
def users():
    print(request)
    return request.data

if __name__ == "__main__":
    run_simple("localhost", 8000, app)
