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




// Google Calendar API docs for Inserts

// Refer to the JavaScript quickstart on how to setup the environment:
// https://developers.google.com/calendar/quickstart/js
// Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
// stored credentials.

var event = {
  'summary': 'Google I/O 2015',
  'location': '800 Howard St., San Francisco, CA 94103',
  'description': 'A chance to hear more about Google\'s developer products.',
  'start': {
    'dateTime': '2015-05-28T09:00:00-07:00',
    'timeZone': 'America/Los_Angeles'
  },
  'end': {
    'dateTime': '2015-05-28T17:00:00-07:00',
    'timeZone': 'America/Los_Angeles'
  },
  'recurrence': [
    'RRULE:FREQ=DAILY;COUNT=2'
  ],
  'attendees': [
    {'email': 'lpage@example.com'},
    {'email': 'sbrin@example.com'}
  ],
  'reminders': {
    'useDefault': false,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10}
    ]
  }
};

var request = gapi.client.calendar.events.insert({
  'calendarId': 'primary',
  'resource': event
});

request.execute(function(event) {
  appendPre('Event created: ' + event.htmlLink);
});
