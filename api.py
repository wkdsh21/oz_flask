from http.client import responses

from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schemas import BookSchema

blp = Blueprint('books', __name__, url_prefix='/books', description='Operations on books')

# 데이터 저장소
books = []
id_cur=0
# 엔드포인트 구현...
@blp.route('/')
class BookList(MethodView):
    # 책 전체 반환
    @blp.response(200,BookSchema(many=True))
    def get(self):
        return books
    # 책 저장
    @blp.arguments(BookSchema)
    @blp.response(201,description="Book added")
    def post(self,book):
        global id_cur
        id_cur+=1
        book.update({"book_id":id_cur})
        books.append(book)
        return book

@blp.route('/<int:book_id>')
class Book(MethodView):
    @blp.arguments(BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book_id == book["book_id"]), None)
        if book is None:
            abort(404, massage="Book not found")
        book.update(new_data)
        return book

    @blp.response(204)
    def delete(self, book_id):
        books_len=len(books)
        for book in books:
            if book_id == book["book_id"]:
                books.remove(book)
        if books_len ==len(books):
            abort(404, massage="Book not found")
        return ""




