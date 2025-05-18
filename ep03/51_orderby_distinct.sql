-- Liste as categorias por ordem alfabética

select
  distinct product_category_name

from
  tb_products
  
where
  product_category_name is not null

order by
  product_category_name asc

limit
  100