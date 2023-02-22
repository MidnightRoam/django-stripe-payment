let favoriteImg = document.getElementById("favorite-img");

favoriteImg.addEventListener("mouseover", () => {
    favoriteImg.src = 'https://cdn-icons-png.flaticon.com/512/535/535183.png'
})

favoriteImg.addEventListener("mouseout", () => {
    favoriteImg.src = 'https://cdn-icons-png.flaticon.com/512/535/535285.png'
})