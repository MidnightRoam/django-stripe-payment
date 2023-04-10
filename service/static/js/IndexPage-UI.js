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


function openFullFilteringForm() {
    const buttonOpen = document.getElementById('open-filter-form');
    const filteringForm = document.getElementById('filtering-form');

    buttonOpen.addEventListener('click', (e) => {
        e.preventDefault();
        filteringForm.classList.toggle('form__active');
    })
}

openFullFilteringForm();
