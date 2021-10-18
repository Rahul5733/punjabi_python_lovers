from flask import Flask

app = Flask(__name__)

@app.route("/kuldeepmanak")
def hello_world():
    return "<h1>cheti kar serwan puttra!</h1><h2>wdia gana!</h2><p>written by totu abd sabng by the legend Kuldeep manak!</p>"

@app.route("/sujeetpatar")
def hello_world2():
    return "<h1>cheti kar serwan puttra!</h1><h2>wdia gana!</h2><p>written by totu abd sabng by the legend sujeet patar!</p>"

@app.route("/manmohanwaris")
def hello_world3():
    return "<h1>cheti kar serwan puttra!</h1><h2>wdia gana!</h2><p>written by totu abd sabng by the legend sujeet patar!</p>"
