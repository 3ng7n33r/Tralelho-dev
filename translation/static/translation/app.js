function collapsenav() {
	let coll = document.getElementsByClassName("collapsible");
	coll[0].classList.toggle("active");
	let content = document.getElementsByClassName("content");
    if (content[0].style.display === "block") {
		content[0].style.display = "none";
	  } else {
		content[0].style.display = "block";
	  }
}

function txtUpDown() {
	let coll = document.getElementsByClassName("transbutton");
	coll[0].classList.toggle("active");
	let content = document.getElementsByClassName("txtUpsideDown");
    if (content[0].style.display === "block") {
		content[0].style.display = "none";
	  } else {
		content[0].style.display = "block";
	  }
}