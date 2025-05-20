-- Objetivo:
-- Qual é o produto mais caro que o seller já vendeu?

with tb_seller_product as (

  select
    seller_id,
    product_id,
    count(*) as qtd_product,
    sum(price) as receita
  from tb_orders as t1
  left join
    tb_order_items as t2 
    on t2.order_id = t1.order_id
  where order_status = 'delivered'
  group by
    seller_id,
    product_id
  order by
    seller_id

), tb_seller_sort as (

  select
    t1.*,
    row_number() over (
      partition by seller_id 
      order by
        qtd_product desc,
        receita desc
      ) as order_qtd
  from tb_seller_product as t1

)

select
  seller_id,
  product_id,
  qtd_product
from tb_seller_sort
where order_qtd <= 5
limit 10