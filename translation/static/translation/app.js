//Collapse and pull out sidenav in translation page
function collapsenav() {
	let coll = document.getElementById("collapsebutton");
	coll.classList.toggle("transbutton--pressed");
	let content = document.getElementsByClassName("description");
	for (let i=0, len=content.length; i<len; i++) {
		content[i].classList.toggle("hidden")
	}
}

//Collapse and pop up upsidedown text in translation page
function txtUpDown() {
	let coll = document.getElementById("transbutton");
	coll.classList.toggle("neumorphic--pressed");
	let translation = document.querySelectorAll('td:last-child');
	let baselanguage = document.querySelectorAll('td:first-child');
	let content = document.getElementsByClassName("txtUpsideDown")[0];
    if (content.style.display === "block") {
		content.style.display = "none";
		for (let i=0, len = translation.length; i<len; i++) {
			translation[i].style.removeProperty("display")
			baselanguage[i].style.removeProperty("border-radius")
		}
	  } else {
		content.style.display = "block";
		for (let i=0, len = translation.length; i<len; i++) {
			translation[i].style.display = "none";
			baselanguage[i].style.borderRadius = "10px";
		}
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
		} else if (text.length > 85) {
			textbox.style.fontSize = "30px"
		} else {
			textbox.style.fontSize = "40px"
		}
	}
  }
  



