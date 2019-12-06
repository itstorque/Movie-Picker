---
layout: page
title: Pick
enable_brython: True
permalink: /pick
permalink_name: /pick
---


<p id="command_placeholder" hidden></p>
<a id="copy_js">Copy JS Script For Messenger</a>

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

  document.getElementById("copy_js").onclick = function(){

    var fake_input = document.createElement('input');
    document.body.appendChild(fake_input)
    inp.value = document.getElementById("command_placeholder").textContent
    inp.select();
    document.execCommand('copy', false);
    inp.remove();

  };
  
</script>
