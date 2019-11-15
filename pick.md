---
layout: page
title: Pick
enable_brython: True
permalink: /pick
---


<p id="deep_list" onload="brython()">
    {% include_relative deep_list.txt %}
</p>

<script type="text/javascript">

</script>

<script type="text/python">

    from browser import document, alert

    from select_movie import *

    file_content = document["deep_list"].text

    while "\n " in file_content:

      file_content = file_content.replace("\n ", "\n")

    while "  " in file_content:

      file_content = file_content.replace("  ", " ")

    while "\n\n" in file_content:

      file_content = file_content.replace("\n\n", "\n")

    movie_list = create_list(file_content)

    chosen_movies = random_n_list(movie_list, 6)

    for movie_title in chosen_movies:

      file_content = file_content.replace(movie_title, "<span class='selected'>" + movie_title + "</span>")

    document["deep_list"].html = file_content

    document <= "Random 6 movies:\n\n"

    document <= chosen_movies

</script>
