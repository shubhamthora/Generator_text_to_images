from flask import Flask  , jsonify
from flask import render_template
import openai
api= "api"
app = Flask(__name__,template_folder='templates')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt:", prompt)
  response = openai.Image.create(prompt=prompt, n=5, size="256x256") 
  print(response)
  return jsonify(response)

 

if __name__ == '__main__':

    app.run(debug=True)