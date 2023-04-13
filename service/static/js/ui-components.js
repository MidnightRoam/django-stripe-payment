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
        if (popup) {
            popup.addEventListener('click', () => {
                popup.classList.toggle('screenshot-open')
                closePopup.classList.toggle('hide')
                document.body.classList.toggle("stop-scrolling");
            })
        }
        if (closePopup) {
            closePopup.addEventListener('click', () => {
                popup.classList.remove('popup-close')
            })
        }
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

function sliderGameTrailers() {
    // Slider for game screenshots on the game detail page
    const left = document.getElementById("left")
    const right = document.getElementById("right")
    const screenshots = document.querySelectorAll(".game__trailer")
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

sliderGameTrailers()


function switchGameScreenshotOrTrailer() {
    const screenshotsBar = document.getElementById('screenshots-bar');
    const trailerBar = document.getElementById('trailer-bar');
    const screenshots = document.getElementById('screenshots');
    const trailerPopup = document.getElementById('trailer-popup');

    screenshotsBar.addEventListener('click', () => {
        screenshots.classList.add('active');
        screenshotsBar.classList.add('active__bar');
        trailerBar.classList.remove('active__bar');
        trailerPopup.classList.remove('active')
    })

    trailerBar.addEventListener('click', () => {
        screenshots.classList.remove('active');
        screenshotsBar.classList.remove('active__bar');
        trailerBar.classList.add('active__bar');
        trailerPopup.classList.add('active')
    })
}

switchGameScreenshotOrTrailer()


function switchGameSubInfoFields() {
    const switchers = document.querySelectorAll('.about__link');
    const productDescription = document.getElementById('product-description');
    const productRequirements = document.getElementById('product-requirements');
    const productSubInfo = document.getElementById('product-sub-info');

    switchers.forEach((switcher) => {
        switcher.addEventListener('click', (e) => {
            e.preventDefault();
            switchers.forEach((siblingSwitcher) => {
                if (siblingSwitcher !== switcher) {
                    siblingSwitcher.classList.remove('active');
                }
            })

            switcher.classList.add('active');

            if (switcher.textContent === 'ABOUT GAME') {
                productRequirements.classList.add('hide');
                productDescription.classList.remove('hide');
            } else if (switcher.textContent === 'SYSTEM REQUIREMENTS') {
                productRequirements.classList.remove('hide');
                productDescription.classList.add('hide');
            }

            if (switcher.textContent != 'ABOUT GAME') {
                productSubInfo.classList.add('rounded');
            } else {
                productSubInfo.classList.remove('rounded');
            }
        });
    });
}

switchGameSubInfoFields();


function openFullGameTechRequirements() {
    const minimalReqs = document.getElementById('minimal-reqs');
    const recommendedReqs = document.getElementById('recommended-reqs');


    minimalReqs.addEventListener('click', () => {
        minimalReqs.classList.toggle('active');
    })

    recommendedReqs.addEventListener('click', () => {
        recommendedReqs.classList.toggle('active');
    })
}

openFullGameTechRequirements();
