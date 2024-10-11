from marshmallow import Schema, fields

class BookSchema(Schema):
    book_id=fields.Int(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)