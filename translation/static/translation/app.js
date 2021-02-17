//Collapse and pull out sidenav in translation page
function collapsenav() {
	let coll = document.getElementsByClassName("collapsible")[0];
	coll.classList.toggle("active");
	let content = document.getElementsByClassName("content")[0];
    if (content.style.display === "block") {
		content.style.display = "none";
	  } else {
		content.style.display = "block";
	  }
}

//Collapse and pop up upsidedown text in translation page
function txtUpDown() {
	let coll = document.getElementsByClassName("transbutton")[0];
	coll.classList.toggle("active");
	let content = document.getElementsByClassName("txtUpsideDown")[0];
    if (content.style.display === "block") {
		content.style.display = "none";
	  } else {
		content.style.display = "block";
	  }
}

function switchVisibilityBlock(ID) {
	let element = document.getElementById(ID);
	if (element.style.display === "block") {
		element.style.display = "none";
		} else {
		element.style.display = "block";
		}
  } 

function switchVisibilityFlex(ID) {
	let element = document.getElementById(ID);
	if (element.style.display === "flex") {
		element.style.display = "none";
		} else {
		element.style.display = "flex";
		}
  } 

//send text to upsidedown translator
function togglerow(id) {
	// toggle off old selection
	let old = document.getElementsByClassName("activerow");
	while(old.length > 0){
		old[0].classList.remove("activerow");
	}

	// grab new element, set css to active, grab its p-text, grab upsidedown box
	let element = document.getElementById(id);
	element.classList.add("activerow");
	let text = element.getElementsByTagName("p")[1].textContent;
	let updown = document.getElementsByClassName("txtUpsideDown")[0];
	updown.textContent = text;

	let textbox = document.getElementById("fittext")

	// adjust font to fit container on mobile
	if (textbox.clientWidth < 400 || textbox.clientHeight < 250){
		if (text.length > 170){
			textbox.style.fontSize = "25px"
		} else if (text.length > 100) {
			textbox.style.fontSize = "30px"
		} else {
			textbox.style.fontSize = "40px"
		}
	}
  }
  



