const addItemButton = document.getElementById('add_item');
const itemList = document.querySelector('ul.my_list');

addItemButton.addEventListener('click', function() {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  itemList.appendChild(newItem);
});
