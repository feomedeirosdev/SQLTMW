-- Quantos produtos tem mais de 5 litros?

SELECT t1.product_id,
       t1.product_length_cm * t1.product_height_cm * t1.product_width_cm * 0.001 AS product_volume_litro

FROM tb_products AS t1

WHERE product_volume_litro > 5