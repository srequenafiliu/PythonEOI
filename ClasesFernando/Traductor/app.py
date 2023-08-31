from flask import Flask
from transformers import pipeline
from flask_cors import CORS;
app = Flask(__name__)
CORS(app)
models = ["en-es", "es-en"]
pipes = []
for model in models:
    model = f"Helsinki-NLP/opus-mt-{model}"
    pipes.append(pipeline("translation", model=model, max_length=1024))
@app.route('/<source>/<target>/<text>')
def translate(source, target, text):
    i = models.index(f"{source}-{target}")
    return pipes[i](text)[0]["translation_text"]