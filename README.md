# Tính toán và phân tích điểm thi (Test Grade Calculator)
Chương trình được xây dựng để giúp thực hiện chấm điểm và phân tích kết quả thi của các học sinh ở nhiều lớp khác nhau. Mục đích của chương trình là giúp giảm thời gian chấm điểm.

## Yêu cầu khi xây dựng và sử dụng chuơng trình Test Grade Calculator
- Cần cài đặt Python với phiên bản từ 3.9 trở lên.
- Tải (Clone) chương trình từ Github về máy local để chạy như sau: _Chương trình được lưu trữ trên Github tại nhánh chính (master branch)_
  - Tại máy local tạo 1 thư mục để chứa tệp chương trình sẽ được tải về từ github
  - Từ terminal bạn sử dụng câu lệnh sau để chỉ đến thư mục mới tạo `cd` _'tên đường dẫn thư mục vừa tạo'_ (vd: cd /users/desktop/abc)
  - Tiếp đến bạn sử dụng câu lệnh sau để clone chương trình về: `git clone` _'đường dẫn được lấy từ github'_
    - Cách lấy _'đường dẫn được lấy từ github'_ theo hướng dẫn hình bên dưới:
    <img width="430" alt="Github" src="https://github.com/Quincy85/Quincy85-DAP304x_asm1_quynhnkhFX23192/assets/106717665/002e1690-1b1e-46eb-a54d-25ae5b7b4885">
  - Lúc này toàn bộ chương trình đã được tải về máy local để bạn chạy chương trình


## Các bước xây dựng chương trình "Test Grade Calculator"
### A. Import các thư viện cần thiết
#### 1. Thực hiện cài `Pandas`, `NumPy`, `Regex` nếu máy tính của bạn chưa được cài trước đó bằng cách: ***(Trường hợp đã cài đặt các thư viện này rồi bạn hãy bỏ qua bước này.)***
  ```
  pip install pandas
  pip install numpy
  pip install regex
  ```
#### 2. Import các thư viện `pandas`, `numpy` và `re` trước khi xây dựng các hàm chạy chương trình
  ```
  import numpy as np
  import pandas as pd
  import re
  ```
### B. Xây dựng các hàm và câu lệnh để thực hiện các bước của chương trình chấm điểm
### I. Mở các tệp dữ liệu bên ngoài được yêu cầu
#### 1. Tạo hàm (function) thực hiện việc mở file
- Function này có tên là `open_File` với biến đầu vào là tên file người dùng nhập vào (ở đây là `class_name`)
- Chúng ta sẽ sử dụng `try/except` để thực hiện việc mở file:
  - Trường hợp file được tìm thấy sẽ sử dụng `pd.read_csv` để thực hiện mở file. *Lưu ý*: cần thêm 2 tham số `delimiter='\t'` & `header=None` để định dạng lại file đọc
  - Trường hợp file không được tìm thấy sẽ `return None`
#### 2. Tạo function in kết quả mở file
- Function này có tên là `print_Open_File_Result` với biên đầu vào là `class_name`.
- Function này sẽ thực hiện in kết quả sau khi chạy hàm `open_File`:
  - Trường hợp đọc file thành công sẽ in ra thông báo: "Successfully opened `class_name`.txt"
  - Trường hợp file không tìm thấy sẽ in thông báo: “File `class_name`.txt cannot be found”
#### 3. Xuất kết quả đọc file theo tên file mà người dùng đã nhập
- Viết câu lệnh để yêu cầu người dùng nhập tên file cần mở vào và gán vào biến `class_name`:
  
  ```
  class_name = input("\nEnter a file name (i.e. class1 for class1.txt):")
  ```
- Thực hiện gọi function `print_Open_File_Result`
  
  ```
  print_Open_File_Result(class_name)
  ```
### II. Scan file và phân tích
#### 1. Tạo function thực hiện kiểm tra các thông tin trong file
- Function này có tên là `check_File` với biên đầu vào là `file` được mở
- Khởi tạo các biến `global` cái sẽ được sử dụng cho các hàm xuất báo cáo và chấm điểm ở các bước sau. Các biến gồm:
  - `num_lines`: số lượng dòng có trong file     
  - `num_valid`: số lượng dòng hợp lệ
  - `num_invalid`: số lượng dòng không hợp lệ
  - `ID_number_pattern`: biến xác định các điều kiện hợp lệ của mã học sinh
  - `valid_list`: danh sách chứa các dòng hợp lệ
  - `invalid_list`: danh sách chứa các dòng không hợp lệ
