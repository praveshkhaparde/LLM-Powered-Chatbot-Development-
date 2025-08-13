from flask import Flask, render_template, request
app = Flask(__name__, template_folder = ".")

nav_tag = """
    <ul>
        <li><a href = "."> Home Page </a></li>
        <li><a href = "/about"> About Page </a></li>
        <li><a href = "/third-page"> Third Page </a></li>
        <li><a href = "/calc-page"> Length Calculator </a></li>
    </ul>
"""

@app.route('/')
def home():
    return render_template("index.html") + nav_tag

@app.route('/about')
def about():
    return "About Page" + nav_tag

@app.route('/third-page')
def third_page():
    return "<marquee>Third Page</marquee>" + nav_tag

@app.route('/calc-page', methods = ['GET', 'POST'])
def calc_page():
    result = None
    if request.method == 'POST':
        text = request.form.get('text_input')
        result = len(text) if text is not None else None
    return nav_tag+render_template('calc.html', result = result)

if __name__ == '__main__':
    app.run(debug = True)