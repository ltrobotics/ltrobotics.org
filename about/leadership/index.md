---
layout: normal
title: Leadership
subtitle: The officers for the 2022 - 2023 school year
---
<div class="row gtr-5000">
  {% for officer in site.data.officers %}
    <div class="col-3">
      <span class="image fit"><img src="{{ site.url }}{{ officer.img }}" alt="{{ officer.name }}" /></span>
      <h4>{{ officer.name }}</h4>
      <h6>{{ officer.position }}</h6>
      <br>
    </div>
  {% endfor %}
</div>
