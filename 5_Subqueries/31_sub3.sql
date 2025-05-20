-- receita por estado, por produto da categoria mais vendida

with tb_best_category as(
    select t2.product_category_name
    from tb_order_items as t1
    left join tb_products as t2 on t2.product_id = t1.product_id
    group by t2.product_category_name
    order by count(*) desc
    limit 4
),

tb_estate_product as (
  select 
    t2.seller_state as estado,
    t1.product_id as produto,
    sum(t1.price) as receita,
    t3.product_category_name
  from
    tb_order_items as t1
  left join
    tb_sellers as t2 on t2.seller_id = t1.seller_id
  left join
    tb_products as t3 on t3.product_id = t1.product_id
  inner join
    tb_best_category as t4 on t3.product_category_name = t4.product_category_name
  group by
    t2.seller_state,
    t1.product_id,
    t3.product_category_name
)

select
  *

from
  tb_estate_product as t1 

inner join 
  tb_best_category as t2 on t1.product_category_name = t2.product_category_name