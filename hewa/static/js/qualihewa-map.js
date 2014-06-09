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