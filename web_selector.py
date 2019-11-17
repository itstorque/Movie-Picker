from browser import document, alert

from select_movie import *

file_content = document["deep_list_data_src"].text

while "\n " in file_content:

  file_content = file_content.replace("\n ", "\n")

while "  " in file_content:

  file_content = file_content.replace("  ", " ")

while "\n\n" in file_content:

  file_content = file_content.replace("\n\n", "\n")

movie_list = create_list(file_content)

file_content = "\n".join(sorted(movie_list))

chosen_movies = random_n_list(movie_list, 6)

for movie_title in chosen_movies:

  file_content = file_content.replace(movie_title, "<span class='selected'>" + movie_title + "</span>")

document["deep_list"].html = file_content

command = 'answers=["Movie Poll for "+(new Date()).getMonth()+"/"+(new Date()).getDay(),"%s","%s","%s","%s","%s","%s"];x=document.getElementsByClassName("_30yy _7oam");for(var i=0;i<x.length;i++){if(x[i].title=="Create a poll"){x=x[i];break}};x.click();setTimeout(()=>{for(var i=0;i<6;i++){document.getElementsByClassName("_5n1-")[0].click()};setTimeout(()=>{y=document.getElementsByClassName("_58al");for(var i=0;i<7;i++){y[i+1].value=answers[i]}},200)},100)' % tuple(chosen_movies)

document["command_placeholder"].text = command
