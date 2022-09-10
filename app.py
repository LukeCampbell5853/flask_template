from flask import *

app = Flask(__name__, static_url_path='/static')

@app.route("/")

def index():
  return(render_template("home.html"))

@app.route("/echo",methods=["POST"])

def echo():
  data = request.data
  return(data)
  
if __name__ == '__main__':
  app.run(debug = True, host="0.0.0.0")
