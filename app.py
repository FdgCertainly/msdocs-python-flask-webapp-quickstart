from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

import os

# from hello import answer_query_with_context, df, document_embeddings


app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
   
   
# @app.route('/chat')
# def chat():
#     print('Request for chat page received')
#     return answer_query_with_context("Do you have 90s dresses?", df, document_embeddings)

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))



if __name__ == '__main__':
   app.run()