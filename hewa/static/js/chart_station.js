
$(function(){
    /* this function handles options chosen by user */
    var url = '/chart-data' + window.location.pathname;

    $('#selectBox').change(function(){
        var selectedBox = $('#selectBox')[0];
        var selectedValue = selectBox.options[selectBox.selectedIndex].value;
        if (selectedValue === 'monthly'){
            generateChart(url + 'monthly', '');
        }else if (selectedValue === 'weekly'){
            generateChart(url + 'weekly', '');
        }else if (selectedValue === 'daily') {
            generateChart(url + 'daily', '');
        }
    });
    generateChart(url + 'daily', '');
});


