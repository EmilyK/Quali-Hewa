var kampala = new google.maps.LatLng(0.3136110,32.5811110);
var marker;
var map;

function initialize() {
  var mapOptions = {
    zoom: 7,
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
			var infowindow = new google.maps.InfoWindow({
				content: content
			})
			//create a marker
			var marker = new google.maps.Marker({
				position: latLng,
				map: map,
				title: value.properties.title
			});
			google.maps.event.addListener(marker, 'click', function(){
				infowindow.open(map, marker);
			});
		});
	});

	var infowindow = new google.maps.InfoWindow({
		content: 'Welcome to QualiHewa'
	})
	marker = new google.maps.Marker({
		position: kampala,
		map: map,
		title: 'Kampala'
	});
	google.maps.event.addListener(marker, 'click', function(){
		infowindow.open(map, marker);
	});


}

google.maps.event.addDomListener(window, 'load', initialize);
