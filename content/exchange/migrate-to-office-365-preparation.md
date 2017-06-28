---
permalink: migrate-to-office-365-preparation/
audit_date:
title: Migrate to Office 365
type: article
created_date: '2017-06-28'
created_by: William Loy
last_modified_date: '2017-06-28'
last_modified_by: William Loy
product: Microsoft Exchange
product_url: exchange
---
Add Office 365 subscriptions at Rackspace Cloud Office.

### Prerequisites

- **Applies to:** Administrator
- **Difficulty:** Moderate
- **Time needed:** Approximately 1-2 hours
- **Tools required:** Cloud Office Control Panel access, an Office 365 tenant with Rackspace Cloud Office

For more information about prerequisite terminology, see [Cloud Office support terminology](/how-to/cloud-office-support-terminology/).


### Compare Microsoft Exchange against Office 365

|Feature | Microsoft Exchange | Office365 Business | Office365 Business Essentials | Office365 Business Premium
|---|---|---|---|---|
|**Shared Environment Limitations**| YES |  | NO | NO |
|**Transport rules**| Max: 2 | | No Limit | No Limit |
|**Shared mailboxes**| | |&#10003; |&#10003;|
|**Sharepoint** |2007 | | 2016| 2016|
|**Exchange email** | &#10003;| |&#10003;|&#10003;|
|**Online Microsoft Office Suite** | | &#10003; |&#10003; |&#10003;|
|**Desktop Microsoft Office Suite and 1 TB One Drive** | Optional |&#10003;| |&#10003; |
|**Skype for Business** | &#10003; Internal Users||&#10003;Internal Users|&#10003; Internal Users and External Users |

### Prepare to migrate from Microsoft Exchange to Office 365

1. Create your Office 365 tenant

2. Create a list of users that you plan to migrate.

3. Add the applicable Office 365 license for every user you plan to migrate. See [Add an Office 365 License](/how-to/add-an-office-365-subscription) for instructions.

3. Create those users in your [Office 365 portal](portal.office.com).

4. Migrate your data from Microsoft Exchange to Office 365.

   - You can request an assisted migration at this point
   - Alternatively you can [self-migrate using Migration Wiz](/how-to/migrate-your-email-by-using-the-self-service-migration-tool/) 

5. Once you are ready for email to be directed to your Office 365 mailboxes, update your domain's DNS to start directing email to Office 365.

6. Migrate new data from the old Microsoft Exchange mailboxes.

7. Remove the Microsoft Exchange mailboxes from your Cloud Office Account and contact support to update your billing.
