# Mason's Portfolio Site V2
[![Build status](https://img.shields.io/github/workflow/status/Machinething/Portfolio-SiteV2/Test%20Website/development?label=Build)](https://github.com/MachineThing/Portfolio-SiteV2/actions/workflows/test.yml)

Please go to MachineThing/portfolio for the newer version

## Dotenv Settings
*Note: Please put strings in quotation marks or the dotenv file may not be read correctly!*
### Main Settings
Parameter | Description | Value type
--- | --- | ---
SECRET_KEY | [Django Secret Key](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY) | *String*
GITHUB_KEY | GitHub API key, it needs permissions for *read:user*, you can get one [here](https://github.com/settings/tokens") | *String*
CAPTCHA_SECRET_KEY | reCAPTCHA secret key, you can get one [here](https://www.google.com/recaptcha/admin/create) | *String*
CAPTCHA_PUBLIC_KEY | reCAPTCHA site key, you can get one [here](https://www.google.com/recaptcha/admin/create) | *String*

### Database Settings
Parameter | Description | Value type
--- | --- | ---
USE_SQLITE | Set this to **True** (without quotation marks) to use Sqlite3 database, or set this to **False** (without quotation marks) to use Postgresql database, Postgresql is preferred over Sqlite3 especially in a production environment. | *Boolean*
PG_DATABASE | Name of the Postgresql database, can be ignored if *USE_SQLITE* is set to **True** | *String*
PG_USER | Username of the user that controls the *PG_DATABASE* database, can be ignored if *USE_SQLITE* is set to **True** | *String*
PG_PASSWORD | Password of the user that controls the *PG_DATABASE* database, can be ignored if *USE_SQLITE* is set to **True** | *String*
PG_ADDRESS | The IP address where the Postgresql database is located at, if the database is on the same server where the the website is located at use the address "127.0.0.1" | *String*
