from flask import Flask , request, render_template_string
import threading
import time


app = Flask(__name__)

counter = 0
entries = []

use_lock = False

state_lock = threading.Lock()


INDEX_HTML = """

<!doctype html>
 <html>
    <head><meta charset="utf-8"><title>Concorrencia + XSS (demo)</title></head>
    <body>
    <h1>Concorrencia + XSS (APENAS LOCAL)</h1>

    <h2>Formulario (stored entry)</h2>
    <form action="/submit" method="post">
    <input name="q" size="60" placeholder="Cole o payload aqui" />
    <button type="submit">Enviar</button>
    </form>

    <h2>Contador (increment)</h2>
    <form action="/increment" method="post">
    <button type="submit">Incrementar 1</button>
    </form>
    <p>Valor do contador: <strong>{{ counter }}</strong></p>

    <hr/>
    <h3>Entries (mostrar sem escapar) --- stored XSS demo</h3>
    <ul>
    {% for e in entries %}
    <li>{{ e|safe }}</li>
    {% endfor %}
    </ul>

    <hr/>
    <p><small>use_lock = {{ use_lock }}</small></p>
    </body>
</html>
 """

@app.route("/",methods=["GET"])
def index():
    #mostrar estado atual
    return render_template_string(INDEX_HTML,
                                 counter=counter,
                                 entries=entries,
                                 use_lock=use_lock)


@app.route("/submit",methods=["POST"])
def submit():
    global entries
    g = request.form.get("q","")

    if use_lock:
        with state_lock:
            entries.append(q)
    
    else:
        entries.append(q)
    
    return ("",302,{"Location": "/"})

@app.route("/increment",methods=["POST"])
    def increment():
        global counter

        if use_lock:
            with_sate_lock:
                tmp = counter
                time.sleep(0.001)

                tmp += 1
                counter =tmp

        else:
            tmp = counter
            time.sleep(0.001)
            tmp += 1
            counter = tmp
        return ("",302 {"Location": "/"})
@app.route("/reset",methods=["POST"])
    def reset():
        global counter,entries

        if use_lock:
            with state_lock:
                counter = 0
                entries = []

        else:
            counter = 0
            entries = []

        return("",302,{"Location": "/"})

@app.route("toogle_lock",methods = ["POST"])

def toogle_lock():
    global use_lock
    use_lock = not use_lock
    return ("",302,{"Location": "/"})


if __name__ == "__main__":
    app.run(host="127.0.0.1" , port=5000,debug=False, threaded=True)