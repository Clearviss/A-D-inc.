
/*Pierdolone api nie dziala*/
const APILINK = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=849f27806ad805267c166186bcc24106&page=1'
const IMG_PATH = 'https://image.tmdb.org/t/p/w1280'
const SEARCHAPI = 'https://api.themoviedb.org/3/search/movie?&api_key=849f27806ad805267c166186bcc24106&query='

const main = document.getElementById("section")
const form = document.getElementById("form")
const search = document.getElementById("query")
returnMovies(APILINK)
function returnMovies(url) {
    /* pierdolony uganda huja wyjasnil i tera nie wiem co te pierdolone gowno robi ale dzialalo dopoki api nie spierdolili */
    fetch(url).then(res => res.json()).then(function(data){
        console.log(data.results);
        data.results.forEach(element => {
            const div_card = document.createElement('div');
            div_card.setAttribute('class', 'card')
            const div_row = document.createElement('div');
            div_row.setAttribute('class', 'row')
            const div_column = document.createElement('div');
            div_column.setAttribute('class', 'column')
            const div_image = document.createElement('img');
            div_image.setAttribute('class', 'thumbnail')
            div_image.setAttribute('id', 'image')
            const div_title = document.createElement('h3');
            div_title.setAttribute('id', 'title')
            const div_center = document.createElement('center');

            div_title.innerHTML = `${element.title}`
            div_image.src = IMG_PATH + element.poster_path

            div_center.appendChild(div_image)
            div_card.appendChild(div_center)
            div_card.appendChild(div_title)
            div_column.appendChild(div_card)
            div_row.appendChild(div_column)

            main.appendChild(div_row)
        });
    });
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    main.innerHTML = ''

    const searchItem = search.value

    if (searchItem) {
        returnMovies(SEARCHAPI + searchItem)
        search.value = ''
    }
})

