from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
  return render_template('hello.html', name=name)

if __name__ == "__main__":
  # This will enable hot reloading, so you don't need to restart each time
  # after making a change
  # MAKE SURE TO DISABLE IN PRODUCTION
  app.debug = True

  app.run()
