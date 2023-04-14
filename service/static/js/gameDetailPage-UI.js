function switchOtherProductsSections() {
    // Переключает состояния у кнопок
    const switchers = document.querySelectorAll('.others__switcher');

    switchers.forEach((switcher) => {
        switcher.addEventListener('click', (e) => {
            e.preventDefault();
            switchers.forEach((siblingSwitcher) => {
                if (siblingSwitcher !== switcher) {
                    siblingSwitcher.classList.remove('active');
                }
            })
            switcher.classList.add('active');
            otherSectionsActive();
        })
    })
}

switchOtherProductsSections();


function otherSectionsActive() {
    // Переключает состояние у блоков с связанными играми / игровой серией
    const relatedGames = document.querySelectorAll('.related__games');
    const switchers = document.querySelectorAll('.others__switcher');

    switchers.forEach((switcher) => {
        if (switcher.classList.contains('active')) {
            const index = Array.from(switchers).indexOf(switcher)

            relatedGames.forEach((card, i) => {
                if (i === index) {
                    card.classList.add('active');
                } else {
                    card.classList.remove('active');
                }
            })
        }
    })
}

function addonsSectionSlider() {
    // Слайдер для прокрутки списка связанных с игрой игр
    const switcherLeft = document.getElementById('other-products-left');
    const switcherRight = document.getElementById('other-products-right');
    const addons = document.querySelectorAll('.addon__switcher');
    let offset = 0

    switcherLeft.addEventListener('click', () => {
        if (offset >= 0) {
            offset -= 50 * (addons.length - 1)
        } else {
            offset += 50;
        }
        addons.forEach(addon => {
            addon.style.left = `${offset}%`
        })
    });

    switcherRight.addEventListener('click', () => {
        if (offset <= -(50 * (addons.length - 1))) {
            offset = 0;
        } else {
            offset -= 50;
        }
        addons.forEach(addon => {
            addon.style.left = `${offset}%`
        })
    });
}

addonsSectionSlider();
