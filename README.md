# Flask + React + Postgres Starter 

This is a minimal sample Flask and React starter code that demonstrates how both frameworks can be used together in a single page web Application.

The code is based on https://github.com/dternyak/React-Redux-Flask.

## Running The Code Locally

1. Clone the reponsitory
```bash
git clone [TODO INSERT URL]
```
2. Import the project folder into your favorite editor (thats Visual Studio Code for us!)
3. Link your PostgreSQL server by adding the environment variable ```DATABASE_URL``` to your system
  * For Linux based systems: ```export DATABASE_URL=[YOUR URL HERE]```
  * For Windows based systems: ```SET DATABASE_URL=[YOUR URL HERE]```
4. Build the react.js front-end.
```bash
npm run build
```
5. Create the SQL database
```bash
python manage.py create_db
```
6. Start the Flask back-end server
```bash
python manage.py runserver
```
7. Check ```localhost:5000``` in your browser to view the web application.

## Deploying The Code

1. [TODO] setting global environment variables in your system


# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Feedback

* Request a new feature on [GitHub](CONTRIBUTING.md).
* File a bug in [GitHub Issues](https://) [TODO FIX LINK].
* [Tweet](https://twitter.com/microsoft) us with any other feedback.

## Bundled Extensions

The code ships with a set of recommended Visual Studio Code extensions that will empower the developement process of your Flask + React web application. These extensions include rich language support (code completion, go to definition) for both Python and JavaScript, as well as quick deploy to Azure from within VS Code. When the project is imported into VS Code, a notifcation will appear giving you the option to install these extensions. 

List of bundled extensions:

* [Python Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Azure App Service Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureappservice)

## License

Copyright (c) Microsoft Corporation. All rights reserved.

Licensed under the [MIT](LICENSE.txt) License.
