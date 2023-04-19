import os

CLIENT_ID = "3161c04b-f7e0-43f9-a5d9-b884092c0941" # Application (client) ID of app registration

CLIENT_SECRET = "t-V8Q~u-fxq1dpEu7WdQMwUofx4XTHBJs3MHZaOm" # Placeholder - for use ONLY during testing.
# In a production app, we recommend you use a more secure method of storing your secret,
# like Azure Key Vault. Or, use an environment variable.

AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
# AUTHORITY = "https://login.microsoftonline.com/aad-python-dash-app"

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# Use an Azure AD access token to access the Databricks REST API
DATABRICKS_API_URL = "https://adb-6534618731103973.13.azuredatabricks.net/api/2.0/clusters/list" # This resource requires Azure AD admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
