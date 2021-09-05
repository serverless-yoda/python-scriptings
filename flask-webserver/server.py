from flask import Flask, render_template,request
from werkzeug.utils import redirect
import utility

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:pagename>")
def page_name(pagename):
    return render_template(pagename)



@app.route("/submit_form",methods=['POST','GET'] )
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            utility.save_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did not save to the database. Please try again'

    else:    
        return 'Something is wrong. Please try again'
