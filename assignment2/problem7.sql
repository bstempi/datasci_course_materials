select 
sum(multiple)
from (
select a.row_num as a_row_num,
a.col_num as a_col_num,
b.row_num as b_row_num,
b.col_num as b_col_num,
a.value * b.value as multiple
from a join b on a.col_num = b.row_num
) c
where a_row_num = 2 and b_col_num = 3;