- Dùng vòng lặp for để đi qua các dòng của file và xem xét các điều kiện theo yêu cầu, cụ thể:
  - Lấy từng dòng trong file (đang ở dạng dataframe) chuyển sang chuỗi (string) và gán vào biến `row`: sử dụng `.iloc[index].reset_index(drop=True).squeeze()`
  - Thực hiện tách các giá trị trong từng dòng ra với `.split(',')` và gán vào biến `splited_row`
  - Lấy mã học sinh ở vị trị đầu tiền của dòng đã được tách ở trên `splited_row[0]`
  - Sử dụng `if/else` để so sánh các dòng và mã số học sinh được lấy từ file để xác định các dòng hợp lệ và không hợp lệ, cụ thể:
    - Mã học sinh phải đảm bảo khớp với điều kiện được xác định của biến `ID_number_pattern`, gồm: bắt đầu bằng N và theo đó sẽ là 8 chữ số.
    - Số lượng các giá trị trong một dòng phải là 26.
  - Sau đó sẽ thêm các dòng hợp lệ và không hợp lệ vào danh sách tương ứng được khởi tạo từ trước
- Cuối cùng đếm số lượng các dòng hợp lệ và không hợp lệ để lập báo cáo
#### 2. Tạo function tạo báo cáo (report) sau khi thực hiện kiểm tra file
- Function này có tên là `create_Checked_File_Report` với biến đầu vào là `file` cần tạo báo cáo
- Gọi hàm `check_File` để thực hiện kiểm tra thông tin file trước khi tạo báo cáo.
- Báo cáo gồm 2 phần:
  - Phân tích các dòng lỗi trong file
    - Sử dụng vòng lặp for để đi qua các dòng nằm trong danh sách không hợp lệ (`invalid_list`) để:
      - Lấy các giá trị trong 1 dòng và mã số sinh viên
      - Dùng `if/else` xác định các dòng không hợp lệ để in ra thông báo với các lỗi tương ứng:
        - Lỗi do mã sinh viên không hợp lệ: ***"Invalid line of data: N# is invalid: ...."***
        - Lỗi do số lượng các giá trị trong dòng khác 26: ***"Invalid line of data: does not contain exactly 26 values: ..."***
    - Trong trường hợp file không có dòng không hợp lệ sẽ in ra thông báo: ***"No errors found!"***
  - Báo cáo tổng hợp gồm:
    - Tổng số dòng trong file: ***"Total lines of data: xx"***
    - Tổng số dòng hợp lệ: ***"Total valid lines of data: xx"***
    - Tổng số dòng không hợp lệ: ***"Total invalid lines of data: xx"***
#### 3. Tạo function chạy chương trình kiểm tra và xuất báo cáo phân tích file
- Function này có tên là `print_Checked_File_Report` với biến đầu vào là tên file cần thực hiện (`class_name`)
- Ở đây ta chỉ cần gọi các function `open_File` & `create_Checked_File_Report` đã được tạo ở trên
#### 4. Xuất báo cáo tổng hợp tính hợp lệ của dữ liệu trong file được nhập bởi người dùng
Gọi function `print_Checked_File_Report`
  ```
  print_Checked_File_Report(class_name)
  ```
