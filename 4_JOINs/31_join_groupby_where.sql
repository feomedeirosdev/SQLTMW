-- Considerando as vendas de 2017 e pedidos entregues
-- Qual é a receita de cada categoria do produto?
-- e o total em vendas?
-- em unidades e em pedidos

select
  case when t2.product_category_name is null then 'outros' else t2.product_category_name end "Categoria do produto",
  sum(t1.price) as "Receita",
  count(t2.product_id) as "Total de itens vendidos",
  count(distinct t1.order_id) as "Total de pedidos",
  round(cast(count(t2.product_id) as float)/ count(distinct t1.order_id), 2) as "Média por pedido"


from
  tb_order_items as t1

left join 
  tb_products as t2 on t1.product_id = t2.product_id

left join
  tb_orders as t3 on t1.order_id = t3.order_id

where
  t3.order_status = 'delivered' 
  and
  cast(strftime('%Y', t3.order_approved_at) as int) = 2017

group by
  t2.product_category_name

order by
  round(cast(count(t2.product_id) as float) / count(distinct t1.order_id), 2) desc

limit
  10