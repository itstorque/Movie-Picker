---
layout: page
title: Pick
enable_brython: True
permalink: /pick
permalink_name: /pick
---


<p id="command_placeholder"></p>

<p id="deep_list_data_src" hidden>
    {% include_relative deep_list.txt %}
</p>

<p id="deep_list">
    {% include_relative deep_list.txt %}
</p>

<script type="text/python" src="web_selector.py"></script>

<script type="text/javascript">
  window.onload = function() {
     brython();
  }
</script>
