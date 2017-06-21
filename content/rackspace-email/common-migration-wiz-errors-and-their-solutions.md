---
permalink: common-migration-wiz-errors-and-their-solutions/
audit_date:
title: Common Migration Wiz errors and their solutions
type: article
created_date: '2017-06-21'
created_by: William Loy
last_modified_date: '2017-06-21'
last_modified_by: William Loy
product: Rackspace Email
product_url: rackspace-email
---
Common Migration Wiz errors and their solutions.

### Prerequisites

- **Applies to:** Administrator
- **Difficulty:** Challenging
- **Time needed:** Approximately 1-2 hours
- **Tools required:** Access to the Migration Wizard session

For more information about prerequisite terminology, see [Cloud Office support terminology](/how-to/cloud-office-support-terminology/).

If you have not yet started a Migration Wiz session, follow these instructions to get started [Migrating your email using the Self-Service Migration Tool](/how-to/migrate-your-email-by-using-the-self-service-migration-tool/) migrating your migrating your email.

Error:

`Test migration failing: "Your migration failed checking source credentials. [AUTHENTICATIONFAILED] Invalid username or password." when migrating from Yahoo, Outlook.com, Windows Live, Hotmail`

Resolution:

- Verify the credentials are correct by logging in through the OWA URL (apps.rackspace.com) for the destination mailbox and then confirm the source credentials by logging into the account with your current email host such as Yahoo, Outlook.com, etc. Verify your migrating the mailboxes and not the aliases.

- When you try signing in, are you prompted to send a security code to enter? If so, you have two-factor authentication which will not allow Migration Wiz to complete a  migration.

Note: Accounts at Yahoo, Outlook.com, Windows Live, Hotmail usually have a default two-factor authentication system in place. You likely will not know you have two-factor authentication enabled. This two-factor authentication will prevent a migration from proceeding; Migration Wiz is unable to  authenticate two factor authentication.
