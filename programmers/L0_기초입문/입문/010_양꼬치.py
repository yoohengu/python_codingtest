# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 01. 19. 21:56:16

def solution(n, k):
    a = n // 10
    
    total = n*12000 + k*2000 - a*2000
    
    return total