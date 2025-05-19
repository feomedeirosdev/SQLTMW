-- Quai os selleres quenão venderam em dez/2017
-- Considere apenas as vendas válidas

select
  t2.seller_id,
  t3.seller_state
  -- max(case when 
  --   strftime('%Y-%m', t1.order_approved_at) = '2017-12' then 1 else 0 
  -- end) as flag_venda_2017_12

from tb_orders as t1

left join 
  tb_order_items as t2 on t1.order_id = t2.order_id

left join
  tb_sellers as t3 on t2.seller_id = t3.seller_id 

where
  t1.order_approved_at < '2018-01-01'
  and
  t1.order_status = 'delivered'

group by t2.seller_id, t3.seller_state 

having max(case when 
    strftime('%Y-%m', t1.order_approved_at) = '2017-12' then 1 else 0 
  end) = 0
