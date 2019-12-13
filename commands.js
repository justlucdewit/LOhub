//handeling loading the record table----------------------------------------------------------------------
function load(type="5x5 single"){
	fetch('data/'+type+'.json').then(res=>res.json()).then(data=>{
		const json = data;
		let rank = 1
		for (const elem in json){
			build(json[elem], rank, type);
			rank+=1
		}
		document.getElementById("loading").remove();
	});
}

function isFMC(catagory){
	return catagory.endsWith("FMC");
}

function build(obj, rank, catagory){
	if (isFMC(catagory)){
		document.getElementById("headertime").innerText="Moves";
	}

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
	if (obj.evidence != "/"){
		evidencecell.innerHTML = "<a href="+obj.evidence+">Link</a>"
	}
	
	console.log(obj.comments)
	if (obj.comments != "/"){
		commentcell.innerHTML = obj.comments;
	}
}

function tableClear(){
	const rows = document.getElementById("table").children[0].children.length;
	for (let i = 0; i < rows-1; i++){
		document.getElementById("table").children[0].children[1].remove();
	}
}

function changeEvent(){
	const event = document.getElementById("dropdown").value;
	document.getElementById("event").innerText = event;
	tableClear()
	load(event);
}