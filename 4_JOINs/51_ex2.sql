-- Qual o valor total de receita gerada por sellers de cada estado? Considere a base completa com apenas pedidos entregues

select 
  t1.seller_state as estado,
  sum(t2.price) AS receita_R$

from tb_sellers as t1

left join tb_order_items as t2 on t2.seller_id = t1.seller_id

left join tb_orders as t3 on t3.order_id = t2.order_id

where 
  t3.order_status = 'delivered'

group by
  seller_state

order by
  sum(t2.price) desc

limit 10