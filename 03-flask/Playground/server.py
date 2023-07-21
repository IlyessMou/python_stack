from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def render_blue_boxes():
    return render_template('blue_boxes.html', times=3, color='blue')

@app.route('/play/<int:times>')
def render_custom_boxes(times):
    return render_template('blue_boxes.html', times=times, color='blue')

@app.route('/play/<int:times>/<color>')
def render_custom_colored_boxes(times, color):
    return render_template('blue_boxes.html', times=times, color=color)

if __name__ == '__main__':
    app.run(debug=True)