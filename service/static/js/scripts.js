function ajaxSend(url) {
    // Send request
    fetch(`${url}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
      .then(response => response.json())
      .then(json => render(json))
      .catch(err => console.error(err))
}

function filterFormAjax() {
  const form = document.querySelector('form[name=filter]');
  form.addEventListener('change', function(e) {
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();

//    // Get the selected value from the selected element
//    const selectedElement = e.target;
//    const selectedValue = selectedElement.value;
//
//    // Create an object with only the selected value
//    const formData = {
//      [selectedElement.name]: selectedValue
//    };
//
//    // Convert the object to URL-encoded string
//    const params = new URLSearchParams(formData).toString();
//    console.log(params);
//    // Send the selected value using AJAX
//    const url = this.action;
    ajaxSend(url, params);
  })
}
filterFormAjax();

function render(data) {
//    // Render template
//    let output = template.render(data);
//
//    const div = document.querySelector('.products')
//    div.innerHTML = output;
//    console.log(data)
}




