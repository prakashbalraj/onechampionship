select event_name
from
(
select
event_name,
people_count,
id-LAG(id,1,0) OVER (PARTITION BY event_name ORDER BY id) as consecutive_events
from cdna_proc_dev.events
)x
where consecutive_events=1 and people_count>=100 
group by event_name
having count(event_name)>=3;
