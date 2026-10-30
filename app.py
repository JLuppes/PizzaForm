from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/pizza', methods=["GET", "POST"])
def pizzaFormPage():

    if request.method == "POST":

        formPizzaName = request.form.get('pizzaName')


        return render_template('pizzaSuccess.html', pizzaName=formPizzaName)

    return render_template('pizzaForm.html')