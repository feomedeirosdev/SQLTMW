select 
  distinct coalesce(product_category_name, 'outros') as category_fill_na 

from 
  tb_products

order by
  category_fill_na