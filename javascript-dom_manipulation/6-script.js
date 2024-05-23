const characterElement = document.getElementById("character");

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(response => response.json()) //parse the json response
.then(data => {
  characterElement.textContent = data.name;
})
    .catch(error => {
      characterElement.textContent = 'Error fetching character name';
      console.error(error);  // Log the error for debugging
    });
