/* function to generate chart */
function generateChart(url, title){

    $.getJSON(url, function(data){
        $('#container').highcharts({
            title: {
                text: title,
                x: -20 //center
            },
            subtitle: {
                text: 'Raspberry pi readings',
                x: -20
            },
            xAxis: {
                categories: data['dates']
            },
            yAxis: {
                title: {
                    text: 'Readings'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: 'units'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: data['payload']
        });
    });

}




$(function(){
    /* this function handles options chosen by user */
    $('#selectBox').change(function(){
        var selectedBox = $('#selectBox')[0];
        var selectedValue = selectBox.options[selectBox.selectedIndex].value;
        if (selectedValue === 'monthly'){
            generateChart('/chart-data/monthly', 'Monthly Total readings');
        }else{
            generateChart('/chart-data', 'Weekly Total readings');
        }
    })
});


$(document).ready(function(){
    /* this is the default */
    generateChart('/chart-data', 'Weekly Total readings');
});