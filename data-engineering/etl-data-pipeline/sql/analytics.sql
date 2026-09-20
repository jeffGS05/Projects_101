-- Customer order summary
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    COUNT(o.order_id) AS order_count,
    COALESCE(SUM(o.total_amount), 0) AS total_spent
FROM customers c
LEFT JOIN orders o
    ON o.customer_id = c.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_spent DESC;


-- Revenue by order status
SELECT
    status,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue
FROM orders
GROUP BY status
ORDER BY total_revenue DESC;


-- Product sales
SELECT
    product_name,
    SUM(quantity) AS total_quantity,
    SUM(quantity * unit_price) AS total_revenue
FROM order_items
GROUP BY product_name
ORDER BY total_revenue DESC;


-- Order total reconciliation
SELECT
    o.order_id,
    o.total_amount,
    SUM(oi.quantity * oi.unit_price) AS calculated_total,
    o.total_amount - SUM(oi.quantity * oi.unit_price) AS difference
FROM orders o
JOIN order_items oi
    ON oi.order_id = o.order_id
GROUP BY
    o.order_id,
    o.total_amount
ORDER BY o.order_id;
