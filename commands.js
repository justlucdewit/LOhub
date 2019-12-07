//handeling loading the record table----------------------------------------------------------------------
function load(type="5x5 single"){
	fetch('data/'+type+'.json').then(res=>res.json()).then(data=>{
		const json = data;
		for (const elem in json){
			build(json[elem]);
		}
	});
}

function build(obj){
	const table = document.getElementById("table");
	const row = table.insertRow(-1);

	const namecell = row.insertCell(0);
	const timecell = row.insertCell(1);
	const datecell = row.insertCell(2);
	const evidencecell = row.insertCell(3);
	const commentcell = row.insertCell(4);

	namecell.innerHTML = obj.name;
	timecell.innerHTML = obj.time;
	datecell.innerHTML = obj.date;

	const linkText = document.createTextNode("Link");
	const a = document.createElement('a').appendChild(linkText);
	
	a.title = "Link";
	a.href = obj.evidence;
	evidencecell.appendChild(a);
	commentcell.innerHTML = obj.comments;
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