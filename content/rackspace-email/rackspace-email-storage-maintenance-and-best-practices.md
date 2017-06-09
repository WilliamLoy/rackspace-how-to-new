---
permalink: rackspace-email-storage-maintenance-and-best-practices/
audit_date: '2017-02-24'
title: Rackspace Email storage maintenance and best practices
type: article
created_date: '2017-06-08'
created_by: William Loy
last_modified_date: '2017-06-09'
last_modified_by: William Loy
product: Rackspace Email
product_url: rackspace-email
---

This article explains how to monitor user storage in your Cloud Office Control Panel as well as best practices for mailbox storage.

### Prerequisites

- **Applies to:** Administrator

- **Difficulty:** Moderate

- **Tools required:**  Cloud Office Control Panel access

For more information about prerequisite terminology, see [Cloud Office support terminology](/how-to/cloud-office-support-terminology).


Knowing the storage status of your users is paramount to effective account administration.

### Checking mailbox storage in the Cloud Office Control Panel

1.	Log in to the [Cloud Office Control Panel](https://cp.rackspace.com/Login.aspx?ReturnUrl=%2f "Cloud Office Control Panel") using your Rackspace Cloud Office admin ID and password.

2.	Select **Mailboxes** within the **Rackspace Email** section.

    <!--add screen shot file AddmailboxSC1.png-->

3.	If you have multiple domains, select the domain you wish to check storage for.

4. The fourth column in the mailbox list labeled **Usage** shows the amount of free space each user has.

Note: The **Usage** column is not a real time reading of the mailbox storage. **Usage** updates once every 24 hours.

It is important to check  the **Usage** for user to determine which users are nearing capacity. Below are recommendations for users nearing their storage capacity.

Warning: If a mailbox shows at being max capacity, that mailbox will not receive incoming mail. The mail sent during that time will be rejected and WILL NOT deliver after more mailbox space is created.

- Notify users near capacity and counsel them on archiving items to free up mailbox storage.

- If a user deletes an excessive number of emails, this change will take longer to process. Allow ample time for that deletion to be reflected.

- Email in the "Trash" folder does count toward the storage of the mailbox.


### Mailbox storage best practices

- Regularly back up your email data to an external drive.

- Generally speaking, the less mail you store in your mailbox the more effective it will perform. If you mailbox max capacity is 25 GB, and your regularly store 24 GB in it, the mailbox will experience performance issues like slow load times.

- Never have over 10,000 items in one folder.

- Set a schedule to archive email. For instance, "I am going to archive any email over 2 years old".

- Audit your email for unneeded messages. For instance, if you know you will never need that Spam message for any reason, delete it.

- If you archive or delete messages on your local [mail client]() log into [apps.rackspace.com]() to make certain that those changes are reflected in webmail.

Note: Consider the storage shown in apps.rackspace.com to be the authority for your storage available on the server.
