from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_name(page_name=None):
    return render_template(page_name)


# def store_data(data):
#     with open('./database.txt', mode='w') as database:
#         email = data['Email']
#         subject = data['Subject']
#         message = data['Message']
#         file = database.write(f'{email}, {subject}, {message}\n')


def store_data_csv(data):
    with open('./database.csv', newline='\n', mode='a') as csv_database:
        email = data['Email']
        subject = data['Subject']
        message = data['Message']
        csv_file = csv.writer(csv_database, delimiter=',',
                              quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # store_data(data)
            store_data_csv(data)
            return redirect('submitted.html')
        except:
            return 'Error: Did not save to database.'
    else:
        return 'Error: Something went wrong. Try Again.'
