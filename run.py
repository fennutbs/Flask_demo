# -*- coding:utf-8 -*-

from app import app
from app.analysis import  analysis_bp
from app.query import query_bp

app.register_blueprint(analysis_bp)
app.register_blueprint(query_bp)

if __name__ == "__main__":
    # app.run(debug=True, ssl_context=("ca/server-cert.pem","ca/server-key.pem"))
    app.run(debug=True)
