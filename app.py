from llama_index import SimpleDirectoryReader,GPTListIndex,GPTVectorStoreIndex,LLMPredictor,PromptHelper
from langchain import OpenAI
import sys
import os
from llama_index import ServiceContext,StorageContext,load_index_from_storage
os.environ["OPENAI_API_KEY"] = "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"

from flask import Flask, render_template,request,jsonify

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form['msg']
    input = msg
    # response = answerMe(input)
    response = answerMe(input) 
    return response.response

def answerMe(questions):
    storageContext = StorageContext.from_defaults(persist_dir='json_data')
    index = load_index_from_storage(storageContext)
    quer_engine = index.as_query_engine()
    response = quer_engine.query(questions)
    return response


if __name__ == "__main__":
	app.run(port=5000)