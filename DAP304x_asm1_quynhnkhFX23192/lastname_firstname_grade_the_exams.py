
""" ---- IMPORT LIBRARY ---- """

import numpy as np
import pandas as pd
import re

""" ---- I. MỞ CÁC TỆP DỮ LIỆU BÊN NGOÀI ĐƯỢC YÊU CẦU ---- """

""" -- 1. Tạo hàm (function) thực hiện việc mở file -- """

def open_File(class_name):
    try:
        file_path = class_name+".txt"
        file = pd.read_csv(file_path, delimiter='\t', header=None)
        return file
    except FileNotFoundError:
        return None 

""" -- 2. Tạo function in kết quả mở file -- """

def print_Open_File_Result(class_name):
    # sử dụng lại hàm mở file - open_File
    file = open_File(class_name)

    # dùng if, else để kiểm tra xem file có mở thành công không và in ra kết quả tương ứng
    if file is not None:
        print(f"\nSuccessfully opened {class_name}.txt\n")
    else:
        print(f"\nFile {class_name}.txt cannot be found\n")

""" -- 3. Xuất kết quả đọc file theo tên file mà người dùng đã nhập -- """ 

class_name = input("\nEnter a file name (i.e. class1 for class1.txt):")
print_Open_File_Result(class_name)


""" ---- II. SCAN FILE VÀ PHÂN TÍCH ---- """

""" -- 1. Tạo function thực hiện kiểm tra các thông tin trong file -- """

def check_File(file):
    # tạo các biến global vì sẽ được sử dụng lại ở các function khác 
    global num_lines      
    global num_valid
    global num_invalid
    global ID_number_pattern
    global valid_list
    global invalid_list
        
    if file is not None:
        """ Khởi tạo 2 danh sách (list) gồm: 
            - valid_list: chứa các dòng hợp lệ trong file
            - invalid_list: chứa các dòng không hợp lệ trong file """
        valid_list = []
        invalid_list = []
        
        num_lines = len(file)   # đếm số lượng dòng trong file
        
        """ Xác định định dạng số ID học sinh theo yêu câu, cụ thể:
            - Bắt đầu bằng N 
            - 8 ký tự số đi sau N """
        ID_number_pattern = r'^N\d{8}'
            
        # Dùng vòng lặp for để đi qua các dòng của file và xem xét các điều kiện theo yêu cầu 
        for i in range(num_lines):
            row = file.iloc[i].reset_index(drop=True).squeeze()   # Lấy từng dòng của file (dạng dataframe) chuyển thành string 
            splited_row = row.split(',')                          # Tách các giá trị của dòng thông qua dấu ","  
            count_values_in_row = len(splited_row)                # Đếm số lượng các giá trị trong dòng đã được tách
            student_ID = splited_row[0]                           # lấy số ID của học sinh
        
            """ Tạo hàm điều kiện if, elif, else để thêm các giá trị có điều kiện vào danh sách invalid_list & valid_list.
            Cụ thể:
                - Thêm vào invalid_list khi:
                    + Số ID của học sinh trong file không đúng định dạng quy định
                    + Số lượng các giá trị trong 1 dòng khác 26
                - Thêm vào valid_list: các trường hợp còn lại """
            if re.match(ID_number_pattern, student_ID)==None:
                invalid_list.append(row)
            elif count_values_in_row != 26:
                invalid_list.append(row)
            else:
                valid_list.append(row)
            
        num_valid = len(valid_list)       # số lượng dòng hợp lệ
        num_invalid = len(invalid_list)   # số lượng dòng không hợp lệ
            
    else:
        return None 

""" -- 2. Tạo function tạo báo cáo (report) sau khi thực hiện kiểm tra file -- """

