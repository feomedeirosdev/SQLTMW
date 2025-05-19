-- Quantos produtos de "beleza_saude" com menos de 1 litro

select 
  count(*) as n_linhas,
  count(product_id) as qtd_produt_ids,
  count(distinct product_id) as qtd_distinct_product_ids,
  count(distinct product_category_name) as qtd_distinct_category_name

from 
  tb_products

where
  product_category_name = 'beleza_saude'
  and 
  ((product_length_cm * product_height_cm	* product_width_cm) * power(10, -3)) < 1