select * from image_list t where t.images_code like '%2012%'
for update 


select *
       --listagg(''''||id||'''',',') within group (order by null)
  from count t
 where t.id <= 3000 and t.id >2000
   and t.id not in (select to_number(l.images_code) from image_list l)
 order by id
