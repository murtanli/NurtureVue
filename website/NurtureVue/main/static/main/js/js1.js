window.onload = function() {
    showSlides(1);
  }



function showSlides(index) {
  var slides = document.getElementsByClassName("slide1");
  var buttons = document.getElementsByClassName("but1");

  

  for (var i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    buttons[i].style.background = "rgba(26, 34, 38, 1)";
    buttons[i].style.color = "white";
    buttons[i].classList.remove("active");

    buttons[i].addEventListener("mouseenter", function() {
      this.style.background = "rgba(32, 209, 60, 1)";
      this.style.color = "black";
    });

    buttons[i].addEventListener("mouseleave", function() {
      if (!this.classList.contains("active")) {
        this.style.background = "rgba(26, 34, 38, 1)";
        this.style.color = "white";
      }
    });
  }

  slides[index - 1].style.display = "block";
  buttons[index - 1].style.background = "rgba(32, 209, 60, 1)";
  buttons[index - 1].style.color = "black";
  buttons[index - 1].classList.add("active");
}
  