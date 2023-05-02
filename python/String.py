# Tạo một danh sách các số từ 1 đến 10
my_list = list(range(1, 11))

# Khai báo biến để lưu trữ tổng các số chẵn trong danh sách
sum_even = 0

# Khai báo biến để đếm số lần lặp
count = 0

# Sử dụng vòng lặp while để lặp qua danh sách các số
while my_list:
    num = my_list.pop(0) # Lấy phần tử đầu tiên của danh sách

    # Kiểm tra nếu số lẻ thì bỏ qua và tiếp tục vòng lặp
    if num % 2 == 1:
        continue

    # Cộng số chẵn vào tổng
    sum_even += num

    # Tăng biến đếm lên 1
    count += 1

    # Kiểm tra nếu đã lặp qua 5 phần tử thì dừng vòng lặp
    if count == 5:
        break
else:
    # Nếu vòng lặp không bị dừng bởi lệnh break, thì in ra thông báo
    print("Đã lặp qua toàn bộ danh sách")

# In ra tổng các số chẵn đã tìm được
print("Tổng các số chẵn là:", sum_even)
