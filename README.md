# Reverse Proxy for CPSC 362

This is the source behind the the [Dev362](https://dev362.amyip.net)
development server. It allows both the display of the primary dev
instance, as well as the dev instances of team members. 

It's not of itself designed to be used for other people or projects;
it uses hard-coded values in the Flask script. However, it's entirely
possible to either use the existing format to adapt it to your needs.
You can also generate functions iteratively and link them to a 
configuration file - if you want help doing this, 
[contact Amy](mailto:amy@amyip.net).

## Setting Up

Before setting this up, determine if something like NGINX or Apache
works better for your needs; chances are it does. 

This reverse proxy also requires that you use non-root relative 
addressing; if you have common JS across mutliple pages, this 
usually won't work. For instance, if you're trying to access/link 
`http://sitename/username/endpoint.html` through general code,
and you're currently in `http://sitename/username/folder/site.html`,
references would need to be as `../endpoint.html`, NOT `/endpoint.html`.
As a result, sanitization of URLs often doesn't work; **DO NOT** accept
user-generated or dynamic endpoints for redirects and resource fetching
without being extremely careful.

### Installing Dependencies

While this can be done manually, we recommend just using a venv:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

The `source` command should always be run if you drop the current environment scope.

### Generating Keys

If you're fine with self-signed certificates, or if this instance
is behind another reverse proxy (like NGINX or Apache), the following
will generate the necessary files:

```bash
openssl req -newkey rsa:4096 -nodes -keyout key.pem -x509 -days 36500 -out certificate.pem
```

Be very careful not to leak your keys.

If you're exposing this as production directly to the public, you need
to get keys from a Certificate Authority (CA) instead. The easiest
way to use this is to use Certbot to get keys from Let's Encrypt,
which you can find [here](https://certbot.eff.org/).

### Running

You can launch the server by:

```bash
./run.sh
```

This launches the server in Gunicorn, a production-grade WSGI server.

If you want to run in Werkzeug (a dev-grade) server instead:

```bash
python3 app.py
```

Note that it will default to port 5000, which might not work with your configuration
(by default it doesn't), and will not use SSL. This can be configured by changing
the `app.run()` at the end of `app.py`.
