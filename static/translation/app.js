//Collapse and pop up upsidedown text in translation page
function txtUpDown() {
	let coll = document.getElementById("transbutton");
	coll.classList.toggle("pressed");
	let translation = document.querySelectorAll('td:last-child');
	let baselanguage = document.querySelectorAll('td:first-child');
	let content = document.getElementsByClassName("txtUpsideDown")[0];
	let h2 = document.getElementsByClassName("category")
    if (content.style.display === "block") {
		content.style.display = "none";

		for (var i = 0; i < h2.length; i++) {
			h2[i].classList.toggle("transmode")
		  }

		for (let i=0, len = translation.length; i<len; i++) {
			translation[i].style.removeProperty("display")
			baselanguage[i].style.removeProperty("border-radius")
		}
	  } else {
		content.style.display = "block";

		for (var i = 0; i < h2.length; i++) {
			h2[i].classList.toggle("transmode")
		  }

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

	// adjust font to fit container on a tablet
	if (textbox.clientWidth < 800 || textbox.clientHeight < 800){
		if (text.length > 170){
			textbox.style.fontSize = "30px"
		} else if (text.length > 80) {
			textbox.style.fontSize = "40px"
		} else {
			textbox.style.fontSize = "50px"
		}
	}

	// adjust font to fit container on mobile
	if (textbox.clientWidth < 400 || textbox.clientHeight < 400){
		if (text.length > 170){
			textbox.style.fontSize = "25px"
		} else if (text.length > 80) {
			textbox.style.fontSize = "30px"
		} else {
			textbox.style.fontSize = "40px"
		}
	}
  }
  



