from flask import Flask, app,render_template,request
import requests
import json
app = Flask(__name__)

@app.route("/" )
def index():
    return render_template("index.html")



@app.route("/translated" ,methods=["POST","GET"])
def translated():
    text=request.form.get("English")
    url = "https://freekode.centeltech.com/api/minions?txt={}".format(text)
    response = requests.get(url).text
    dict_json= json.loads(response)
    return render_template("index.html",translation= dict_json["translated"])





if __name__=="__main__":
    app.run(debug=True)
