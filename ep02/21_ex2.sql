-- Quantos produtos tem mais de 5 litros?

select
  count(*),
  count(distinct product_id)

from 
  tb_products

where
  product_length_cm	* product_height_cm	* product_width_cm * 0.001> 5