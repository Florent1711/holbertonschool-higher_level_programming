const movieList = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const movies = data.results;  // Extract movie data from response
      movies.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        movieList.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error(error);  // Log the error for debugging
    });
