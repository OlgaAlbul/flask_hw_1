from flask import Flask, render_template

app = Flask(__name__)


@app.route('/main/')
def start_page():
    context = {
        'title': 'Мой магазин'
    }
    return render_template('main.html', **context)


@app.route('/clothes/')
def closes():
    context = {
        'title': 'Одежда'
    }
    return render_template('clothes.html', **context)


@app.route('/shoes/')
def shoes():
    context = {
        'title': 'Обувь'
    }
    return render_template('shoes.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
