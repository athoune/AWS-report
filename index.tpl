<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>aws report</title>
		<link rel="stylesheet" href="style.css" type="text/css" media="screen" charset="utf-8">
		<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js"></script> 
		<script src="js/jquery.flot.js" type="text/javascript" charset="utf-8"></script>
		<script src="js/jquery.flot.stack.js" type="text/javascript" charset="utf-8"></script>
		<script type="text/javascript" charset="utf-8">
		$(function() {
			var data = %(data)s;
			var options = {
				legend: {
					position: 'nw'
				},
				series: {
					lines: {
						show: true
					}
				},
				xaxis: {
					mode: "time",
					timeformat: "%%y-%%m-%%d"
				}
			};
			var plot = $.plot($("#graph"), data, options);
		});
		
		</script>
	</head>
	<body>
		<h1>AWS report</h1>
		<div id="graph" style="width: 1200px; height:400px"></div>
	</body>
</html>
