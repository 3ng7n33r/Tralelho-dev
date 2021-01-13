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

function togglerow(id) {
	let old = document.getElementsByClassName("activerow");
	while(old.length > 0){
		old[0].classList.remove("activerow");
	}

	let element = document.getElementById(id);
	element.classList.add("activerow");

	let text = element.getElementsByTagName("p")[1].textContent;

	let updown = document.getElementsByClassName("txtUpsideDown")[0];
	updown.textContent = text;
  } 