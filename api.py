from flask import Flask, request, jsonify, send_file, abort
from flask_cors import CORS
import pandas as pd
from context import Visualizer
import matplotlib
from strategies import *
import json
import os
import glob

matplotlib.use('Agg')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

files = glob.glob("inputs/*")
for f in files:
    os.remove(f)
files = glob.glob("outputs/*")
for f in files:
    os.remove(f)

next_session_id = 0

visualizer = Visualizer()

strats = {
    "bar": BarPlotter(),
    "line": LinePlotter(),
    "scatter": ScatterPlotter(),
    "histogram": HistogramPlotter(),
    "correlogram": CorrelogramPlotter(),
    "boxplot": BoxPlotter(),
    "density": DensityPlotter(),
    "violinplot": ViolinPlotter()

}


def get_service_list():
    out = []
    for i, filename in enumerate(os.listdir("services")):
        with open("services/" + filename, "r") as f:
            svc = json.load(f)
            svc["id"] = str(i)
            out.append(svc)
    return out


def get_service(service_id):
    svcs = get_service_list()
    print("input_id", service_id, type(service_id))
    for s in svcs:
        print("svc id", s["id"], type(s["id"]))
        if s["id"] == service_id:
            return s


@app.route("/get-session-id", methods=["GET"])
def get_session_id():
    global next_session_id
    session_id = str(next_session_id)
    next_session_id += 1
    return str(session_id)


@app.route("/services", methods=["GET"])
def services():
    return jsonify(get_service_list())


@app.route('/upload', methods=["POST"])
def upload():
    session_id = request.headers["Session-Id"]
    if session_id == "null":
        return abort(400, "sessionId is null")
    # print([key for key in request.form.keys()])
    csv = request.files["csv"]
    filename = f"inputs/{session_id}.csv"
    csv.save(filename)
    df = pd.read_csv(filename)
    return jsonify(list(df.columns))


@app.route("/get-image/<int:session_id>")
def get_result_plot(session_id):
    return send_file(f"outputs/{session_id}.png")


@app.route("/execute", methods=["POST"])
def execute():
    service_id = request.headers["Service-Id"]
    session_id = request.headers["Session-Id"]
    if session_id == "null":
        return abort(400, "sessionId is null")
    df = pd.read_csv(f"inputs/{session_id}.csv")
    svc = get_service(service_id)
    strategy = eval(svc["strategy"] + "()")
    visualizer.strategy = strategy
    column_dict = json.loads(request.data.decode("UTF-8"))
    visualizer.plot(
        df,
        columns=[column_dict[key] for key in sorted(column_dict.keys())]
    )
    output_filename = f"outputs/{session_id}.png"
    plt.savefig(f"outputs/{session_id}.png")
    plt.clf()
    return send_file(output_filename)


@app.route("/test", methods=["POST"])
def test():
    print(request.files)
    print(request.data)
    print(request.json)
    print(request.values)
    print(request.args)
    print(request.form)
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)
