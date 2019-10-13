# import library

from flask import Flask, render_template, request
from threading import Thread
import table as t  # table class that get data from database
import schedule
import time
import xml_parse
from flask_apscheduler import APScheduler



# Configuration for APScheduler
class Config(object):

    JOBS = [

        {
            'id': 'job2',
            'func': '__main__:xml_parse.check_new',
            'args': (),
            'trigger': 'interval',
            'seconds': 1800,
        }
    ]





application = Flask(__name__)
application.config.from_object(Config())
table = t.recall_table()


@application.route('/')
def home():

    return render_template('login.html')


@application.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    error = None
    if request.method == 'POST':
        if request.form['password'] == 'password':
            # session['logged_in'] = True
            return render_template('it3_index_integrate.html', table=t.recall_table())

        else:
            error = "Invalid Credentials.Try again!"
            return render_template("login.html",error = error)
    else:
        return render_template('login.html')





@application.route('/iteration_2')
def iteration_2():

    return render_template('it_2_login.html')


@application.route('/iteration_2_login', methods=['POST'])
def it2_admin_login():
    error = None
    if request.method == 'POST':
        if request.form['password'] == 'password':
            # session['logged_in'] = True
            return render_template('index.html', table=t.recall_table())

        else:
            error = "Invalid Credentials.Try again!"
            return render_template("it_2_login.html",error = error)
    else:
        return render_template('it_2_login.html')




# iteration 2 recall page
@application.route("/recall")
def recall():
    return render_template('recall.html', table=t.recall_table())


# iteration 2 statistics page
@application.route("/statistics")
def statistics():
    return render_template('statistics.html')


# iteration 2 tips page
@application.route("/tips")
def tips():
    return render_template('tips.html')


# iteration 2 team page
@application.route("/team")
def team():
    return render_template('team.html')


# schedule for routine check of food recall news
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)






# main function
if __name__ == '__main__':

    scheduler = APScheduler()
    scheduler.init_app(application)
    scheduler.start()
    application.run(debug=False)  # start web page
