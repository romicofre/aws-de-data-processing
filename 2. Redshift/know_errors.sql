# get user id 
select user, CURRENT_USER_ID;

# get last error
select * from stl_load_errors
where starttime = (select MAX(starttime) from stl_load_errors);
