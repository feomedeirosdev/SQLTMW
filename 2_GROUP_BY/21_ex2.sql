-- Quantos produtos tem mais de 5 litros?

select
  count(*) as n_lines,
  count(distinct product_id) as n_distinct_products

from 
  tb_products

where
  product_length_cm	* product_height_cm	* product_width_cm * 0.001 > 5