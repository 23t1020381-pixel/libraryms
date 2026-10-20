# LibraryMS v0.2

## Chạy ứng dụng
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
flask --app app run --debug
```
Mở `http://127.0.0.1:5000`.

## Kiểm tra
- `/` trang chủ, thống kê số đầu sách/sách sẵn sàng và 3 sách mới.
- `/books` danh sách, lọc thể loại, chọn 1/2/3 cột.
- `/books/1` chi tiết sách; thử `/books/999` để kiểm tra trang 404.
- `/api/books` API JSON.
- `base.html` dùng chung; `macros.html` có `book_card(book)` và `status_badge(available)`.
- `app.py` chỉ xử lý dữ liệu/route, không chứa HTML và không dùng `escape()`.

## Git commit và tag
```powershell
git init
git add .
git commit -m "Hoan thanh LibraryMS v0.2"
git tag v0.2
git tag
```
Lệnh chạy bằng termiral:
cd C:\ma_nguon_mo\libraryms
py -m pip install -r requirements.txt
flask --app app run --debug
