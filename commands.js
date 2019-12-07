let json;
let months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
function add(name, time, moves, link){
	submit ={
		"name": name,
		"time": time,
		"date": new Date().getFullYear()+"-"+new Date().getMonth()+"-"+new Date().getDay(),
		"evidence": link,
		"comments": moves+" moves"
	}
	json[name] = submit;
}

function load(){
	$.getJSON('data/5x5.json', function(data) {
    	json = data;
    	loadall()
	});
}

function build(obj){
	let table = document.getElementById("table");
	let row = table.insertRow(-1);

	let namecell = row.insertCell(0);
	let timecell = row.insertCell(1);
	let datecell = row.insertCell(2);
	let evidencecell = row.insertCell(3);
	let commentcell = row.insertCell(4);


	namecell.innerHTML = obj.name;
	timecell.innerHTML = obj.time;
	datecell.innerHTML = obj.date;

	let a = document.createElement('a');
	var linkText = document.createTextNode("Link");
	a.appendChild(linkText);
	a.title = "Link"
	a.href = obj.evidence;
	evidencecell.appendChild(a);
	commentcell.innerHTML = obj.comments
}

function len(jso){
	counter = 0;
	for (elem in jso){
		counter++;
	}
	return counter;
}

function loadall(){
	for (elem in json){
		console.log(elem)
		build(json[elem])
	}
}

load()
//setTimeout(function(){loadall()}, 1000); 