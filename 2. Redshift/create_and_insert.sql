drop table dailyreport;

create table dailyreport
(
  mintotalprice int,
  maxtotalprice int,
  daydate TIMESTAMP
);

insert into dailyreport(
	select max(totalprice), min(totalprice), getdate()
	from listing
)  
