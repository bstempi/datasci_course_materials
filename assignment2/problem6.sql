select count(*)
from 
(
select distinct docid
from frequency
where term = "transactions"
) a
join
(
select distinct docid
from frequency
where term = "world"
) b
on a.docid = b.docid;
