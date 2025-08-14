from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page: handles GET and POST (for secret code input)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        entered_code = request.form.get('secret_code')
        if entered_code == "teri maa ki choot behenchod madarchod lawde gandu dalle ": # replace with actual code
            return redirect(url_for('employee'))
        else:
            return render_template('code__prompt.html', error="Incorrect secret code.")
    return render_template('code__prompt.html')

# Employee Page
@app.route('/employee')
def employee():
    return render_template('employee.html')

# This is just to ensure your site is running
if __name__ == '__main__':
    app.run(debug=True)
