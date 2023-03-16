const sortSidebar = document.getElementById('sort-sidebar');
const hideSortSidebarBtn = document.getElementById('hide-sidebar-btn');
const btnReset = document.getElementById('sidebar-btn');
const sideBar = document.getElementById('side-bar');

function hideSortSidebar() {
    hideSortSidebarBtn.addEventListener('click', (event) => {
        event.preventDefault();
        sortSidebar.classList.toggle('hide');
        hideSortSidebarBtn.classList.toggle('fa-angle-double-down');
        hideSortSidebarBtn.classList.toggle('sidebar-hide__btn');
        btnReset.classList.toggle('hide');
        sideBar.classList.toggle('sidebar__hide');
    });
}

hideSortSidebar();