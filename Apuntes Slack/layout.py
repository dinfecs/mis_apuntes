<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.min.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
</head>
<body>
    <nav>
        <ul>
            {% block nav %}{% endblock %}
        </ul>
    </nav>
    <section>
        {% block body %}{% endblock %}
    </section>
    <footer>
        &copy;2017 Andros Fenollosa
    </footer>
</body>
</html>