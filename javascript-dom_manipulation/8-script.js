// Function to fetch data from the API
async function fetchHello() {
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
    const data = await response.json();
    const helloElement = document.getElementById('hello');
    helloElement.textContent = data.hello;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Call the fetchHello function when the script is loaded
window.addEventListener('load', fetchHello);