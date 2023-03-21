const sideBar = document.getElementById('side-bar');
const openSideBar = document.getElementById('open-sidebar');

openSideBar.addEventListener('click', sideBarHandler)


function sideBarHandler() {
    sideBar.classList.toggle('open-sidebar');
}


