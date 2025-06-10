from flask import Flask, render_template, request, redirect
import mysql.connector # type: ignore

app = Flask(__name__)

# Conexión a MySQL
def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',         # Cambia esto si usas otro usuario
        password='',         # Coloca tu contraseña de MySQL aquí
        database='flask_db'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        correo = request.form['correo']
        password = request.form['password']

        conn = get_connection()
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO usuarios (username, correo, password) VALUES (%s, %s, %s)"
            valores = (username, correo, password)
            cursor.execute(sql, valores)
            conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()

        return redirect('/login')
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            return redirect('/')
        else:
            return "Credenciales incorrectas"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

