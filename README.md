---
author: Rohini More (rohini.more@capgemini.com)
languages: Python
products: azure-active-directory
description: "This sample demonstrates a Python web application calling a Azure Databricks APIs that is secured using Azure Active Directory."

---
# Integrating Microsoft Identity Platform with a Python web application and call Azure Databricks APIs

## About this sample

> This sample is also available as a quickstart for the Microsoft identity platform:
[Quickstart: Add sign-in with Microsoft to a Python web app]("https://docs.microsoft.com/azure/active-directory/develop/quickstart-v2-python-webapp")

### Overview

This sample demonstrates a Python web application that signs-in users with the Microsoft identity platform and calls the Azure Databricks APIs.

1. The python web application uses the Microsoft Authentication Library (MSAL) to obtain a JWT access token from the Microsoft identity platform (formerly Azure AD v2.0):
2. The access token is used as a bearer token to authenticate the user when calling the Microsoft Azure Databricks APIs.

![Overview](./ReadmeFiles/topology.png)
![Auth Flow](./ReadmeFiles/auth-flow.png)

### Scenario

This sample shows how to build a Python web app using Flask and MSAL Python,
that signs in a user, and get access to Azure Databricks APIs.
For more information about how the protocols work in this scenario and other scenarios,
see [Authentication Scenarios for Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-scenarios).

## How to run this sample

To run this sample, you'll need:

> - [Python 2.7+](https://www.python.org/downloads/release/python-2713/) or [Python 3+](https://www.python.org/downloads/release/python-364/)


### Step 1:  Register the sample python application with your Azure Active Directory tenant

#### Choose the Azure AD tenant where you want to create your applications

As a first step you'll need to:

1. Sign in to the [Azure portal](https://portal.azure.com) using either a work or school account or a personal Microsoft account.
1. If your account is present in more than one Azure AD tenant, select your profile at the top right corner in the menu on top of the page, and then **switch directory**.
   Change your portal session to the desired Azure AD tenant.

#### Register the Python Webapp and Azure Databricks (aad-python-dash-app)

1. Navigate to the Microsoft identity platform for developers [App registrations](https://go.microsoft.com/fwlink/?linkid=2083908) page.
1. Select **New registration**.
1. When the **Register an application page** appears, enter your application's registration information:
   - In the **Name** section, enter a meaningful application name that will be displayed to users of the app, for example `aad-python-dash-app`.
   - Change **Supported account types** to **Accounts in any organizational directory and personal Microsoft accounts (e.g. Skype, Xbox, Outlook.com)**.
   - In the Redirect URI (optional) section, select **Web** in the combo-box and enter the following redirect URIs: `http://localhost:5000/getAToken`.
1. Select **Register** to create the application.
1. On the app **Overview** page, find the **Application (client) ID** value and record it for later. You'll need it to configure the Visual Studio configuration file for this project.
1. Select **Save**.
1. From the **Certificates & secrets** page, in the **Client secrets** section, choose **New client secret**:

   - Type a key description (of instance `app secret`),
   - Select a key duration of either **In 1 year**, **In 2 years**, or **Never Expires**.
   - When you press the **Add** button, the key value will be displayed, copy, and save the value in a safe location.
   - You'll need this key later to configure the project in Visual Studio. This key value will not be displayed again, nor retrievable by any other means,
     so record it as soon as it is visible from the Azure portal.
1. Create a Azure Databricks service resource in your desired resource group in Azure Portal
1. Select the **API permissions** section
   - Click the **Add a permission** button and then,
   - Ensure that the **APIs my organization uses** tab is selected
   - In the search box, type **AzureDatabricks**
   - In the **Delegated permissions** section, permissions are checked: **user_impersonation**.
   - Select the **Add permissions** button

### Step 3:  Configure the sample to use your Azure AD tenant

In the steps below, "ClientID" is the same as "Application ID" or "AppId".

#### Configure the python webapp project

> Note: if you used the setup scripts, the changes below may have been applied for you

1. Open the `app_config.py` file
1. Find the app key `Enter_the_Tenant_Name_Here` and replace the existing value with your Azure AD tenant name.
1. You saved your application secret during the creation of the `aad-python-dash-app` app in the Azure portal.
   Now you can set the secret in environment variable `CLIENT_SECRET`,
   and then adjust `app_config.py` to pick it up.
1. Find the app key `Enter_the_Application_Id_here` and replace the existing value with the application ID (clientId) of the `aad-python-dash-app` application copied from the Azure portal.


### Step 4: Run the sample

- You will need to install dependencies using pip as follows:
```Shell
$ pip install -r requirements.txt
```

Run app.py from shell or command line. Note that the host and port values need to match what you've set up in your redirect_uri:

```Shell
$ flask run --host localhost --port 5000
```

## More information

For more information about web apps scenarios on the Microsoft identity platform see [Scenario: Web app that calls web APIs](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/aad/app-aad-token#configure-an-app-in-azure-portal)
