-- 코드를 입력하세요
# 12세 이하 여아의 환자 이름, 환자번호, 성별코드, 나이, 전화번호
# 전화번호가 없으면 none으로 
# 나이 기준 내림차순
# 나이가 같아? 그럼 환자이름 기준
SELECT PT_NAME,PT_NO, GEND_CD, AGE, IFNULL(TLNO,'NONE') AS TLNO
FROM PATIENT
where GEND_CD = 'w' and AGE <=12 
ORDER BY AGE DESC, PT_NAME ASC