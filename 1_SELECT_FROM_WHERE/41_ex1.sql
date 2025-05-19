-- Quantos produtos temos na categoria 'artes'?

SELECT COUNT(*) AS tot_products

FROM tb_products AS t1

WHERE t1.product_category_name = 'artes'