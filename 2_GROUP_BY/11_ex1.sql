-- Ex1. Quantos produtos temos na categoria 'artes'?

select
  count(*) AS tot_linhas,
  count(product_id) AS tot_products_artes,
  count(distinct product_id) AS tot_products_artes_distintos,
  count(distinct product_category_name) AS qtd_categorias_distintas

from
  tb_products

where
  product_category_name = 'artes'