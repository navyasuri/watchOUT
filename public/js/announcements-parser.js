let parse = () => {
    let data = []

    let announcements = document.getElementsByClassName('entry')
    let titles = document.getElementsByClassName('title')
    let dates = document.getElementsByClassName('date')
    let locations = document.getElementsByClassName('location')
    let descriptions = document.getElementsByClassName('desc')
    let urls = document.getElementsByClassName('url')
    let texts = document.getElementsByClassName('text')

    for(let i in announcements){
        if(i == 'item') break
        if(i == 'length') break
        let a = {'links':{'url':'','text':''}}
        a.title = titles[i].value
        a.date = dates[i].value
        a.location = locations[i].value
        a.description = descriptions[i].value
        a.links.url = urls[i].value
        a.links.text = texts[i].value

        data.push(a)
    }
    send({'data':data})
}
