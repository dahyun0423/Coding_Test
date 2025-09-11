-- 코드를 입력하세요
# address = 강원도
# 공장ID asc
SELECT factory_id, factory_name, address from food_factory
where address like '%강원도%'
order by factory_id asc;
