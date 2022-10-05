
insert into {destination_table}
select date(EffectiveDate,'start of month') as period_month ,
    avg(bid),
    min(bid),
    max(bid),
    avg(ask),
    min(ask),
    max(ask)
from {source_table}
group by period_month