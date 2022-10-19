

function updateFav(id){
    const fav = $(`#${id}`)

    const color = fav.css('color')
    fetch(`http://localhost:8000/updateFav/${id}`)
    if(color === 'rgb(128, 128, 128)')
        fav.css('color','red')
    else
        fav.css('color','grey')

}

