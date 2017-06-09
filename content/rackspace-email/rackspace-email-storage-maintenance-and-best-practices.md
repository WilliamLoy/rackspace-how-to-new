---
permalink: rackspace-email-storage-maintenance-and-best-practices/
audit_date:
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

- **Tools required:**  Cloud Office Control Panel access

For more information about prerequisite terminology, see [Cloud Office support terminology](/how-to/cloud-office-support-terminology).



### Checking mailbox storage in the Cloud Office Control Panel

1.	Log in to the [Cloud Office Control Panel](https://cp.rackspace.com/Login.aspx?ReturnUrl=%2f "Cloud Office Control Panel") using your Rackspace Cloud Office admin ID and password.

2.	Select **Mailboxes** within the **Rackspace Email** section.

    <!--add screen shot file RSEstorageCPSC1.png-->

3.	If you have multiple domains, select the domain you wish to check storage for.

4. The fourth column in the mailbox list labeled **Usage** shows the amount of free space each user has.

Warning: If a mailbox is at max capacity, the mail sent during that time will be rejected and WILL NOT deliver after more mailbox space is created.

Note: The **Usage** column is not a real time reading of the mailbox storage. **Usage** updates once every 24 hours. Always reference the storage in apps.rackspace.com for real time storage.



It is important to check  the **Usage** for user to determine which users are nearing capacity. Below are recommendations for users nearing their storage capacity.

- Notify users near capacity and counsel them on archiving items to free up mailbox storage.

- If a user deletes an excessive number of emails, this change will take longer to process. Allow ample time for that deletion to be reflected.

- Email in the "Trash" folder DOES COUNT toward the storage of the mailbox. Follow the below steps to ensure a deleted message is not counting toward your mailbox storage.

     1. Move an unwanted message to **Trash**
     2. The message has been moved to the **Trash** folder. Delete the message from **Trash**.   
     3. The message no longer counts toward the mailbox storage. If you need to recover a message that you deleted from trash see [Recover delete email in Webmail](/how-to/recover-deleted-email-in-webmail/).

     Warning: Messages purged from the **Trash** folder can be recovered for up to 14 days after deletion. After 14 days the message cannot be recovered.

- **Consider Rackspace Email Archiving** to ensure that email traffic to and from your domain is archived going forward. [Enable email archiving: Cloud Office Control Panel](/how-to/enable-email-archiving-cloud-office-control-panel/).


### Checking mailbox storage in webmail

1. Log in to [apps.rackspace.com](https://apps.rackspace.com/index.php).

2. Click your username in the upper-right hand corner and the dropdown menu will show the current mailbox storage.

<!--add screen shot file RSEstorageWebmailSC1.png-->

Note: Consider the storage shown in [apps.rackspace.com](https://apps.rackspace.com/index.php) to be the authority for your storage available on the server.


### Mailbox storage best practices

- We recommend that all customers enable [**Rackspace Email Archiving**](/how-to/enable-email-archiving-cloud-office-control-panel/) for all domains.  Archiving locally poses risks that Rackspace is unable to assist our customers with.  

- Never store over 10,000 items in one folder, especially the **Inbox**.

- Audit your email for unneeded messages. For instance, if you know you will never need that Spam message for any reason, delete it.

- Set a schedule to archive email. For instance, "Every month I am going to archive any email over 2 years old". Regularly archiving mail not only protects your data in the event that you experience data loss, but it prevents mail performance issues by freeing up storage in the mailbox.

Note: Rackspace support cannot assist with archiving  your email locally.

- Generally speaking, the less mail you store in your mailbox the less likely you are to experience performance issues. If your mailbox max capacity is 25 GB, and you regularly store 24 GB in it, you might experience performance issues.

- If you archive or delete messages on your [local mail client](/how-to/cloud-office-support-terminology/#cloud-office-terminology) log into [apps.rackspace.com](https://apps.rackspace.com/index.php) to make certain that those changes are reflected in webmail.

Note: Consider the storage shown in [apps.rackspace.com](https://apps.rackspace.com/index.php) to be the authority for mailbox storage available on the server.