def create_Checked_File_Report(file):
    
    # sử dụng function check_File để thực hiện kiểm tra file cần làm báo cáo
    check_File(file)
        
    if file is not None:

        print("**** ANALYZING ****\n")

        # dùng vòng lặp for đi qua các dòng của dataframe và xem xét các điều kiện theo yêu cầu 
        for i in range(num_invalid):
            
            """ Lấy từng dòng của file (dataframe) chuyển thành dạng string và tách các giá trị thông qua dấu "," 
            để thực hiện đếm số lượng các giá trị trong 1 dòng """  
            splited_row = invalid_list[i].split(',')
            count_values_in_row = len(splited_row)
            student_ID = splited_row[0]     # lấy số ID của học sinh
        
            """ Tạo hàm điều kiện if, elif để in ra các dòng không hợp lệ, bao gồm các dòng có:
                - Số ID của học sinh trong file không khớp với yêu cầu
                - Số lượng các giá trị trong 1 dòng khác 26 """
            if re.match(ID_number_pattern, student_ID)==None:
                print(f"Invalid line of data: N# is invalid:\n {invalid_list[i]}\n")
            elif count_values_in_row != 26:
                print(f"Invalid line of data: does not contain exactly 26 values:\n {invalid_list[i]}\n")
        
        # In thông báo khi báo cáo phân tích không có dòng nào không hợp lệ
        if num_lines == num_valid:
            print("No errors found!")
            
        # In báo cáo gồm tổng số dòng, tổng số dòng hợp lệ và tổng số dòng không hợp lệ
        print("\n**** REPORT ****\n")
        print(f'Total lines of data: {num_lines}')
        print(f'Total valid lines of data: {num_valid}')
        print(f'Total invalid lines of data: {num_invalid}')
    else:
        return None 

""" -- 3. Tạo function chạy chương trình kiểm tra và xuất báo cáo phân tích file -- """
    
def print_Checked_File_Report(class_name):
    file = open_File(class_name)
    create_Checked_File_Report(file)

""" -- 4. Xuất báo cáo tổng hợp tính hợp lệ của dữ liệu trong file được nhập bởi người dùng -- """
    
print_Checked_File_Report(class_name)


""" ---- III. TÍNH TOÁN ĐIỂM THI ---- """

""" -- 1. Tạo function thực hiện tính điểm thi -- """

