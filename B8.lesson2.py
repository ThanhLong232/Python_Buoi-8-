#bài 2 Viết đoạn lệnh để kiểm tra xem một khóa có nằm trong từ điển không. Nếu có, xuất ra “Tồn tại giá trị trong từ điển với giá trị là v” với v là giá trị có trong từ điển. Nếu không, xuất ra là “Không có khóa k trong từ điển” với k là khóa đã nhập.
def dict_thatthuong(dictionary):
    keys = input("Nhập vào keys muốn kt: ")
    if keys in dictionary:
        a = dictionary[keys]
        print(f"Tồn tại giá trị trong từ điển với giá trị {a}")
    else:
        print(f"khong có kháo {keys} trong từ điển")

if __name__ == "__main__":
    dictionary = {"a":1, "b":2}
    dict_thatthuong(dictionary)