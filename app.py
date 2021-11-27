from flask import Flask, send_from_directory
from flask import request
import os.path
from suffix import *

cnt = 0

app = Flask(__name__)
@app.route("/")
def input():
    return """
    <title>Suffix automaton generator</title>
    <center><form action="/generate" method="POST">
    <label for="string">String:</label>
    <input type="text" id="string" name="string" value="abc"><br><br>
    <input type="checkbox" id="links" name="links" value="1">Show links<br><br>
    <input type="submit" value="Visualize">
    </form></center>"""

@app.route("/generate", methods=['POST'])
def generate():
    st = request.form.to_dict()['string']
    global cnt
    cnt += 1
    print("Total number of queries: ", cnt)
    if len(st) > 40:
        return "<center>Graph too large. Please only input graphs with 40 nodes or less.</center>"
    print("String: ", request.form.to_dict()['string'])
    gen(st, request.form.get('links')!=None)
    workingdir = os.path.abspath(os.getcwd())
    return send_from_directory(workingdir, 'graph.pdf')
