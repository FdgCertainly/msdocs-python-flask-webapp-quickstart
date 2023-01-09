from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
# import openai
# import pandas as pd
# import numpy as np
# from transformers import GPT2TokenizerFast
# import pickle
# from dotenv import load_dotenv
# import os

from hello import answer_query_with_context,df, document_embeddings,  order_document_sections_by_query_similarity, vector_similarity, load_embeddings, get_query_embedding,  construct_prompt, OPEN_API_KEY


app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return answer_query_with_context("Do you have 90s dresses?", df, document_embeddings)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
   
   
# @app.route('/chat', methods=['GET','POST'])
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