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