$(document).ready(function(){
    $.getJSON('/chart-data', function(data){
        // console.log(data['payload']);
        $('#container').highcharts({
            title: {
                text: 'Monthly Average Readings',
                x: -20 //center
            },
            subtitle: {
                text: 'Raspberry pi readings',
                x: -20
            },
            xAxis: {
                categories: ['Mon','Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
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