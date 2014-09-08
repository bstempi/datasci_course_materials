select sum(count)
from frequency
where
term = "washington" or
term = "taxes" or
term = "treasury"
group by docid
order by sum(count) desc
 limit 1;