def calculate_Grades(file):
    # tạo các biến global vì sẽ được sử dụng lại ở các function khác 
    global num_student_high_scores
    global mean_student_score
    global max_student_score
    global min_student_score
    global range_of_score
    global median_score
    global max_skipped_answers_list
    global max_incorrect_answers_list
    global total_student_grades
    
    # sử dụng function check_File để thực hiện kiểm tra file cần chấm điểm
    check_File(file)
    
    if file is not None:
        # biến chứa chuỗi đại diện cho các câu trả lời
        answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    
        # thực hiện tách chuỗi câu trả lời ở trên và đếm số lượng các giá trị có trong chuỗi
        answer_key_list = answer_key.split(',')
        num_answer_key = len(answer_key_list)
    
        # khởi tạo 1 list chứa điểm của tất cả học sinh 
        total_student_grades = []
    
        # đếm số lượng valid đã được check 
        num_valid = len(valid_list)
    
        # Thực hiện 1 vòng lặp for để đi qua các câu trả lời của từng học sinh (chỉ tính cho các dữ liệu nằm trong danh sách hợp lệ)
        for i in range(num_valid):
            # tách chuỗi các câu trả lời của từng học sinh thông qua dấu ","
            student_answers = valid_list[i].split(',')

            # khởi tạo 1 list chứa điểm của từng học sinh
            student_grades = []
    
            """ Thực hiện 1 vòng lặp for để thực hiện so sánh các câu trả lời của học sinh với anwser_key và add kết quả vào list student_grades
                Note: [j+1] là do bỏ vị trí ban đầu của list là mã ID của học sinh """
            for j in range(0, num_answer_key):
                if student_answers[j + 1] == answer_key_list[j]:
                    student_grades.append(4)
                elif student_answers[j + 1] == "":
                    student_grades.append(0)
                else:
                    student_grades.append(-1)
    
            # add điểm đã được xác định của mỗi học sinh vào list chứa điểm của tất cả học sinh trong lớp
            total_student_grades.append(student_grades)
    
        # covert danh sách tổng điểm của toàn bộ học sinh trong lớp thành dataFrame và thêm cột tính tổng điểm của từng học sinh
        total_student_grades_table = pd.DataFrame(total_student_grades)
        total_student_grades_table['total_grades'] = total_student_grades_table.sum(axis=1)

        # đếm số lượng học sinh có điểm lớn hơn 80
        num_student_high_scores = len(total_student_grades_table[total_student_grades_table.total_grades > 80])
        # tính điểm trung bình
        mean_student_score = round(total_student_grades_table.total_grades.mean(),3)
        # xác định điểm cao nhất
        max_student_score = total_student_grades_table.total_grades.max()
        # xác định điểm thấp nhất
        min_student_score = total_student_grades_table.total_grades.min()
        # tính miền giá trị của điểm (cao nhất trừ thấp nhât)
        range_of_score = max_student_score - min_student_score
        # tính điểm trung vị
        median_score = round(total_student_grades_table.total_grades.median())

        # khởi tạo các list chứa số thứ tự câu hỏi (index) và số lượng học sinh tương ứng đã bỏ qua câu trả lời
        skipped_answer_index_list = []
        count_skipped_answer_list = []
        
        # khởi tạo các list chứa số thứ tự câu hỏi (index) và số lượng học sinh tương ứng đã trả lời sai
        incorrect_answer_index_list = []
        count_incorrect_answer_list = []
    
        # thực hiện vòng lặp để đi qua điểm số của tất cả học sinh đã bỏ qua câu trả lời và trả lời sai để add vào list đã tạo trên
        for i in range(num_answer_key):
            # sử dụng try, except để bỏ qua lỗi trong trường hợp không tìm thấy giá trị cần đếm theo điều kiện 
            try:
                num_skipped_answers = total_student_grades_table[i].value_counts()[0]
                num_incorrect_answers = total_student_grades_table[i].value_counts()[-1]
            except KeyError:
                pass
            else:
                skipped_answer_index_list.append(i + 1)
                count_skipped_answer_list.append(num_skipped_answers)
    
                incorrect_answer_index_list.append(i + 1)
                count_incorrect_answer_list.append(num_incorrect_answers)
    
        # tìm giá trị lớn nhất trong list các câu trả lời đã bị bỏ qua và list các câu trả lời sai:
        max_skipped_answer = max(count_skipped_answer_list)
        max_incorrect_answer = max(count_incorrect_answer_list)
    
        # xác định số lượng có trong 2 list "num_skipped_answer_list" & "incorrect_answer_index_list"
        num_in_skipped_list = len(count_skipped_answer_list)
        num_in_incorrect_list = len(count_incorrect_answer_list)
    
        # khởi tạo list chứa kết quả các câu bị bỏ qua nhiều nhất gồm combo: số thứ tự câu hỏi - số lượng học sinh bỏ qua - tỉ lệ bị bỏ qua
        max_skipped_answers_list = []
        
        # Sử dụng vòng lặp for để tìm vị trí câu trả lời có lượng học sinh bỏ qua nhiều nhất và lưu kết quả vào list "max_skipped_answers_list":
        for i in range(num_in_skipped_list):
            if count_skipped_answer_list[i] == max_skipped_answer:
                skipped_rate = round((max_skipped_answer / num_valid), 3)
                skipped_results = f'{skipped_answer_index_list[i]} - {count_skipped_answer_list[i]} - {skipped_rate}'
                max_skipped_answers_list.append(skipped_results)
    
        # khởi tạo list chứa kết quả các câu bị sai nhiều nhất gồm combo: số thứ tự câu hỏi - số lượng học sinh trả lời sai - tỉ lệ bị sai
        max_incorrect_answers_list = []
        
        # Sử dụng vòng lặp for để tìm vị trí câu trả lời có lượng học sinh sai nhiều nhất và lưu kết quả vào list "max_incorrect_answers_list":
        for i in range(num_in_incorrect_list):
            if count_incorrect_answer_list[i] == max_incorrect_answer:
                incorrect_rate = round((max_incorrect_answer / num_valid), 3)
                incorrect_results = f'{incorrect_answer_index_list[i]} - {count_incorrect_answer_list[i]} - {incorrect_rate}'
                max_incorrect_answers_list.append(incorrect_results)
        
    else:
        return None 

