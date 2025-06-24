from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'tu_secreto_aqui'  # Cambia esto por algo seguro

# Configuración Flask-Mail (ajusta con tus datos)
app.config['MAIL_SERVER'] = 'smtp.tu-servidor.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tu-email@dominio.com'
app.config['MAIL_PASSWORD'] = 'tu-contraseña'

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()
        fecha = request.form.get('fecha', '').strip()
        hora = request.form.get('hora', '').strip()
        motivo = request.form.get('motivo', '').strip()

        # Validaciones básicas
        if not nombre or not email or not fecha or not hora or not motivo:
            flash('Por favor, completa todos los campos.', 'danger')
            return redirect(url_for('index'))

        # Aquí puedes agregar validación más avanzada si quieres

        # Preparar correo
        subject = f'Nueva cita agendada por {nombre}'
        body = f"""
        Has recibido una nueva cita:

        Nombre: {nombre}
        Email: {email}
        Fecha: {fecha}
        Hora: {hora}
        Motivo: {motivo}
        """

        try:
            msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_USERNAME']])
            msg.body = body
            mail.send(msg)
            flash('Cita agendada correctamente, ¡gracias!', 'success')
        except Exception as e:
            print(f'Error al enviar correo: {e}')
            flash('Hubo un error al enviar el correo, intenta más tarde.', 'danger')

        return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
