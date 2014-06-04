var map = L.mapbox.map('map', 'ekar45.ib0g1o5d').setView([0.413199, 32.6892796], 7);


var myLayer = L.mapbox.featureLayer().addTo(map);

var geojson = {
    type: 'FeatureCollection',
    features: [{
        type: 'Feature',
        properties: {
            title: 'Fort Portal',
            'marker-color': '#f86767',
            'marker-size': 'large',
            'marker-symbol': 'star',
            url: 'http://en.wikipedia.org/wiki/fortportal'
        },
        geometry: {
            type: 'Point',
            coordinates: [.66, 30.275]
         }},
        {
        type: 'Feature',
        properties: {
            title: 'Kampala',
            'marker-color': '#7ec9b1',
            'marker-size': 'large',
            'marker-symbol': 'star',
            url: 'http://en.wikipedia.org/wiki/Kampala'
        },
        geometry: {
            type: 'Point',
            coordinates: [0.413199, 32.6892796]
        }
    }]
};

L.marker([0.413199, 32.6892796], {
    icon: L.mapbox.marker.icon({
        'marker-size': 'large',
        'marker-symbol': 'bus',
        'marker-color': '#fa0'
    })
}).addTo(map);


L.marker([.66, 30.275], {
    icon: L.mapbox.marker.icon({
        'marker-size': 'large',
        'marker-symbol': 'bus',
        'marker-color': '#fa0'
    })
}).addTo(map);


/* fetch geojson from django app
*/
// $.getJSON("{% url 'data' %}")
// myLayer.setGeoJSON(geojson)
// myLayer.on('mouseover', function(e) {
//     e.layer.openPopup();
// });
// myLayer.on('mouseout', function(e) {
//     e.layer.closePopup();
// });


$(document).ready(function(){
    
    $(function () {
        var seriesContainer = [];

        $.getJSON('api/v1/stations/1/',(function(data){
                var analyserUrl = data.analyser;
                $.getJSON(analyserUrl, function(data){
                    // use `data` that is returned
                    var allReadings = data.readings;
                    var dataSet = [];
                    $.each(allReadings, function(i, value){
                        dataSet.push(value);
                    })
                    console.log(dataSet);
                });
            }));
    });
});
                // $.ajax({
                //     url: analyserUrl,
                //     type: 'GET',
                //     accepts: 'application/json',
                //     dataType: 'json'
                // }).done(function(data){
                     
                //     data.readings is an array with links to the Analyser's readings Resources
                    
                //     var allReadings = data.readings;
                //     for (var i=0; i<allReadings.size; i++){

                //     }
                //     // console.log(data.readings);//
                // });
//                 seriesContainer.push({name: 'Carbonmonoxide', data: [parseFloat(data.carbonmonoxide_sensor_reading), 
//                     10, 
//                     34, 
//                     56,
//                     23,
//                     12,
//                     6]});
//                 seriesContainer.push({name: 'Nitrogendioxide', data: [parseFloat(data.nitrogendioxide_sensor_reading), 
//                     2, 
//                     15, 
//                     6,
//                     13,
//                     12,
//                     5]});
//                 seriesContainer.push({name: 'LPG', data: [parseFloat(data.lpg_gas_sensor_reading), 
//                     1.0, 9.5, 14.5, 9.2, 5.5, 15.2]});


//                 $('#container').highcharts({
//                     title: {
//                         text: 'Weekly readings in Ntinda',
//                         x: -20 //center
//                     },
//                     subtitle: {
//                         text: 'Source: Analyser in Ntinda',
//                         x: -20
//                     },
//                     xAxis: {
//                         categories: ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat',
//                             'Sun']
//                     },
//                     yAxis: {
//                         title: {
//                             text: 'Readings'
//                         },
//                         plotLines: [{
//                             value: 0,
//                             width: 1,
//                             color: '#808080'
//                         }]
//                     },
//                     tooltip: {
//                         valueSuffix: 'mm'
//                     },
//                     legend: {
//                         layout: 'vertical',
//                         align: 'right',
//                         verticalAlign: 'middle',
//                         borderWidth: 0
//                     },
//                     series: seriesContainer
//                     //  [{
//                     //     name: 'Carbonmonoxide',
//                     //     data: [7.0, 6.9, 9.5, 14.5, 9.2, 5.5, 15.2]
//                     // }, {
//                     //     name: 'Nitrogenmonoxide',
//                     //     data: [-0.2, 0.8, 5.7, 11.3, 7.0, 12.0, 0.8]
//                     // }, {
//                     //     name: 'LPG gas',
//                     //     data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6]
                    
//                     // }]
//                 });

//             //method for creating the chart

//     });
    


// });