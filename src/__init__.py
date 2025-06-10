from flask import Flask
import os

__version__ = "0.0.1dev"

# extract dir portion from absolute path of the file
currentDir = os.path.dirname(os.path.abspath(__file__))

templateDir = os.path.join(currentDir, '..', 'templates')
staticDir = os.path.join(currentDir, '..', 'static')

app = Flask(
    __name__,
    template_folder=templateDir,
    static_folder=staticDir
)

# config upload and processed folders
app.config['UPLOAD_FOLDER'] = os.path.join(currentDir, '..', 'uploads')
app.config['PROCESSED_FOLDER'] = os.path.join(currentDir, '..', 'processed')

# ensure them two dirs exist lol
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

from . import routes