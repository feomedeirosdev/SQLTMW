-- Faça um aquery que apresenta o tamanho médio, máximo e mínimo da descrição do objeto por categoria

select
  product_category_name,
  round(min(product_description_lenght), 2) as description_lenght_min,
  round(max(product_description_lenght), 2) as description_lenght_max,
  round(avg(product_description_lenght), 2) as description_lenght_med
  
from
  tb_products

where
  product_category_name is not null

group by
  product_category_name
