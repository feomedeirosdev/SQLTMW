-- crie uma coluna nova que contenha a informação de volume em m3 e reaorganize as colunas de forma diferente

select 
  product_id,
  product_category_name,
  ((product_length_cm * product_height_cm	* product_width_cm) / power(10, 6)) as product_volume_m3,
  product_name_lenght,
  product_description_lenght,
  product_photos_qty,
  product_weight_g,
  product_length_cm,
  product_height_cm,
  product_width_cm

from 
  tb_products

limit
 10