from flask import Flask, render_template, request, redirect
import os

sistema = Flask(__name__)


@sistema.route('/Loving Bordado')
def homepage():
    return render_template('index.html')


sistema.run(debug=True)
