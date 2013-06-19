from bottle import route, run

@route('/')
def hello():
    with open('Slideshow.html') as f:
        return f.read()

run(host='localhost', port=8130, debug=True)
