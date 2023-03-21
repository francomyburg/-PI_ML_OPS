# -PI_ML_OPS
<h1>Proyecto individual N°1 henry  MLOPS</h1>
<h2>Franco Myburg-Cohorte n°8</h2>
<h2>Links<h2>
<a href="https://francomyburg.up.railway.app/docs">API</a><br>
<a href="https://huggingface.co/spaces/Francomyburg/appmovie1">app recomendacion de peliculas</a><br>
<a href="https://www.youtube.com/watch?v=01OkTX-Y9zA">Video("sin audio")</a>
<h3>Resumen del Proyecto</h3>
<p>El proyecto se puede dividir en dos partes, la primera relacionada con el trabajo de un data engineer donde se nos pedía realizar un proceso de ETL(Extract, Transform y Load) de los datos proporcionados y después de este proceso crear una api para realizar consultas a estos datos.<br>
La segunda parte tenemos que tomar el rol de un data scientist y realizar un sistema de recomendación de películas.</p>
<h3>Descripcion del proyecto</h3>
El primer paso es el proceso de ETL que se realiza dentro de un jupyternotebook(ETL.ipnyb) del cual se realizaron las siguentes transformaciones:
<ul>
<li>Crea la columna id(la cual contiene la primera letra de la plataforma + showid) para despues poder unir los datos de las peliculas con los scores de los usuarios</li>
<li>Se rellena los espacios nulos de la columna rating con G(General audiences)</li>
<li>En las columnas que correspondan cambiar al formato de fecha YYYY-MM-DD</li>
<li>La columna Duration se divide en dos duration_int y duration_type</li>
<li>Los campos de textos se pasan a minisculas</li>
<li>Se crean dos datasets a partir de los cambios realizados, uno para el desarrollo de la API al cual se le agregó el promedio de los scores de los usuarios a cada película y otro con cada score por película para el sistema de recomendación</li>
</ul>
El segundo paso fue la creacion de la Api con el framework Fastapi el cual consta de las siguentes funciones
<ul>
<li>get_max_duration: Película con mayor duración con filtros opcionales de año,plataforma y tipo de duración</li>
<li>get_score_count: Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año </li>
<li>get_count_platform: Cantidad de películas por plataforma</li>
<li>get_actor: Actor que más se repite según plataforma y año.</li>
</ul>

El deploy de la api se realizo con docker y railway para alojar en la nube.
<p>
<img src = 'https://bitestreams.com/blogs/fastapitemplate/logos.webp' height = 300></p>
<br><br>
Tercer paso analisis exploratorios de los datos antes de realizar el modelo de machine learning,donde en resumen se observan precencia de valores nulos,las cantidad de scores por peliculas,cantidad de score por usuario,etc.<br>
Cuarto paso se realizo el sistema de recomendacion de peliculas con los datos que se consideraron importantes para el modelo,se utilizo el algoritmo SVD(single value decomposition) de la libreria surprise.

<h2>Archivos</h2>
<ul>
<li><b>ETL.ipynb</b>: notebook donde se realizo el proceso de ETL</li>
<li><b>main.py</b>: script de python donde se desarrollo la API</li>
<li><b>datfinal.csv</b>archivo csv del cual la API consulta los datos</li>
<li><b>dockerfile</b> archivo para crear la imagen del contenedor de docker</li>
<li><b>requirements.txt</b>librerias utilizadas en el proyecto</li>
<li><b>EDA.ipynb</b>: notebook con el analisis exploratorio de los datos</li>
<li><b>ML_project.ipynb</b>: notebook donde se realiza el sistema de recomendacion</li>
<li><b>querys.ipynb</b>: borrador con las querys que utiliza FastApi</li>
</ul>

