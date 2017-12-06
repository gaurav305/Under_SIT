--Batch Procedure
declare
   l_batch_no number;
begin
   l_batch_no := frtb_batch.create_batch(business_date_from_in => to_date('15-09-2017 00:00:00','DD-MM-YYYY HH24:MI:SS'),
                                         business_date_to_in   => to_date('19-09-2017 05:44:59','DD-MM-YYYY HH24:MI:SS'));
   dbms_output.put_line('Created batch id: '||l_batch_no);
end;
/