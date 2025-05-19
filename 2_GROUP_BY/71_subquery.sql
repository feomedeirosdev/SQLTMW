
select 
  *

from (

    select
      seller_state as estado,
      count(distinct seller_id) as qtd_vendedores
      
    from
      tb_sellers

    group by
      seller_state

)

where 
  qtd_vendedores > 10