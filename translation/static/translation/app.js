let coll = document.getElementsByClassName("collapsible");
let i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    let content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
} 

function collapsenav() {
	let coll = document.getElementsByClassName("collapsible");
	coll[0].classList.toggle("active");
	let nav = document.getElementsByClassName("content");
	nav[0].style.display = "none";
}