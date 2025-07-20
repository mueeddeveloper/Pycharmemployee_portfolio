from flask import Flask, render_template, request, redirect

app = Flask(__name__)
SECRET_CODE = "1234" # You can change this to your desired secret code

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/employee', methods=['GET', 'POST'])
def employee():
    if request.method == 'POST':
        entered_code = request.form.get('secret_code')
        if entered_code == SECRET_CODE:
            return render_template("employee.html")
        else:
            return render_template("code_prompt.html", error="Incorrect secret code.")
    return render_template("code_prompt.html", error=None)

@app.route('/visit')
def visit():
    return redirect("https://indiasgoldenpast.netlify.app/", code=302)

if __name__ == '__main__':
    app.run(debug=True)

