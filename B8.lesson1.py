#Bài 1:.1 Viết một đoạn lệnh cho phép người dùng thêm một khóa vào từ điển. Trong đó khóa và giá trị do người dùng chỉ định:
def nhap_dict(n):
    dict={}
    for i in range(3):
        print(f"Nhập vào key thứ {i+1}: ")
        keys = nhap_dl()
        print(f"Nhập vào values thứ {i+1}: ")
        values = nhap_dl()
        dict[keys] = values
        print()
    return dict

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

if __name__ == "__main__":
    n = int(input("Nhập vào số lượng phần tử: "))
    dictionary = nhap_dict(n)
    print(f"Các phần tử vừa nhập là: {dictionary}")