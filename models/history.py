__author__ = "Paulo Antunes"
__copyright__ = "Copyright 2018, XTCryptoSignals"
__credits__ = ["Paulo Antunes", ]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Paulo Antunes"
__email__ = "pjmlantunes@gmail.com"


from mongoengine import (
    Document,
    StringField,
    DecimalField,
    IntField,
    DateTimeField
)
import settings as s


class History(Document):
    symbol = StringField(required=True)
    source = StringField(required=True)
    price = DecimalField(required=True, precision=s.SYMBOL_FLOAT_PRECISION)
    number_trades_24h = IntField()
    volume_24h = DecimalField(precision=s.SYMBOL_FLOAT_PRECISION)
    price_change_percent = DecimalField(precision=2)
    number_trades_change_percent = DecimalField(precision=2)
    volume_change_percent = DecimalField(precision=2)
    created_on = DateTimeField(required=True)

    meta = {
        'abstract': True,
        'indexes': [
            ("-created_on", ),
        ],
        'ordering': ['-created_on'],
    }

    def get_object(self):
        item = {}
        for k in self._fields.keys():
            if k == "id":
                continue
            if k in ['symbol', 'source', 'price', 'number_trades', 'volume']:
                item[k] = self[k]
                continue
            if k in ['created_on']:
                item[k] = str(self[k])
                continue
        return item


class History10s(History):
    pass


class History30s(History):
    pass


class History1m(History):
    pass


class History10m(History):
    pass


class History30m(History):
    pass


class History1h(History):
    pass


class History3h(History):
    pass


class History6h(History):
    pass


class History12h(History):
    pass


class History24h(History):
    pass
