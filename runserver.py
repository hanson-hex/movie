# -*- encoding=utf-8 -*-
from app import app


if __name__ == '__main__':
    config = dict(
        host='0.0.0.0',
        port=2003,
        debug=True
    )
    app.run(**config)