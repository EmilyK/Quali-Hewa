/*for home page only*/
$(function(){
    /* this function handles options chosen by user */
    $('#selectBox').change(function(){
        var selectedBox = $('#selectBox')[0];
        var selectedValue = selectBox.options[selectBox.selectedIndex].value;
        if (selectedValue === 'monthly'){
            generateChart('/chart-data/monthly', 'Monthly Average readings from all stations');
        }else if (selectedValue === 'daily'){
            generateChart('/chart-data/daily', 'Daily Average readings from all stations');
        }else{
            generateChart('/chart-data', 'Weekly Average readings from all stations');
        }
    })
});

$(document).ready(function(){
    /* this is the default */
    generateChart('/chart-data', 'Weekly Average readings for all stations');
});