-- Faça uma query que mostre o tamanho médio, máximo e mínimo do nome do objeto por categoria. Considere apenas os objetos que tenham a descrição maiorque 50

select
  product_category_name,
  -- product_description_lenght
  round(min(product_name_lenght),2) as min_name_len,
  round(max(product_name_lenght),2) as max_name_len,
  round(avg(product_name_lenght),2) as med_name_len

from
  tb_products

where
  product_category_name is not null
  and
  product_description_lenght >= 300

group by
  product_category_name
