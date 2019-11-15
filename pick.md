---
layout: page
title: Pick
permalink: /pick/
---

<body>
<p id="deep_list" onload="brython()">
    {% include_relative deep_list.txt %}
</p>

<script type="text/javascript">

    alert(document.getElementById('deep_list').innerHTML)

</script>

<script type="text/python">

    from browser import document, alert

    from select_movie import *

    alert("yo")

    file_content = document["deep_list"].text

    movie_list = create_list(file_content)

    document <= "Random 6 movies:\n\n"

    document <= random_n_list(movie_list, 6)

</script>
