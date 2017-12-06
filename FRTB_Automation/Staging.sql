-- FRTB_OWNER

select * from frtb_contributors;
select * from frtb_steps order by step_no;

select * from fs_file_info;

select * from dba_directories where directory_name = 'FRTB_WORK_DIR';

select * from frtb_batches;


select * from audit_log where session_user='FRTB_OWNER' order by audit_log_key desc;

-- FRTB Batches
select * from frtb_batch_files order by batch_id desc;

delete frtb_batch_files where file_id = 61;
commit;


select * from frtb_batch_steps order by batch_id, step_no ;

select * from frtb_batches where batch_id =20 ;


-- Deleting from tables
delete frtb_batch_steps where batch_id <= 17;
delete frtb_batch_files where batch_id <= 20;
delete frtb_batch_ac_contributors where batch_id <= 15;
delete frtb_batches where batch_id <= 15;

-- Look at log entres (latest at top) ...
select * from frtb_logs_vw;

select * from frtb_stage where batch_id =5;
select * from frtb_normalised where batch_id=5;

Select count(*) as Cross_Currency_Count from frtb_normalised where Instrument_type='crossCurrency' and Batch_id=3;


declare
   l_batch_no number;
begin
   l_batch_no := frtb_batch.create_batch(business_date_from_in => ('01-MAY-2015'),business_date_to_in => ('31-DEC-2015'));
   dbms_output.put_line('Created batch id: '||l_batch_no);
end;
/

select * from swmis_owner.clearing_fx_rates order by exchange_date desc;

insert into swmis_owner.clearing_fx_rates
select currency_code, base_currency_code, to_date('31-DEC-2015','DD-MON-YYYY'), exchange_rate
from swmis_owner.clearing_fx_rates
where exchange_date = to_date('31-JUL-2015','DD-MON-YYYY');

-- e.g Run a single step ...
begin
   frtb_batch.process_batch(batch_id_in => 8,single_step_in => 'LOAD');
end;
/

-- e.g Run from a step onwards ...
begin
   frtb_batch.process_batch(batch_id_in => 1, restart_step_in => 'VALIDATE');
end;
/

-- Clear down (clearing STAGE will mean you have run LOAD again)
truncate table frtb_stage;
-- Clear down (clearing NORMALISED will mean you have run from ANONYMIZE again)
truncate table frtb_normalised;
-- Clear all logging
truncate table frtb_logs;

select * from frtb_batch_options where name = 'MATCHING_SCOPE';

declare
t utl_file.file_type;
begin
   t:=utl_file.fopen('FRTB_WORK_DIR','FRTB_MWIRE_IR_0000000033_20170113112225804_20161001_20161130-PFN.csv','r');
      utl_file.fclose(t);
end;
/

select * from frtb_owner.fs_file_register order by file_id desc;

delete frtb_owner.fs_file_register where file_id =1;

select * from frtb_owner.my_files;


SELECT SYS_CONTEXT ('USERENV', 'SERVER_HOST') FROM DUAL;
------------------------------------------------------------
------------------------------------------------------------
Select * from FS_FILE_REGISTER ;

-- To change the FRTB directory(to upload the normalized file)
create or replace directory frtb_work_dir as '/export/home/gaurav.saini/frtb';

-- To change the FRTB directory(Extract)
create or replace directory frtb_work_dir as '/export/app/mis_reports_tst/tmp';

-- To change the main directory to the new Share Mount(on ms00285)
create or replace directory FRTB_WORK_DIR as '/export/app/frtb/testing';


-- To change for matching
update frtb_batch_options  set value = 'INT' where name = 'MATCHING_SCOPE';
commit;


-- To Transfer to SFTP Staging Server
-- The Job runs every 5 mins to transfer
select * from staging_owner.stg_file_register_stat_vw order by 5 desc;

select * from dba_scheduler_jobs where owner = 'STAGING_OWNER';