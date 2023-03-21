const hamb = document.getElementById('hamb');
const popup = document.querySelector('#popup');
const body = document.body;

// Clone navbar for a custom mobile css styles
const navbar = document.querySelector('#navbar');

hamb.addEventListener('click', hambHandler);

// Click on hamburger menu
function hambHandler(e) {
    e.preventDefault();
    popup.classList.toggle("open");
    hamb.classList.toggle("active");
    renderPopup();
}

// Render of popup's elements
function renderPopup() {
    popup.appendChild(navbar);
}

// Code for a close popup on clicking on link
const links = Array.from(navbar.children);


// For every navbar's element on click calling function
links.forEach((link) => {
    link.addEventListener("click", closeOnClick);
});

// Closing popup when clicking on a link
function closeOnClick() {
    popup.classList.remove("open");
    hamb.classList.remove("active");
}