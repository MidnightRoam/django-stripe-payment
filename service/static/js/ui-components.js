function changeItemFavoriteIcon() {
    let favoriteImg = document.getElementById("favorite-img");

    favoriteImg.addEventListener("mouseover", () => {
        favoriteImg.src = 'https://cdn-icons-png.flaticon.com/512/535/535183.png'
    })

    favoriteImg.addEventListener("mouseout", () => {
        favoriteImg.src = 'https://cdn-icons-png.flaticon.com/512/535/535285.png'
    })
}

changeItemFavoriteIcon();

function showPopup() {
    const popupImg = document.querySelectorAll('.popup')
    const screenShot = document.querySelectorAll('.screenshot')
    const closePopup = document.getElementById("popup-close")


    popupImg.forEach((popup) => {
        popup.addEventListener('click', () => {
            popup.classList.toggle('popup-open')
            closePopup.classList.toggle('hide')
            document.body.classList.toggle("stop-scrolling");
        })

        closePopup.addEventListener('click', () => {
            popup.classList.remove('popup-close')
            console.log('закрыто')
        })
    })
}

showPopup();

