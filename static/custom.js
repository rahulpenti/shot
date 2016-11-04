$('#button_submit').click(function(){

    var years = [],
        rollNo = '';
	$('input:checkbox:checked', '.checkbox-inline').each(function() {
	    years.push(this.value);
    });
    console.log(years);
    rollNo = ($('#roll_input')[0].value);
    var url = window.location.origin + '/getpaper?rollno=' + rollNo + '&years=' + years;
    var url2 = window.location.origin + '/getpaper';
    $.get(url2, { rollno: rollNo, years: years.join(',')})
        //.done(function() {
          //  alert("Success");
   //     });

	$("#hidden").show();
});
