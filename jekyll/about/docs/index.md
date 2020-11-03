---
layout: normal
title: Documents
subtitle: Important Club Documents and Forms
---
<section id="content">
    <h4>View and download here:</h4>
    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>File</th>
            <th>Description</th>
            <th>Download</th>
          </tr>
        </thead>
        <tbody>
          {% for document in site.data.docs %}
            <tr>
              <td>{{ document.name }}</td>
              <td>{{ document.desc }}</td>
              <td><a href="{{ document.link }}" class="button primary small icon solid fa-download" target="_blank">DL</a></td>
              </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
</section>
