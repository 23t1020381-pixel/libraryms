from flask import Flask, render_template, abort, request
app = Flask(__name__)

BOOKS = [
 {"id":1,"title":"Dế Mèn phiêu lưu ký","author":"Tô Hoài","category":"Văn học","year":1941,"available":True,"description":"Tác phẩm thiếu nhi nổi tiếng của văn học Việt Nam."},
 {"id":2,"title":"Tắt đèn","author":"Ngô Tất Tố","category":"Văn học","year":1939,"available":True,"description":"Tiểu thuyết hiện thực về đời sống nông thôn."},
 {"id":3,"title":"Python cơ bản","author":"Nguyễn Văn A","category":"Công nghệ","year":2024,"available":True,"description":"Nhập môn lập trình Python."},
 {"id":4,"title":"Cơ sở dữ liệu","author":"Trần Văn B","category":"Công nghệ","year":2023,"available":False,"description":"Các khái niệm cơ bản về hệ quản trị cơ sở dữ liệu."},
 {"id":5,"title":"Nhà giả kim","author":"Paulo Coelho","category":"Tiểu thuyết","year":2025,"available":True,"description":"Câu chuyện về hành trình theo đuổi ước mơ."},
 {"id":6,"title":"Tuổi trẻ đáng giá bao nhiêu","author":"Rosie Nguyễn","category":"Kỹ năng","year":2022,"available":False,"description":"Gợi ý về học tập, trải nghiệm và trưởng thành."},
 {"id":7,"title":"Clean Code","author":"Robert C. Martin","category":"Công nghệ","year":2026,"available":True,"description":"Nguyên tắc viết mã nguồn dễ đọc và bảo trì."},
 {"id":8,"title":"Cho tôi xin một vé đi tuổi thơ","author":"Nguyễn Nhật Ánh","category":"Văn học","year":2021,"available":True,"description":"Tác phẩm về tuổi thơ và ký ức."},
]
@app.context_processor
def inject_categories():
    return {"all_categories": sorted({b["category"] for b in BOOKS})}

@app.route("/")
def home():
    recent = sorted(BOOKS, key=lambda b:b["year"], reverse=True)[:3]
    return render_template("index.html", total=len(BOOKS),
        available=sum(1 for b in BOOKS if b["available"]), recent=recent)

@app.route("/books")
def books():
    category=request.args.get("category","")
    columns=request.args.get("cols", "3", type=str)
    if columns not in ("1","2","3"): columns="3"
    filtered=[b for b in BOOKS if not category or b["category"]==category]
    return render_template("books.html", books=filtered, category=category, columns=columns)

@app.route("/books/<int:book_id>")
def book_detail(book_id):
    book=next((b for b in BOOKS if b["id"]==book_id),None)
    if book is None: abort(404, description=f"Không tìm thấy sách có mã {book_id}.")
    return render_template("book_detail.html", book=book)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", message=error.description or "Trang không tồn tại."),404

@app.route("/api/books")
def api_books():
    from flask import jsonify
    return jsonify(BOOKS)

if __name__=="__main__":
    app.run(debug=True)
