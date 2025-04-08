from flask import *
from chatbot import respuesta
from flask import Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    pregunta = None
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        pregunta = request.form['pregunta']
        respuesta_usuario = respuesta(pregunta)
        
        return Response(render_template('index.html', answer=respuesta_usuario), content_type="text/html; charset=utf-8")

if __name__ == '__main__':
    app.run(debug=True)