### III. Tính toán điểm thi
#### 1. Tạo function thực hiện tính điểm thi
- Function này có tên là `calculate_Grades` với biên đầu vào là `file` được mở
- Khởi tạo các biến `global` cái sẽ được sử dụng cho các hàm xuất báo cáo và chấm điểm ở các bước sau. Các biến gồm:
  - `num_student_high_scores`: số lượng học sinh đạt điểm cao (>80)     
  - `mean_student_score`: Điểm trung bình
  - `max_student_scor`: Điểm cao nhất
  - `min_student_score`: Điểm thấp nhất
  - `range_of_score`: Miền giá trị của điểm (cao nhất trừ thấp nhất).
  - `median_score`: Giá trị trung vị (Sắp xếp các điểm theo thứ tự tăng dần. Nếu # học sinh là số lẻ, bạn có thể lấy giá trị nằm ở giữa của tất cả các điểm (tức là [0, 50, 100] —      trung vị là 50). Nếu # học sinh là chẵn bạn có thể tính giá trị trung vị bằng cách lấy giá trị trung bình của hai giá trị giữa (tức là [0, 50, 60, 100] — giá trị trung vị         là 55))
  - `max_skipped_answers_list`: Danh sách các câu hỏi bị học sinh bỏ qua nhiều nhất theo thứ tự: số thứ tự câu hỏi - số lượng học sinh bỏ qua -  tỉ lệ bị bỏ qua.
  - `max_incorrect_answers_list`: Danh sách các câu hỏi bị học sinh sai qua nhiều nhất theo thứ tự: số thứ tự câu hỏi - số lượng học sinh trả lời sai - tỉ lệ bị sai.
  - `total_student_grades`: Danh sách chứa điểm của tất cả các học sinh.
- Gọi hàm `check_File` để thực hiện kiểm tra thông tin file trước khi tạo báo cáo.
- Sử dụng `.split(',')` để tách chuỗi đại diện cho các câu trả lời đúng (`anwser_key`) tạo thành một danh sách
- Khởi tạo một danh sách chứa điểm của tất cả các học sinh (`total_student_grades`)
- Sử dụng vòng lặp `for` để đi qua các câu trả lời của từng học sinh (chỉ tính cho các dữ liệu nằm trong danh sách hợp lệ)  
  - Khởi tạo một danh sách để chứa điểm của các học sinh 
  - Tiếp tục sử dụng thêm 1 vòng lặp `for` để thực hiện so sánh các câu trả lời của học sinh với anwser_key và thêm kết quả vào danh sách chứa điểm của học sinh đó. Sử dụng           `if/else` và `.apend()` để thực hiện *(Lưu ý: cần bỏ vị trí đầu tiên của list là mã ID của học sinh)*
    - +4 điểm cho mỗi câu trả lời đúng: giá trị giống với `anwser_key` 
    - 0 điểm cho mỗi câu trả lời bị bỏ qua: giá trị rỗng 
    - -1 điểm cho mỗi câu trả lời sai: giá trị khác với `anwser_key`
  - Thực hiện chuyển danh sách tổng điểm của toàn bộ học sinh trong lớp thành dataFrame và thêm cột tính tổng điểm của từng học sinh
    - Sử dụng `pd.DataFrame()` để chuyển sang dataFrame
    - Sử dụng `.sum(axis=1)` để thêm cột tính điểm cho từng học sinh
- Sau khi có bảng (dataFrame) chứa điểm của tất cả học sinh, chúng ta thực hiện tính toán thống kê, gồm:
  - Đếm số lượng học sinh có điểm lớn hơn 80 với `len()`
  - Tính điểm trung bình với `.mean()`
  - Xác định điểm cao nhất với `.max()`
  - Xác định điểm cao nhất với `.min()`
  - Tính miền giá trị của điểm: điểm cao nhất - điểm cao nhất
  - Tính điểm trung vị: `.median()`
  - Để xác định các câu trả lời bị bỏ qua và trả lời sai nhiều nhất ta phải thực hiện thêm một số bước sau:
    - Khởi tạo các danh sách chứa số lượng các câu trả lời bị bỏ qua và vị trí tương ứng của nó
    - Thực hiện vòng lặp để đi qua từng câu trả lời của tất cả học sinh và thực hiện đếm số lượng câu bị bỏ qua và trả lời sai.
      - Sử dụng `.value_counts()[0]`: để đếm số lượng các câu trả lời bị bỏ qua
      - Sử dụng `value_counts()[-1]`: để đếm số lượng các câu trả lời bị sai
      - Sử dụng `try/except` để bỏ qua lỗi trong trường hợp không tìm thấy giá trị cần đếm
      - Thêm số lượng đếm được và vị trí tương ứng vào danh sách được khởi tạo
    - Từ danh sách số lượng các câu trả lời bị bỏ qua và trả lời sai tìm giá trị lớn nhất
    - Khởi tạo các danh sách chứa kết quả các câu trả lời bị bỏ qua và bị sai nhiều nhất theo thứ tự:
      ***số thứ tự câu hỏi - số lượng học sinh trả lời sai/bỏ quả - tỉ lệ bị sai/bỏ qua***
    - Tiếp tục sử dụng các vòng lặp `for` kết hợp `if/else` để tìm vị trí câu trả lời có lượng học sinh bỏ qua và sai nhiều nhất. Từ đó lưu kết quả vào danh sách được khởi tạo ở        trên.
#### 2. Tạo function để tạo báo cáo thống kê
- Function này có tên là `create_Grade_Report` với biên đầu vào là `file` được mở
- Gọi hàm `calculate_Grades` để thực hiện tính toán và thống kê điểm thi của file được mở.
- Báo cáo thống kê bao gồm:
  - Số lượng học sinh đạt điểm cao (>80): **_Total student of high scores: xx_**
  - Điểm trung bình: **_Mean (average) score: xx_**
  - Điểm cao nhất: **_Highest score: xx_**
  - Điểm thấp nhất: **_Lowest score: xx_**
  - Miền giá trị của điểm (cao nhất trừ thấp nhất): **_Range of scores: xx_**
  - Giá trị trung vị: **_Median score: xx_**
  - Các câu hỏi bị học sinh bỏ qua nhiều nhất: **_Question that most people skip: xx_**
  - Các câu hỏi bị học sinh sai qua nhiều nhất: **_Question that most people answer incorrectly: xx_**
#### 3. Tạo function để chạy chương trình tính điểm và xuất báo cáo thống kê
- Function này có tên là `print_Grades_Report` với biến đầu vào là tên file cần thực hiện (`class_name`)
- Ở đây ta chỉ cần gọi các function `open_File` & `create_Grade_Repor` đã được tạo ở trên
#### 4. Xuất kết quả tính điểm theo tên file được nhập bởi người dùng
Gọi function `print_Grades_Report`
  ```
  print_Grades_Report(class_name)
  ```
### IV. Tạo tệp kết quả
#### 1. Tạo function ghi tệp kết quả
- Function này có tên là `write_Student_Grade_Results` với 2 biến đầu vào là tên file được mở `class_name` và file đã được mở `file`
- Gọi function `calculate_Grades` để lấy kết quả đã được tính toán để thực hiện ghi file
- Khởi tạo danh sách chứa thông tin mã học sinh `student_id_list` và điểm số `student_grade_list`
- Sử dùng vòng lặp for để lấy mã học sinh và điểm số tương ứng, sau đó thêm vào danh sách "student_grade_list" và `student_id_list`
- Từ danh sách mã học sinh và điểm số đã được lấy ở trên, tạo 1 thư viện (dictionary) chứa thông tin này
  ```
  grade_data = {"student_id": student_id_list, "total_grade": student_grade_list}
  ```
- Sau đó chuyển đổi thư viện chứa thông tin mã học sinh và điểm số thành dạng bảng (dataframe) `pd.DataFrame()`
- Sử dụng Pandas để ghi tệp dưới định dạng .txt (`.to_csv(file_path,index=None, header=None)`). _Lưu ý: tên file lưu sẽ có định dạng `class_name`_grades.txt_
- Để thực hiện in nội dung file mới được ghi ta sử dụng code sau: `.to_csv(index=False, header=None, sep=',')`
#### 2. Tạo function chạy file kết quả đã được ghi
- Function này có tên là `write_And_Print_Grade_Result` với biến đầu vào là tên file cần thực hiện (`class_name`)
- Ở đây ta chỉ cần gọi các function `open_File` & `write_Student_Grade_Results` đã được tạo ở trên
#### 3. Thực hiện ghi file và xuất kết quả file ghi theo tên file được nhập bởi người dùng
Gọi function `write_And_Print_Grade_Result`
  ```
  write_And_Print_Grade_Result(class_name)
  ```
### C. Tương tác với Github để thực hiện đẩy hoặc tải chương trình vừa viết từ máy local sang Github và ngược lại
### I. Đẩy (Upload) chương trình vừa viết lên Github

### II. Tải (Clone) chương trình vừa viết về máy local để chạy hoặc chỉnh sửa
- Tại máy local tạo 1 thư mục để chứa tệp chương trình sẽ được tải về từ github
- Từ terminal bạn sử dụng câu lệnh sau để chỉ đến thư mục mới tạo `cd` _'tên đường dẫn thư mục vừa tạo'_ (vd: cd /users/desktop/abc)
- Tiếp đến bạn sử dụng câu lệnh sau để clone chương trình về: `git clone` _'đường dẫn được lấy từ github'_
  - Cách lấy _'đường dẫn được lấy từ github'_ 