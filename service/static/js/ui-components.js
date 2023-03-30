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

function showScreenshotPopup() {
    // Show game screenshot in full size
    const popupImg = document.querySelectorAll('.popup')
    const screenShot = document.querySelectorAll('.screenshot')
    const closePopup = document.getElementById("screenshot-close")


    popupImg.forEach((popup) => {
        popup.addEventListener('click', () => {
            popup.classList.toggle('screenshot-open')
            closePopup.classList.toggle('hide')
            document.body.classList.toggle("stop-scrolling");
        })

        closePopup.addEventListener('click', () => {
            popup.classList.remove('popup-close')
        })
    })
}

showScreenshotPopup();

function dropdownGameLanguages() {
    // Show game localization languages dropdown menu
    const gameLanguages = document.getElementById("languages");
    const dropdown = document.getElementById("languages-dropdown");
    const caret = document.getElementById("caret");

    gameLanguages.addEventListener('click', () => {
        dropdown.classList.toggle('dropdown-show');
        caret.classList.toggle('rotate');
    })
}

dropdownGameLanguages()


function sliderGameScreenshots() {
    // Slider for game screenshots on the game detail page
    const left = document.getElementById("left")
    const right = document.getElementById("right")
    const screenshots = document.querySelectorAll(".screenshot")
    let offset = 0

    left.addEventListener('click', () => {
    if (offset >= 0) return
        offset += 100;
        screenshots.forEach(screenshot => {
          screenshot.style.left = `${offset}%`;
        });
        console.log('right')
    });

    right.addEventListener('click', () => {
    if (offset <= -(100 * (screenshots.length - 1))) {
        offset = 100;
    };
        offset -= 100;
        screenshots.forEach(screenshot => {
          screenshot.style.left = `${offset}%`;
        });
        console.log('left')
    });
}

sliderGameScreenshots()

