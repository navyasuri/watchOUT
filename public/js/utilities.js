let add = (field) => {
  //console.log(field)
  let btn = field.lastChild
  let newIn = document.createElement('input')
  if (btn.previousSibling == null || btn.previousSibling.value.length != 0) {
    // Create new input field, give it a class:
    newIn.className += "entry-field"
    // Add the new input, keeping the button at the bottom:
    field.removeChild(btn)
    field.appendChild(newIn)
    field.appendChild(btn)
  }
}

let listParse = (obj, populate, list) => {
    // 'populate' is the array to be populated, passed as obj.populate, e.g. person.tags
    for(var x of list.children)
        // Check that we are working with <input> elements:
        if(x.nodeName === "INPUT") {
            //console.log(x.nodeName)
            // Push the child input field if not blank:
            if(x.value !== "") {
                populate.push(x.value)
                //console.log("pushed")
                //console.log(x.value)
            }
            // If the input IS blank, skip it:
            if(x.value === "") {
                //console.log("Empty, skipped: ")
                //console.log(x.value)
            }
            // If the input is blank AND this array is empty, add a blank slot:
            if(x.value === "" && populate.length == 0) {
                //console.log("Empty array! ISSUE")
                populate.push("")
            }
        }
        //console.log(populate)
}

let send = (_data) => {
  $.ajax({
    // 'http://localhost:5000/data/' +
    url: 'https://imheroku.herokuapp.com/save/' + document.getElementById('category').innerText,
    method: 'POST',
    data: _data,
    dataType: 'json'
  }).done((data)=>{
    alert(data.message)
  }).fail((data)=>{
    // console.log(err);
    alert('saved did not work... failed\n'+data.error)
  })
}
