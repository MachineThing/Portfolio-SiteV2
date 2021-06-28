# Mason's Portfolio Site V2
[![Build status](https://img.shields.io/github/workflow/status/Machinething/Portfolio-SiteV2/Test%20Website/development?label=Build)](https://github.com/MachineThing/Portfolio-SiteV2/actions/workflows/test.yml)

*Soon to be located at [masonfisher.net](https://www.masonfisher.net)*

## Dotenv Settings
*Note: Please put strings in quotation marks or the dotenv file may not be read correctly!*
### Main Settings
Parameter | Description | Value type
--- | --- | ---
SECRET_KEY | [Django Secret Key](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY) | *String*
GITHUB_KEY | GitHub API key, you can get one [here](GITHUB_KEY="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") | *String*
GITHUB_USER | Username of a GitHub user, used for the "grassgraph" | *String*

### Database Settings
Parameter | Description | Value type
--- | --- | ---
USE_SQLITE | Set this to **True** (without quotation marks) to use Sqlite3 database, or set this to **False** (without quotation marks) to use Postgresql database, Postgresql is preferred over Sqlite3 especially in a production environment. | *Boolean*
PG_DATABASE | Name of the Postgresql database, can be ignored if *USE_SQLITE* is set to **True** | *String*
PG_USER | Username of the user that controls the *PG_DATABASE* database, can be ignored if *USE_SQLITE* is set to **True** | *String*
PG_PASSWORD | Password of the user that controls the *PG_DATABASE* database, can be ignored if *USE_SQLITE* is set to **True** | *String*
PG_ADDRESS | The IP address where the Postgresql database is located at, if the database is on the same server where the the website is located at use the address "127.0.0.1" | *String*
