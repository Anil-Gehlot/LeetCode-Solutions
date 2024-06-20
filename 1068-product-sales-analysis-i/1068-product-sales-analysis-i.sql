select product_name, year, price from Sales left join Product on Sales.product_id = Product.product_id ; 
-- select product_name, year, price from Sales left join Product using (product_id); 