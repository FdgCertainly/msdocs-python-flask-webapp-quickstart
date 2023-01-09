from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from hello import answer_query_with_context 
from hello  import df
from hello  import document_embeddings
from hello import order_document_sections_by_query_similarity
from hello import vector_similarity
from hello import load_embeddings
from hello import get_query_embedding
from hello import construct_prompt

app = Flask(__name__)


@app.route('/chat')
def index():
   print('Request for index page received')
   return answer_query_with_context("Do you have 90s dresses?", df, document_embeddings)
#    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

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