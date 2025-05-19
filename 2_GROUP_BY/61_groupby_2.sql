
select
  seller_state as estado,
  count(distinct seller_id) as qtd_vendedores
  
from
  tb_sellers

where
  seller_state in ('SP', 'RJ', 'PR')

group by
  seller_state
