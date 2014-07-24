select count(distinct term)
from frequency where 
(
docid = "10398_txt_earn" 
or
docid = "925_txt_trade"
)
and count = 1;
