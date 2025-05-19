-- Faça uma query que apresente o tamanho médio, máximo e mínimo do nome do objeto por categoria. Considere apenas os objetos com descrição maior que 300. exiba apenasas categorias com tamanho medio de descrição do objeto maior que 100

select
  product_category_name as category,
  round(avg(product_name_lenght),2) as med_name_len,
  round(max(product_name_lenght),2) as max_name_len,
  round(min(product_name_lenght),2) as min_name_len
  
from
  tb_products

where
  product_category_name is not null
  and
  product_description_lenght >= 300

group by
  product_category_name

having
  avg(product_description_lenght) > 10
  or
  max(product_name_lenght) < 50

order by 
  max_name_len desc,
  min_name_len asc

