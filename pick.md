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

    var copyText = document.createElement('input');
    document.body.appendChild(copyText)

    copyText.select();
    copyText.setSelectionRange(0, 99999);

    document.execCommand("copy");

    alert("Copied the script: " + copyText.value);
    copyText.remove()

  };

</script>
