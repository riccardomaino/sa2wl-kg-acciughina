### The Google form where you can submit information

[Add book information along with work role details](https://docs.google.com/forms/d/1BY32F4tUwe_H6dIkfraO4anYmebuVaD7qC5palj4n-w/edit)

### Snapshot of the expected KG in turtle syntax
<blockquote>
urw:1234 a prov:Person;<br>
&nbsp;&nbsp;&nbsp;&nbsp; rdfs:label 'Nora Keita Jemisin';<br>
&nbsp;&nbsp;&nbsp;&nbsp;    urw:gender urw:female;<br>
&nbsp;&nbsp;&nbsp;&nbsp;    dul:hasRole urw:Transnational;<br>
&nbsp;&nbsp;&nbsp;&nbsp;    urw:yearOfBirth urw:1972;<br>
&nbsp;&nbsp;&nbsp;&nbsp;    urw:countryOfBirth urw:USA .<br><br>

urw:5678 a urw:BiographicalSituation ;<br>
&nbsp;&nbsp;&nbsp;&nbsp;    dul:isSettingFor urw:USA , urw:1972 , urw:Transnational , urw:female , urw:artist1234 ;<br>
&nbsp;&nbsp;&nbsp;&nbsp;    prov:wasDerivedFrom urb:wikidata<br>
    
urb:wikidata  schema:url  "https://www.wikidata.org/wiki/Q2427544" .<br>
</blockquote>


### Graphical representation of the KG snapshot 
![The snapshot of a pattern that represents the work roles](./img/work_roles_kg.png)
