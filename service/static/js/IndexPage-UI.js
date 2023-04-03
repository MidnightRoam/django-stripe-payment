function openGameCatalog() {
    // Open game catalog popup on the index page
    const buttonOpen = document.getElementById('open-catalog');
    const popupCatalog = document.getElementById('items-catalog');

    buttonOpen.addEventListener('click', () => {
        popupCatalog.classList.toggle('active');
        buttonOpen.classList.toggle('btn-active');
        document.body.classList.toggle("stop-scrolling");
    })
}

openGameCatalog();
