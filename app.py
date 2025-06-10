from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de conexión MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'flask_db'
}

@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM persona")
    personas = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', personas=personas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO persona (nombre) VALUES (%s)", (nombre,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('agregar.html')

if __name__ == '__main__':
    app.run(debug=True)
