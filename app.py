from flask import Flask, send_from_directory
from flask import request
import os.path
from suffix import *

cnt = 0

app = Flask(__name__)
@app.route("/")
def input():
    return """
    <title>Suffix Automata Visualizer</title>
    <center>
    <h1 style="font-family: Monaco; padding-top: 30px">Suffix Automata Visualizer</h1>
    <h2 style="font-family: Monaco; padding-top: 100px">
    <form action="/generate" method="POST">
    <label for="string">String:</label>
    <input type="text" id="string" name="string" style="font-family: Monaco"><br><br>
    <input type="checkbox" id="links" name="links" value="1" style="width: 20px; height:20px">Show links<br><br>
    <input type="submit" value="Visualize" style="font-family: Monaco; font-size: 20px">
    </form></h2>
    <footer>
        <p style="font-family: Monaco"><a href="https://github.com/anouarac/suffix-automata-visualizer" style="color:#BF0065">anouarac</a> - 2021</p>
    </footer>
    </center>"""

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
