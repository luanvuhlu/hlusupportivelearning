$(document).ready(function(){
    $( ".datepicker" ).datepicker({ dateFormat: 'yy-mm-dd' });
})

function check_form(form_id){
    if (form_id=='member-form'){
        if($('#subject-code').val()==''){
            $('#subject-code').focus();
            alert('Subject is required !');
            return false;
        }
        if($('#subject-theory').val()==''){
            $('#subject-theory').focus();
            alert('Theory class is required !');
            return false;
        }
        if($('#subject-seminar').val()==''){
            $('#subject-seminar').focus();
            alert('Seminar class is required !');
            return false;
        }
        if($('#leader-name').val()==''){
            $('#leader-name').focus();
            alert('Full name is required !');
            return false;
        }
        if($('#leader-phone').val()==''){
            $('#leader-phone').focus();
            alert('Phone is required !');
            return false;
        }
        if($('#leader-email').val()==''){
            $('#leader-email').focus();
            alert('Email is required !');
            return false;
        }
        if($('#date-valid').val()==''){
            $('#date-valid').focus();
            alert('Date valid is required !');
            return false;
        }
        var input_codes=$('#members .input-code');
        var input_names=$('#members .input-name');
        var input_code;
        var input_name;
        var input_code2;
        var input_name2;
        for(var i=1; i<=15; i++){
            input_code=input_codes[i]
            input_name=input_names[i]
            if(input_code.val()==''){
                continue;
            }
            if(input_code.val().length < 6){
                input_code.focus();
                alert('Code invalid !');
                return false;
            }
            if(input_code.val()!='' && input_name.val() ==''){
                input_name.focus();
                alert('Name is required !');
                return false;
            }
            for(var j=2; j<=15; j++){
                input_code2=input_codes[j];
                if(i!=j && input_code.val()== input_code2.val()){
                    input_code2.prop('readonly', false);
                    input_code2.focus();
                    alert('Duplicate code');
                    return false;
                }
            }
        }
    $('#'+form_id).submit();
    }
}