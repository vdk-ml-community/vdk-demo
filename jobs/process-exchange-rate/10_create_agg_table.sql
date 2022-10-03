create table if not exists {rates_agg_table} (
    period_month text,
    avg_bid integer,
    min_bid integer,
    max_bid integer,
    avg_ask integer,
    min_ask integer,
    max_ask integer)