# Create table

create schema dip_de_usach;

create table dip_de_usach.movies(
      id0          	 int,
  ID                   int,
  Title               varchar(200),
  Year                 int,
  Age                 varchar(20),
  IMDb               float,
  Rotten_Tomatoes     varchar(200),
  Netflix              int,
  Hulu                 int,
  Prime_Video          int,
  Disney              int,
  Type                 int,
  Directors           varchar(200),
  Genres              varchar(200),
  Country             varchar(200),
  Language            varchar(200),
  Runtime            int
);



# Load data from s3

copy dip_de_usach.movies
from 's3://redshift-data-de-usach/MoviesOnStreamingPlatforms_20200101.csv'
access_key_id 'your_access_key_id'
secret_access_key 'your_secret_access_key'
csv
IGNOREHEADER 1 
delimiter ','
TRUNCATECOLUMNS;
