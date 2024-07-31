# Litestar-CouchDB

[![image](https://img.shields.io/pypi/v/litestar-couchdb.svg)](https://pypi.python.org/pypi/litestar-couchdb)

[![image](https://img.shields.io/travis/dekoza/litestar-couchdb.svg)](https://travis-ci.com/dekoza/litestar-couchdb)

[![Documentation Status](https://readthedocs.org/projects/litestar-couchdb/badge/?version=latest)](https://litestar-couchdb.readthedocs.io/en/latest/?version=latest)

CouchDB integration for Litestar.

-   Free software: Apache Software License 2.0
-   Documentation: <https://litestar-couchdb.readthedocs.io>.

## Features

-   Provides convenient Repository for CouchDB adhering to Litestar\'s
    AbstractRepository.

```python
from litestar_couchdb import CouchRepository
from msgspec import Struct
from myproject.schema import MyModelSchema


class MyModelRepository(CouchRepository):
    model_type: Struct = MyModelSchema

```

...and you're done.

## Credits

Created by Dominik Kozaczko
