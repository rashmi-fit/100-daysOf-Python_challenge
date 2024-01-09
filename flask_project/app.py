from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        button_value = request.form['button']
        if button_value == 'x':
            return redirect(url_for('yoga_session_book'))
        elif button_value == 'y':
            return redirect(url_for('self_learning'))
        elif button_value == 'z':
            return redirect(url_for('feedback'))
    return render_template('buttons.html')

@app.route('/yoga_session_book')
def yoga_session_book():
    return render_template('yoga_booking.html')

@app.route('/self_learning')
def self_learning():
    return render_template('learning_purpose.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback_form.html')

if __name__ == '__main__':
    app.run(debug=True)
