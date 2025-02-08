import os
from datetime import timedelta
import pyodbc
from flask import Flask, request, session, render_template, jsonify, send_from_directory
from dotenv import load_dotenv


app = Flask(__name__, template_folder='templates')

TEMPLATES_DIR = os.path.join(os.getcwd(), 'templates')




@app.route('/rules')
def rules():
    if 'logged_in' in session:
        login = session['login']
        password = session['password']
        user_ip = session['user_ip']
        balance = session['shop_balance']
        return render_template('rules.html', login=login, password=password, user_ip=user_ip, shop_balance=balance)
    else:
        return render_template('rules.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)