---
layout: normal
title: Sponsors
subtitle: We are very grateful for these organizations for sponsoring us!

---
<div class="box-alt">
  <div class="row gtr-uniform">
    <section class="col-1"></section>
    {% for sponsor in site.data.sponsors %}
      <section class="col-3 col-5">
        <span class="image fit"><img src="{{ site.url }}{{ sponsor.img }}" alt="{{ sponsor.name }}" /></span>
        <h3><a href="{{ sponsor.link }}">{{ sponsor.name }}</a></h3>
        <p>{{ sponsor.desc }}</p>
      </section>
    {% endfor %}
  </div>
</div>
