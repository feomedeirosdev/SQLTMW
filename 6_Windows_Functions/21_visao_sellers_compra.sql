-- Tempo médio entre vendas dos sellers
-- Apenas pedidos entregues
-- Liste os 10 melhores e os 10 piores

WITH tb_seller_order AS (
  SELECT 
    t1.order_id,
    DATE(t1.order_approved_at) AS data_venda,
    t2.seller_id
  FROM tb_orders AS t1
  LEFT JOIN tb_order_items AS t2
    ON t1.order_id = t2.order_id
  WHERE t1.order_status = 'delivered'

), tb_seller_order_sort AS (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY seller_id, DATE(order_approved_at)
    ) AS date_seller_order
  FROM (
    SELECT 
      t1.order_id,
      t2.seller_id,
      DATE(t1.order_approved_at) AS data_venda,
      t1.order_approved_at
    FROM tb_orders AS t1
    LEFT JOIN tb_order_items AS t2
      ON t1.order_id = t2.order_id
    WHERE t1.order_status = 'delivered'
  )
), tb_seller_lag_data AS (
  SELECT
    order_id,
    seller_id,
    data_venda,
    LAG(data_venda) OVER (
      PARTITION BY seller_id
      ORDER BY data_venda
    ) AS lag_data_venda
  FROM tb_seller_order_sort
  WHERE date_seller_order = 1

), tb_tempo_sellers AS (

  SELECT
    *,
    JULIANDAY(data_venda) - JULIANDAY(lag_data_venda) AS avg_diff_dias
  FROM tb_seller_lag_data
  WHERE lag_data_venda IS NOT NULL

)

SELECT
    seller_id,
    ROUND(AVG(avg_diff_dias), 2) AS tempo_medio_dias
FROM tb_tempo_sellers
GROUP BY seller_id
ORDER BY ROUND(AVG(avg_diff_dias), 2) 
LIMIT 10