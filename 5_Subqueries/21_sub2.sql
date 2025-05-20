-- receita por estado, por produto da categoria mais vendida

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

left join (
    select t2.product_category_name as category, 
           1 as flag_category
    from tb_order_items as t1
    left join tb_products as t2 on t2.product_id = t1.product_id
    group by t2.product_category_name
    order by count(*) desc
  ) as t4 on t3.product_category_name = t4.product_category_name

-- where t4.flag_category = 1

group by
  t2.seller_state,
  t1.product_id;

