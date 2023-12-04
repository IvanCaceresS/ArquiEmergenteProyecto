from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/images', methods=['POST'])
def images():
    data = request.get_json()
    
    image_id = data.get('id')
    filename = data.get('filename')

    # Aquí puedes agregar lógica adicional para validar el archivo o el ID

    url = f'http://127.0.0.1:8000/{filename}'
    return jsonify({'id': image_id, 'url': url})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
