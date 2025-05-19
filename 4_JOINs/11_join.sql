-- Qual é a receita de cada categoria do produto?
-- e o total em vendas?
-- em unidades e em pedidos

select
  t1.order_id,
  t1.order_item_id,
  t1.product_id,
  -- t1.seller_id,
  -- t1.shipping_limit_date,
  -- t1.price,
  -- t1.freight_value,
  -- t2.product_id,
  t2.product_category_name
  -- t2.product_name_lenght,
  -- t2.product_description_lenght,
  -- t2.product_photos_qty,
  -- t2.product_weight_g,
  -- t2.product_length_cm,
  -- t2.product_height_cm,
  -- t2.product_width_cm

from
  tb_order_items as t1

left join 
  tb_products as t2 
  on 
  t1.product_id = t2.product_id