#Bài 4: Viết chương trình kiểm tra xem từ điển có rỗng không. Nếu có, in ra là “Từ điển rỗng”. Nếu không, in ra là “Từ điển không rỗng”.
def kt_phantu(dictionary):  
    if dictionary: 
        print("khong rong")
    else:
        print("rong")

if __name__ == "__main__":
    dictionary = {"a": 1, "b": 2, "c": 3.5, "d": "hello"}
    kt_phantu(dictionary)