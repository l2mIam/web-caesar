from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
  <head>
    <style>
      form {{
        background-color: #eee;
        padding: 20px;
        margin: 0 auto;
        width: 540px;
        font: 16px sans-serif;
        border-radius: 10px;
      }}
      textarea {{
        margin: 10px 0;
        width: 540px;
        height: 120px;
      }}
    </style>
  </head>
  <body>
    <form action="/" method="POST">
      <div>
        <label for="rot">
          Rotate by: 
          <input name="rot" value="0" type="text"/>
          <p class="error"></p>
        </label>
      </div>
      <textarea name="text" type="text">{0}</textarea>
      <br>
      <input type="submit" value="Submit Query"/>
    </form>
  </body>
</html>
"""

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return form.format("")
    return "<h1>" + form.format(rotate_string(request.form['text'], int(request.form['rot']))) + "</h1>"

app.run()