---
permalink: prepare-mac-users-for-rackspace-email-to-microsoft-exchange-migration/
audit_date:
title: Prepare Mac users for Rackspace Email to Microsoft Exchange migration.
type: article
created_date: '2017-06-22'
created_by: Maggie Serrano
last_modified_date: '2017-06-22'
last_modified_by: William Loy
product: Rackspace Email
product_url: rackspace-email
---
Prepare Mac users to migrate  from Rackspace Email to Microsoft Exchange.

### Prerequisites

- **Applies to:** Administrator and User
- **Difficulty:** Moderate
- **Time needed:** Approximately 30 minutes
- **Tools required:** Mac computer, apps.rackspace.com access

For more information about prerequisite terminology, see [Cloud Office support terminology](/how-to/cloud-office-support-terminology/).

Mac users require special attention when migrating from Rackspace Email to Microsoft Exchange. This is because Apple Mail interacts with IMAP and POP connections
in such a way that does not translate properly to Microsoft Exchange.

Before beginning, always log into apps.rackspace.com to verify that all email data is stored in your mailbox on the server. If it is not, you are at risk of data loss
and should contact your Administrator to troubleshoot syncing your mail up to apps.rackspace.com.

### Create a backup by exporting the mailbox:

1. Select your mailbox within Apple Mail

2.  Select **Export Mailbox**

3.  Choose a folder or create a new folder, then click **Choose** as the destination of the export.

4.  Once location is selected, the export or backup will be stored where selected.

Note: Apple Mail exports the mailboxes as **.mbox** packages. If you previously exported a mailbox, Apple Mail doesn't overwrite the existing **.mbox** file; it creates
a new **.mbox** file, such as **My Mailbox 3.mbox**.

### Once the backup is created, proceed to remove your mailbox from Apple Mail.

1.  Click on the **IMAP** to be removed.

    Warning: Always double-check  that you are selecting the correct account. Repeat the steps to back up the mailbox if you are not certain the backup was successful. If the account is listed as POP instead of IMAP you should be absolutely certain the back up was successful before proceeding. If it was not the data will be unrecoverable.

2.  Click on the **Minus sign(-)** sign on the bottom of the window.

3.  Click **OK**


Once the mailbox has been removed, and your account is ready for migration, reboot your Mac so your device is ready to re-add your account after your migration is completed.

For steps on adding your Exchange mailbox post migration, please visit our email help tool at https://emailhelp.rackspace.com.
