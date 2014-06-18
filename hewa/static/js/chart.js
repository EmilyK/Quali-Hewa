/* function to generate chart */
function generateChart(url, title, tooltip){

    $.getJSON(url, function(data){
        $('#container').highcharts({
            title: {
                text: title,
                x: -20 //center
            },
            subtitle: {
                text: 'QualiHewa Analyser Readings',
                x: -20
            },
            xAxis: {
                categories: data['dates']
            },
            yAxis: {
                title: {
                    text: 'Readings(parts per million)'
                },
                plotLines: [{
                color: '#FFFF00',
                width: 2,
                value: 30,
                label: {text: "lpg gas limit at 30pmm"}
                }, {
                color: 'red',
                width: 2,
                value: 6,
                label: {text: "carbon monoxide limit at 6pmm"} 
                }]
            },
            tooltip: {
                valueSuffix: 'ppm'
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