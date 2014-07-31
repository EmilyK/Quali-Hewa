/*
function to render and display quelihewa stations map
*/

var kampala = new google.maps.LatLng(0.3136110,32.5811110);
var marker;
var map;

//initialize map on webpage
function initialize() {
  var mapOptions = {
    zoom: 12,
    center: kampala
  };

  map = new google.maps.Map(document.getElementById('map-canvas'),
          mapOptions);

	$.getJSON('/map-geojson/stations', function(data){
		// var latLng = new google.maps.LatLng(data)
		$.each(data, function(key, value){
			var coord = value.geometry.coordinates;
			var latLng = new google.maps.LatLng(parseFloat(coord[0]), parseFloat(coord[1]));

			var content = '<div id="content">'+
				'<h2>' + value.properties.title + '</h2>'+
				'<p>' + "<a href='"+value.properties.url +"'>Readings</a>" + '</p>'+
				'</div>'
			//create an informatin window	
			var infowindow = new google.maps.InfoWindow({
				content: content
			})
			//create a marker
			var marker = new google.maps.Marker({
				position: latLng,
				map: map,
				title: value.properties.title
			});
			//add click event listener
			google.maps.event.addListener(marker, 'click', function(){
				infowindow.open(map, marker);
			});
		});
	});

}

//add map to webpage
google.maps.event.addDomListener(window, 'load', initialize);
