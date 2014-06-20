
$(function(){
    /* this function handles options chosen by user */
    var url = '/chart-data' + window.location.pathname;
    $('#selectBox').change(function(){
        var selectedBox = $('#selectBox')[0];
        var selectedValue = selectBox.options[selectBox.selectedIndex].value;
        if (selectedValue === 'monthly'){
            generateChart(url + 'monthly', 'Monthly Average readings for a specific station');
        }else if (selectedValue === 'weekly'){
            generateChart(url + 'weekly', 'Weekly Average readings for a specific station');
        }else if (selectedValue === 'daily') {
            generateChart(url + 'daily', 'Daily Average readings for a specific station');
        }
    });
    generateChart(url + 'daily', 'Daily Average readings for a specific station');
});


