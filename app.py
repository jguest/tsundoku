from flask import Flask

app = Flask(__name__)
pagecount = 0


@app.route('/')
def index():
    global pagecount
    pagecount += 1
    return "Page count is %d" % pagecount


if __name__ == '__main__':
    app.run()
