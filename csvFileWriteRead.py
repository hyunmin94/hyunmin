import pandas as pd

names = ['학생', '국어', '수학', '영어', '체육']

dic_data = {'학생': ['A', 'B', 'C', 'D'],
            '국어': [80, 70, 60, 80],
            '수학': [90, 94, 53, 90],
            '영어': [70, 40, 80, 90],
            '체육': [100, 50, 70, 90]}

df = pd.DataFrame(dic_data, columns=names)

# CSV 파일 생성
df.to_csv('C:/myPyCode/data/student_exam_result.csv', index=False, encoding='cp949')

# CSV 파일 읽기
exam_df = pd.read_csv('C:/myPyCode/data/student_exam_result.csv', sep=',', index_col ='학생', encoding='cp949')

print(exam_df)