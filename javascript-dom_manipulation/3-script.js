const toggleButton = document.getElementById('toggle_header');
const header = document.querySelector('header');

toggleButton.addEventListener('click', function() {
  header.classList.toggle('red');
  if (header.classList.contains('red')) {
    header.classList.remove('green');
  } else {
    header.classList.add('green');
  }
});
