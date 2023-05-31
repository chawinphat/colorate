from flask import Flask, jsonify, request
app = Flask(__name__)

defaultPalette = ['#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF']

@app.route('/generate')
def get_colors():
    return jsonify(defaultPalette)

