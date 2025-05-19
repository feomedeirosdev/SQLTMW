-- Crie uma coluna nova que contenha a informação de volume em m3

SELECT *,
       t1.product_length_cm	* t1.product_height_cm	* t1.product_width_cm * 0.001 AS product_volume_litros

FROM tb_products AS t1