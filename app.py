from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "This Flask app works! Future primary dev instance will be here."


@app.route("/kevin/<path:path>")
def kevin(path):
    if request.method != "GET":
        return "405 Method Not Allowed", 405
    r = requests.get(f"https://localhost:5001/{path}")
    return Response(
            r.content,
            r.status_code,
            [
                (n, v) 
                for (n, v) 
                in r.raw.headers.items() 
                if n.lower() not in 
                ["Content-Encoding", "Content-Length", "Transfer-Encoding", "Connection"]])


@app.route("/dat/<path:path>")
def dat(path):
    if request.method != "GET":
        return "405 Method Not Allowed", 405
    r = requests.get(f"https://localhost:5002/{path}")
    return Response(
            r.content,
            r.status_code,
            [
                (n, v) 
                for (n, v) 
                in r.raw.headers.items() 
                if n.lower() not in 
                ["Content-Encoding", "Content-Length", "Transfer-Encoding", "Connection"]])


@app.route("/sri/<path:path>")
def sri(path):
    if request.method != "GET":
        return "405 Method Not Allowed", 405
    r = requests.get(f"https://localhost:5003/{path}")
    return Response(
            r.content,
            r.status_code,
            [
                (n, v) 
                for (n, v) 
                in r.raw.headers.items() 
                if n.lower() not in 
                ["Content-Encoding", "Content-Length", "Transfer-Encoding", "Connection"]])


@app.route("/theresa/<path:path>")
def theresa(path):
    if request.method != "GET":
        return "405 Method Not Allowed", 405
    r = requests.get(f"https://localhost:5004/{path}")
    return Response(
            r.content,
            r.status_code,
            [
                (n, v) 
                for (n, v) 
                in r.raw.headers.items() 
                if n.lower() not in 
                ["Content-Encoding", "Content-Length", "Transfer-Encoding", "Connection"]])


@app.route("/amy/<path:path>")
def amy(path):
    if request.method != "GET":
        return "405 Method Not Allowed", 405
    r = requests.get(f"https://localhost:5005/{path}")
    return Response(
            r.content,
            r.status_code,
            [
                (n, v) 
                for (n, v) 
                in r.raw.headers.items() 
                if n.lower() not in 
                ["Content-Encoding", "Content-Length", "Transfer-Encoding", "Connection"]])

if __name__ == "__main__":
    app.run(host="::")
