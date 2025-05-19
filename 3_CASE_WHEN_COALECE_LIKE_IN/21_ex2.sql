-- Faça uma query que apresente o tamanho médio, máximo e mínimo do nome do objeto por categoria

select
  product_category_name,
  round(min(product_name_lenght),2) as name_lenght_min,
  round(max(product_name_lenght),2) as name_lenght_max,
  round(avg(product_name_lenght),2) as name_lenght_med

from
  tb_products

where
  product_category_name is not null

group by
  product_category_name
