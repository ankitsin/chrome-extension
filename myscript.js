var div_content = document.getElementsByClassName('project-title');
for (var i = 0; i < div_content.length; i++) 
{
    var item=div_content[i];
    var movie_name=item.getElementsByTagName('h2');
    var name = movie_name[0].innerHTML;
    var halfurl="http://www.omdbapi.com/?t=";
    var url= halfurl.concat(name);
    // var url = full;
    var add_rating = document.createElement('p'); 
    jQuery.ajaxSetup({
        async: false
    });
    jQuery.getJSON(url, function (data) {
       add_rating.textContent= data.imdbRating;
    });
    item.appendChild(add_rating);
}
