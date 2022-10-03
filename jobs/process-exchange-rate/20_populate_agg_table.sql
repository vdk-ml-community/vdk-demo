
insert into {rates_agg_table}
select date(EffectiveDate,'start of month') as period_month ,
        avg(bid),
        min(bid),
        max(bid),
        avg(ask),
        min(ask),
        max(ask)
from {exchange_rates_series_table}
group by period_month