const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.side-links');
    const sideLinks = document.querySelectorAll('.side-links li')

    burger.addEventListener('click',()=>{
        // This toggles the Nav
       nav.classList.toggle('nav-active');

       //Animates the links coming into display
       sideLinks.forEach((link, index) => {
           if(link.style.animation) {
               link.style.animation = '';
           }
           else {
               link.style.animation = `sideLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
           }
       });
       // Burger animation
        burger.classList.toggle('toggle');
    });
};

navSlide();

const BackToTopBtn = document.querySelector("#backtotop");

BackToTopBtn.addEventListener("click", backToTop);

function backToTop() {
    window.scrollTo(0, 0);
}


// Sign-up
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Login
var modal = document.getElementById('id02');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}