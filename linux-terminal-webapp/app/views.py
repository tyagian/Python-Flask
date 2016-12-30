
from flask import render_template
from app import app

@app.route('/')

def index():

 import subprocess

 cmd = subprocess.Popen(['sudo', 
 'free'],stdout=subprocess.PIPE,stderr=subprocess.PIPE) 
 out,error = cmd.communicate() 
 memory = out.splitlines() 
 return render_template('index.html', memory=memory)
