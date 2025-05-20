-- Qual o peso médio dos produtos vendidos por sellers de cada estado? Considere apenas o ano de 2017 e produtos entregues nessa análise.

select
  t1.seller_state as estado,
  round(avg(t4.product_weight_g), 2) as peso_medio

from
  tb_sellers as t1

left join 
  tb_order_items as t2 on t2.seller_id = t1.seller_id

left join
  tb_orders as t3 on t3.order_id = t2.order_id

left join 
  tb_products as t4 on t4.product_id = t2.product_id

where
  order_status = 'delivered'
  and
  strftime('%Y', order_approved_at) = '2017'

group by 
  t1.seller_state

order by
  round(avg(t4.product_weight_g), 2) desc

limit 10

