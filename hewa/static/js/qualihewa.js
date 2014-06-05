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
                categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
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
            series: [{
                name: 'Carbonmonoxide',
                data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
            }, {
                name: 'Nitrogendioxide',
                data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
            }, {
                name: 'Lpg gas',
                data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
            }]
        });
    });
    
});