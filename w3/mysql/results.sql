use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product

-- 2. Выбрать названия всех автоматизированных складов
select name FROM store WHERE is_automated=1

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select distinct store_id from store natural join sale


-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select distinct store_id from store left join sale using (store_id) where sale_id is null

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select product.name, avg(total/quantity) from sale 
natural join product
group by product_id

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select ...

-- 8. Получить названия всех складов, с которых продавался только один продукт
select ...

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select ...

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select ...
