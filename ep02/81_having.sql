
select
  seller_state as estado,
  count(distinct seller_id) as qtd_vendedores
  
from
  tb_sellers

-- filtro pré agrupamento (agg)
where
  seller_state in ('AC', 'AM', 'RJ', 'SP', 'PR', 'ES')

-- agrupamento
group by
  seller_state

-- filtro pós agrupamento
having
  count(distinct seller_id) > 10

