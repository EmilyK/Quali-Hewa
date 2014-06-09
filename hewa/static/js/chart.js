$(document).ready(function(){
    $.getJSON('/chart-data', function(data){
       
        $('#container').highcharts({
            title: {
                text: 'Weekly total Readings',
                x: -20 //center
            },
            subtitle: {
                text: 'Raspberry pi readings',
                x: -20
            },
            xAxis: {
                categories: data['dates']//['Sun', 'Sat', 'Fri', 'Thur', 'Wed', 'Tue', 'Mon']
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
});