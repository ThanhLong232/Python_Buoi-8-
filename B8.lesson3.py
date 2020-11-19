# Bài 3: Viết chương trình xóa một phần tử với khóa cho trước khỏi từ điển. Xuất lại từ điển sau khi xóa.
def nhap_dl():
    while True:
        try:
            n = input("Nhập vào giá trị: ")
            if n.isnumeric():
                number = int(n)
                break
            else:
                number = n
                break
        finally:
            print("Mời Bạn tiếp tục chương trình.")
    return number
def xoa_khoapt(dictionary):
    keys = nhap_dl()
    del dictionary[keys]

if __name__ == "__main__":
    dictionary = {"a": 1, "b": 2, "c": 3.5, "d": "hello"}
    print(f"Từ điển trước khi xóa: {dictionary}")
    xoa_khoapt(dictionary)
    print(f"Từ điển sau trước khi xóa: {dictionary}")