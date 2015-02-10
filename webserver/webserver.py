from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

# Template rendering example
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
  return render_template('hello.html', name=name)

# JSON response example
@app.route("/json")
def json():
  return jsonify(first_name='John', last_name='Wayne')

if __name__ == "__main__":
  # This will enable hot reloading, so you don't need to restart each time
  # after making a change
  # MAKE SURE TO DISABLE IN PRODUCTION
  app.debug = True

  app.run(host='0.0.0.0')
