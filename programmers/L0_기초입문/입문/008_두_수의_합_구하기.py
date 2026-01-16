# 두 수의 합 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120802
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 01. 16. 22:39:51

def solution(num1, num2):
    if -50000<=num1<=50000 and -50000<=num2<= 50000:
        answer = num1 + num2
        return answer