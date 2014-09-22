$(document).ready(function(){
    $( ".datepicker" ).datepicker();
})
// Clear code and name field of member
function clear_member_field(number){
    var input_name=$('#member-row-'+number+' .input-name');
    var input_code=$('#member-row-'+number+' .input-code');
    input_name.val(input_name.attr('placeholder', 'Name'));
    input_name.prop('readonly', false);
    input_name.val('');
    input_code.prop('readonly', false);
    input_code.val('');
    $('#member-row-'+number+' .btn-view-member').addClass('hidden');
    $('#member-row-'+number+' .btn-add-member').addClass('hidden');
    $('#member-row-'+number+' .is-member').val('-1');
}
function check_exists_code(number, code){
    if(code.length < 6){
        $('#member-row-'+number+' .input-name').attr('placeholder', 'Name');
        $('#member-row-'+number+' .btn-view-member').addClass('hidden');
        $('#member-row-'+number+' .btn-add-member').addClass('hidden');
        $('#member-row-'+number+' .is-member').val('-1');
        return;
    }
    Dajaxice.findinggroup.check_exist_student(set_member_name, {'number':number, 'code':code});

}
function set_member_name(member){
    if(member.code==''){
        $('#member-row-'+member.number+' .input-name').attr('placeholder', 'Name');
        $('#member-row-'+member.number+' .btn-view-member').addClass('hidden');
        $('#member-row-'+member.number+' .btn-add-member').addClass('hidden');
        $('#member-row-'+member.number+' .is-member').val('0');
        console.log('Cannot find student');
        return;
    }
    $('#member-row-'+member.number+' .input-name').attr('placeholder', member.full_name);
    $('#member-row-'+member.number+' .btn-view-member').removeClass('hidden');
    $('#member-row-'+member.number+' .btn-add-member').removeClass('hidden');
    $('#member-row-'+member.number+' .is-member').val('0');
    console.log(member.code+' - '+member.full_name);
}
function view_member_field(number){
    var code=$('#member-row-'+number+' .input-code').val();
    window.open('/student/'+code+'/info/', '_blank');
}
function add_or_remove__member_field(number){
    var input_name=$('#member-row-'+number+' .input-name');
    var input_code=$('#member-row-'+number+' .input-code');
    input_name.val(input_name.attr('placeholder'));
    input_name.prop('readonly', true);
    input_code.prop('readonly', true);
    $('#member-row-'+number+' .is-member').val('1');
}
function clear_group_field(){
    for(var i=1; i<=15; i++){
        clear_member_field(i);
    }
}
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
        for(var i=1; i<=15; i++){
            var input_code=$('#member-row-'+i+' .input-code');
            var input_name=$('#member-row-'+i+' .input-name');
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
                var input_code2=$('#member-row-'+j+' .input-code');
                if(i!=j && input_code.val()==input_code2.val()){
                    input_code2.prop('readonly', false);
                    $('#member-row-'+j+' .input-name').prop('readonly', false);
                    input_code2.focus();
                    alert('Duplicate code');
                    return false;
                }
            }
        }
    $('#'+form_id).submit();
    }
}