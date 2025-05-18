-- Mostrar estatísitcas de máximo, mínimo e média e quantidade de produtos por categoria, excluindo os sem categoria, a categoria 'artes' e a categoria 'bebes'

select 
  product_category_name,
  count(distinct product_id) as qtd_produtos_distintos,
  round(max(product_weight_g / 1000), 2) as maior_peso_kg,
  round(min(product_weight_g / 1000), 2) as menor_peso_kg,
  round(avg(product_weight_g /1000), 2) as media_peso_kg
  
from 
  tb_products 
  
where
  product_category_name is not null
  and product_category_name != 'artes'
  and product_category_name != 'bebes'

group by
  product_category_name