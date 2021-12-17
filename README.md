<h2 dir="auto"><a id="user-content-dashboard-description" class="anchor" aria-hidden="true" href="#dashboard-description"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>MA 705 Dashboard</h2>
<p dir="auto">The final dashboard is deployed on Heroku <a href="https://hill-rachel.herokuapp.com" rel="nofollow">here</a>.</p>
<h2 dir="auto"><a id="user-content-dashboard-description" class="anchor" aria-hidden="true" href="#dashboard-description"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Dashboard Description</h2>
<p dir="auto">This dashboard was created to display results from the Tokyo 2020 Olympic Games. More specifically, it was designed to allow a user to choose a sport and an event within that sport, which are used to display visualizations and statistics. The visualizations show the number of medals awarded in that sport and event, both in total and for the United States. Athlete statistics, including the number of athletes, youngest athlete age, oldest athlete age, average athlete age, the number of ranked athletes, and the average athlete rank for the events within the selected sport are displayed in a table. </p>
<h3 dir="auto"><a id="user-content-data-sources" class="anchor" aria-hidden="true" href="#data-sources"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Data Sources</h3>
<p dir="auto">The data was retrieved from an API and csv data file, which were both created mainly from the official Tokyo 2020 Olympics webpage. Data was gathered from the API on the sports and events which was then prepped, grouped by, and merged with the csv data to create two dataframes, infosport for the sports information, and infoevent for the events information. The csv file was also cleaned and prepped before being finalized as the olympics dataframe. All of this work was done in the dashboard prep file and the dataframes were saved in pickle format to be used in the dashboard (app.py).  </p>
<ul dir="auto">
<li><a href="https://olypi.com/" rel="nofollow">API link</a></li>
<li><a href="https://www.kaggle.com/aliaamiri/2020-summer-olympics-dataset" rel="nofollow">CSV link</a></li>
<li><a href="https://olympics.com/en/olympic-games/tokyo-2020" rel="nofollow">Tokyo 2020 Olympics Website</a></li>
</ul>
<h3 dir="auto"><a id="user-content-other-comments" class="anchor" aria-hidden="true" href="#other-comments"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Repository Files Detail</h3>
<ul dir="auto">
<li><strong>Procfile:</strong>
  <a> included to tell Heroku what commands to run to start the web app</a></li>
<li><strong>app.py:</strong>
  <a> python file used to create and run the dashboard </a></li>
<li><strong>dashboardprep.py:</strong>
  <a> python file used to gather, clean, and prep the data to be used in the dashboard </a></li>
<li><strong>infoevent.pkl:</strong>
  <a> pickle file containing dataframe of event information used in creating dashboard </a></li>
<li><strong>infosport.pkl:</strong>
  <a> pickle file containing dataframe of sports information used in creating dashboard </a></li>
<li><strong>olympics.csv:</strong>
  <a> original csv file containing detailed information on athletes, events, and sports used to create dataframes in dashboard prep file </a></li>
<li><strong>olympics.pkl:</strong>
  <a> pickle file containing dataframe of athlete, event, and sports information used in creating dashboard </a></li>
<li><strong>requirements.txt:</strong>
  <a> text file containing the python modules with version numbers needed for the app to run  </a></li>
<li><strong>sports.json:</strong>
  <a> json file containing the data gathered from the API used to create dataframes in dashboard prep file  </a></li>
</ul>

