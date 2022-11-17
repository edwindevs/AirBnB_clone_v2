#!/usr/bin/python3
''' scrip to start flask '''
from flask import Flask, render_template
from models.state import State
from models import storage
from operator import getitem
app = Flask(__name__)



@app.route('/states_list', strict_slashes=False)
def state_list():
    '''return all storage and renders the html template'''
    all_obj = storage.all(State)
    return render_template('7-states_list.html', states=all_obj)


@app.teardown_appcontext
def teardown_context_session(self):
    '''return the storage'''
    # return storage.close()
    storage.close()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
