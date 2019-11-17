---
layout: page
title: Pick
enable_brython: True
permalink: /pick
---


<p id="command_placeholder"></p>

<p id="deep_list_data_src" onload="brython()" hidden>
    {% include_relative deep_list.txt %}
</p>

<p id="deep_list">
    {% include_relative deep_list.txt %}
</p>

<script type="text/python" src="web_selector.py"></script>
