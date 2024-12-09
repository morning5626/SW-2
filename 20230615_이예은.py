#!/usr/bin/env python
# coding: utf-8

# In[25]:


import random
import string

# 학생 이름 생성 함수 (알파벳 대문자 두 글자)
def generate_name():
    return ''.join(random.choices(string.ascii_uppercase, k=2))

# 학생 정보 생성
students = []
for _ in range(30):
    name = generate_name()  # 이름 생성
    age = random.randint(18, 22)  # 나이 생성 (18 ~ 22 사이)
    grade = random.randint(0, 100)  # 성적 생성 (0 ~ 100 사이)
    student_info = {"이름": name, "나이": age, "성적": grade}  # 딕셔너리 형태로 저장
    students.append(student_info)

# 선택 정렬 (Selection Sort)
def selection_sort(students, key, reverse=False):
    # 주어진 키를 기준으로 학생 리스트를 선택 정렬
    for i in range(len(students)):
        min_max_index = i
        for j in range(i + 1, len(students)):
            # 오름차순, 내림차순에 맞는 조건으로 최소, 최대값 찾기
            if (students[j][key] < students[min_max_index][key] and not reverse) or (students[j][key] > students[min_max_index][key] and reverse):
                min_max_index = j
        # 선택된 최소, 최대값을 i번째 위치로 교환
        students[i], students[min_max_index] = students[min_max_index], students[i]
    return students

# 삽입 정렬 (Insertion Sort)
def insertion_sort(students, key, reverse=False):
    # 삽입은 앞에서부터 순차적으로 정렬된 부분에 하나씩 삽입
    for i in range(1, len(students)):
        current = students[i]
        j = i - 1
        # 오름차순, 내림차순에 맞게 현재 값을 삽입할 위치 찾기기
        while j >= 0 and ((students[j][key] > current[key] and not reverse) or (students[j][key] < current[key] and reverse)):
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = current
    return students

# 퀵 정렬 (Quick Sort)
def quick_sort(students, key, reverse=False):
    # 재귀적으로 분할하여 정렬
    if len(students) <= 1:
        return students
    pivot = students[len(students) // 2]
    # 피벗을 기준으로 분할
    left = [student for student in students if (student[key] < pivot[key] and not reverse) or (student[key] > pivot[key] and reverse)]
    middle = [student for student in students if student[key] == pivot[key]]
    right = [student for student in students if (student[key] > pivot[key] and not reverse) or (student[key] < pivot[key] and reverse)]
    # 왼쪽, 중간, 오른쪽을 재귀적 정렬
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)

# 계수 정렬 (Counting Sort)
def counting_sort(students, key, reverse=False):
    # 성적의 최대값을 구하고, 성적의 범위에 맞춰 카운팅 배열 생성
    max_grade = max(students, key=lambda x: x[key])[key]
    count = [0] * (max_grade + 1)
    
    # 각 학생의 성적에 해당하는 인덱스를 증가시킴
    for student in students:
        count[student[key]] += 1
    
    output = []
    # 성적 순으로 학생들을 출력 배열에 추가
    for i in range(len(count)):
        while count[i] > 0:
            # 성적에 해당하는 학생 정보를 추가
            student = next(student for student in students if student[key] == i)
            output.append(student)
            count[i] -= 1
    
    # 성적을 기준으로 학생을 정렬한 후 결과 리스트를 반대로 할지 말지를 결정
    if reverse:
        output.reverse()
    
    return output


# 기수 정렬 (Radix Sort)
def radix_sort(students, key, reverse=False):
    # 성적에 최대 자리수를 기준으로 기수 정렬 수행
    max_grade = max(students, key=lambda x: x[key])[key]
    exp = 1  # 1의 자리부터 시작
    while max_grade // exp > 0:
        students = counting_sort_by_digit(students, key, exp, reverse)
        exp *= 10  # 자릿수 증가
    return students

# 기수정렬에서 각 자릿수를 기준으로 계수 정렬을 수행하는 함수
def counting_sort_by_digit(students, key, exp, reverse):
    output = [0] * len(students)
    count = [0] * 10  # 0부터 9까지 숫자에 대한 카운팅
    for student in students:
        index = student[key] // exp % 10  # 해당 자릿수 추출
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = len(students) - 1
    while i >= 0:
        index = students[i][key] // exp % 10  # 해당 자릿수 추출
        output[count[index] - 1] = students[i]
        count[index] -= 1
        i -= 1
    # 내림차순일 경우 결과를 반대로 반환
    if reverse:
        return output[::-1]
    return output

# 학생 정보 출력
def print_students(students):
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")
        
# 사용자 인터페이스
def main():
    print("생성된 학생 정보:")
    print_students(students)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")

        try:
            choice = int(input("원하는 작업을 선택하세요 (1, 2, 3, 4): "))
            if choice == 4:
                print("프로그램을 종료합니다.")
                break
            elif choice in [1, 2, 3]:
                key = ["이름", "나이", "성적"][choice - 1]
            else:
                print("잘못된 선택입니다. 1~4 사이의 값을 입력하세요.")
                continue
        except ValueError:
            print("잘못된 입력입니다. 숫자 1~4 사이의 값을 입력하세요.")
            continue

        while True:
            print("\n정렬 방식을 선택하세요:")
            print("1. 오름차순")
            print("2. 내림차순")
            try:
                order = int(input("원하는 정렬 방식을 선택하세요 (1, 2): "))
                if order == 1:
                    reverse = False
                    break
                elif order == 2:
                    reverse = True
                    break
                else:
                    print("잘못된 선택입니다. 1 또는 2를 입력하세요.")
            except ValueError:
                print("잘못된 입력입니다. 1 또는 2를 입력하세요.")

        while True:
            print("\n정렬 알고리즘을 선택하세요:")
            print("1. 선택 정렬")
            print("2. 삽입 정렬")
            print("3. 퀵 정렬")
            print("4. 기수 정렬 (성적 기준)")
            print("5. 계수 정렬 (성적 기준)")
            try:
                algorithm_choice = int(input("원하는 정렬 알고리즘을 선택하세요 (1, 2, 3, 4, 5): "))
                if algorithm_choice == 1:
                    sorted_students = selection_sort(students.copy(), key, reverse)
                    break
                elif algorithm_choice == 2:
                    sorted_students = insertion_sort(students.copy(), key, reverse)
                    break
                elif algorithm_choice == 3:
                    sorted_students = quick_sort(students.copy(), key, reverse)
                    break
                elif algorithm_choice == 4 and key == "성적":
                    sorted_students = radix_sort(students.copy(), key, reverse)
                    break
                elif algorithm_choice == 5 and key == "성적":
                    sorted_students = counting_sort(students.copy(), key, reverse)
                    break
                elif algorithm_choice == 4 or algorithm_choice == 5:
                    print("기수 정렬과 계수 정렬은 성적 기준으로만 사용할 수 있습니다.")
                else:
                    print("잘못된 선택입니다. 1~5 사이의 값을 입력하세요.")
            except ValueError:
                print("잘못된 입력입니다. 숫자 1~5 사이의 값을 입력하세요.")

        # 정렬된 결과 출력
        print("\n정렬된 결과:")
        print_students(sorted_students)

# 프로그램 시작
if __name__ == "__main__":
    main()


# In[ ]:




