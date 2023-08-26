gunicorn -w 8 'app:app' -b '[::]:443' --certfile ./certificate.pem --keyfile ./key.pem
