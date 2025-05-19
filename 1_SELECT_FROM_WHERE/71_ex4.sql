-- Quantos produtos de 'beleza_saude' com menos de 1 litro

SELECT COUNT(*) AS tot_products_beleza_saude

FROM tb_products AS t1

WHERE (t1.product_category_name = 'beleza_saude')
      AND 
      (t1.product_length_cm	* t1.product_height_cm	* t1.product_width_cm * 0.001 < 1)