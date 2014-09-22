// Clear code and name field of member
function clear_member_field(id){
    $('#member-row-'+id+' .input-code').val('');
    $('#member-row-'+id+' .input-name').val('');
}
function check_exists_code(number, code){
    if(code.length < 6){
        $('#member-row-'+number+' .input-name').attr('placeholder', 'Name');
        $('#member-row-'+number+' .btn-view-member').addClass('hidden');
        $('#member-row-'+number+' .btn-add-member').addClass('hidden');
        return;
    }
    Dajaxice.findinggroup.check_exist_student(set_member_name, {'number':number, 'code':code});

}
function set_member_name(member){
    console.log(member.code+' - '+member.full_name);
    if(member.code==''){
        $('#member-row-'+member.number+' .input-name').attr('placeholder', 'Name');
        $('#member-row-'+member.number+' .btn-view-member').addClass('hidden');
        $('#member-row-'+member.number+' .btn-add-member').addClass('hidden');
        return;
    }
    $('#member-row-'+member.number+' .input-name').attr('placeholder', member.full_name);
    $('#member-row-'+member.number+' .btn-view-member').removeClass('hidden');
    $('#member-row-'+member.number+' .btn-add-member').removeClass('hidden');
}