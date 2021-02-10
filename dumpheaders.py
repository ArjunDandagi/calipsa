from prometheus_client import Counter, start_http_server, Summary
from flask import Flask ,request, render_template
app = Flask(__name__)

c = Counter('num_requests', 'The number of requests.')

@app.route("/")
def index():
    c.inc()
    data = sorted(request.headers)
    heading = ("Header Key","Header Value")
    return render_template("index.html",heading = heading ,data=tuple(data))

if __name__ == "__main__":
    start_http_server(9110)
    app.run(host="0.0.0.0", port=8080)
