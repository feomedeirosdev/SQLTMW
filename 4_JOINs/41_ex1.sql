-- Qual é o valor total de receita gerada por clientes de cada estado? Considere a base completa com apenas pedidos entregues

select 
  customer_state as estado,
  (sum(t3.price) / count(distinct t1.customer_id)) as receita_cliente_estado

from tb_customers as t1

left join tb_orders as t2 on t2.customer_id = t1.customer_id

left join tb_order_items as t3 on t3.order_id = t2.order_id

where 
  t2.order_status = 'delivered'

group by
  customer_state

order by
  sum(t3.price) desc

limit 10

