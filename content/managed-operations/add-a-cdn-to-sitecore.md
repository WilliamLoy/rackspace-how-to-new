---
permalink: add-a-cdn-to-sitecore/
audit_date:
title: Add a CDN to Sitecore
type: article
created_date: '2017-05-31'
created_by: Juan Garza
last_modified_date: '2017-05-31'
last_modified_by: Nate Archer
product: Managed Operations
product_url: managed-operations
---

This article describes how to Add a CDN to Sitecore.

### Prerequisite

- Your login credentials for the Azure portal. For information about how to log in to the Azure portal, see [Sitecore Cloud portals and account management](/how-to/sitecore-cloud-portals-and-account-management/).

### Add a CDN service to your Azure account

1. Log in to the [Azure portal](https://portal.azure.com/).

2. Select **All Resources** from the left-hand navigation pane.

3. Click **Add** to create a new resource.

4. Select **New** > **Web + Mobile** > **CDN**.

5. Specify the the CDN Name, subscription, resource group and location, and the pricing tier for the CDN service you want to use.

6. Click **Create**.

### Create a Endpoint

1. Navigate to **CDN profile** in the Azure portal.

2. Select **Endpoint** to add an endpoint. Name the CDN endpoint you want to use.

3. Select **Origin Type** > **Web App**.

    **Note:** If you are using a custom domain you can select Custom Origin for the Origin Type and specify a url for your static content. This is useful for rewriting medialinks and exporting static content to another url. 

4. Select the Web App associated with your Sitecore site. Select the CDN endpoint from the drop down menu, and then click **Add**.

### Configure Sitecore to load static content from the CDN

<!---Still needs to be added--->