""" -- 2. Tạo function để tạo báo cáo thống kê -- """

def create_Grade_Report(file):

    # sử dụng function calculate_Grades để lấy kết quả đã tính toán làm báo cáo
    calculate_Grades(file)
    
    if file is not None:
        # In kết quả sau khi tính toán:
        print(f"\nTotal student of high scores: {num_student_high_scores}")
        print(f"Mean (average) score: {mean_student_score}")
        print(f"Highest score: {max_student_score}")
        print(f"Lowest score: {min_student_score}")
        print(f"Range of scores: {range_of_score}")
        print(f"Median score: {median_score}\n")
        print(f"Question that most people skip: {', '.join(max_skipped_answers_list)}\n")
        print(f"Question that most people answer incorrectly: {', '.join(max_incorrect_answers_list)}")
        
    else:
        return None 
    
""" -- 3. Tạo function để chạy chương trình tính điểm và xuất báo cáo thống kê -- """
    
def print_Grades_Report(class_name):
    file = open_File(class_name)
    create_Grade_Report(file)

""" -- 4. Xuất kết quả tính điểm theo tên file được nhập bởi người dùng -- """
print_Grades_Report(class_name)


""" ---- IV. TẠO TỆP KẾT QUẢ ---- """

""" -- 1. Tạo function ghi tệp kết quả -- """

def write_Student_Grade_Results(class_name, file):

    # sử dụng function calculate_Grades để lấy kết quả đã tính toán và thực hiện ghi file
    calculate_Grades(file)

    if file is not None:
        # tạo 1 bảng (dataframe) chứa điểm các câu trả lời của từng học sinh và thêm cột tính tổng điểm. 
        total_student_grades_table = pd.DataFrame(total_student_grades)
        total_student_grades_table['total_grades'] = total_student_grades_table.sum(axis=1)
    
        # khởi tạo 1 list chứa thông tin mã học sinh và điểm số
        student_id_list = []
        student_grade_list = []
    
        # dùng vòng lặp for để lấy mã học sinh và điểm số tương ứng và thêm vào list "student_grade_list" và "student_id_list"
        for i in range(num_valid):
            student_id = valid_list[i].split(',')[0]     # lấy mã học sinh
            student_grade = np.str_(total_student_grades_table['total_grades'].iloc[i])   # lấy tổng điểm của từng học sinh
            student_id_list.append(student_id)   # add mã học sinh lấy được vào list student_id_list
            student_grade_list.append(student_grade)   # add tổng điểm của từng học sinh lấy được vào list student_grade_list
    
        # tạo 1 thư viện (dictionary) chứa thông tin mã học sinh và điểm của từng học sinh
        grade_data = {"student_id": student_id_list, "total_grade": student_grade_list}
        
        # convert thư viện chứa thông tin mã học sinh và điểm số thành bảng (dataframe)
        student_grade_list_table = pd.DataFrame(grade_data)
        
        # thực hiện ghi file
        file_path = class_name+"_grade.txt"
        student_grade_list_table.to_csv(file_path, index=None, header=None)
    
        # In nội dung file vừa mới ghi
        print(f"\n# this is what {file_path} should look like\n")
        content = student_grade_list_table.to_csv(index=False, header=None, sep=',')
        print(content)
    else:
        return None 
    
""" -- 2. Tạo function chạy file kết quả đã được ghi -- """

def write_And_Print_Grade_Result(class_name):
    file = open_File(class_name)
    write_Student_Grade_Results(class_name, file)

""" -- 3. Thực hiện ghi file và xuất kết quả file ghi theo tên file được nhập bởi người dùng -- """

write_And_Print_Grade_Result(class_name)
