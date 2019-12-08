//handeling loading the record table----------------------------------------------------------------------
function load(type="5x5 single"){
	fetch('data/'+type+'.json').then(res=>res.json()).then(data=>{
		const json = data;
		let rank = 1
		for (const elem in json){
			build(json[elem], rank);
			rank+=1
		}
	});
}

function build(obj, rank){
	const table = document.getElementById("table");
	const row = table.insertRow(-1);
	
	const rankcell = row.insertCell(0)
	const namecell = row.insertCell(1);
	const timecell = row.insertCell(2);
	const datecell = row.insertCell(3);
	const evidencecell = row.insertCell(4);
	const commentcell = row.insertCell(5);

	rankcell.innerHTML = rank
	namecell.innerHTML = obj.name;
	timecell.innerHTML = obj.time;
	datecell.innerHTML = obj.date;
	evidencecell.innerHTML = "<a href="+obj.evidence+">Link</a>"
	// const linkText = document.createTextNode("Link");
	// const a = document.createElement('a').appendChild(linkText);
	
	// a.title = "Link";
	// a.href = obj.evidence;
	// evidencecell.appendChild(a);
	console.log(obj.comments)
	if (obj.comments != "/ moves"){
		commentcell.innerHTML = obj.comments;
	}else{
		commentcell.innerHTML = "/"
	}
}

function tableClear(){
	const rows = document.getElementById("table").children[0].children.length;
	for (let i = 0; i < rows-1; i++){
		document.getElementById("table").children[0].children[1].remove();
	}
}

//handeling the form input----------------------------------------------------------------------------------
function changeEvent(){
	const event = document.getElementById("dropdown").value;

	//change title
	document.getElementById("event").innerText = event;

	//clear table
	tableClear()

	//load new data
	load(event);
}