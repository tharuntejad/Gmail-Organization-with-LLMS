
# Categories into which you want to classify your emails(should be altered as per your requirements)
categories = {
    "Personal": "Emails from friends, family, and personal contacts.",
    "Social":  "Notifications from social media platforms.",
    "Promotions":  "Emails from online services, tech companies, apps, and general promotions.",
    "Finance Promotions": "Financial and insurance-related promotions and general updates.",
    "Verifications": "Time-sensitive emails with OTPs, verification codes, dont include statements, invoices,  bills.",
    "Finances": "Emails related to bank statements, bills, receipts and financial transactions.",
    "Reminders": "Emails related to reminders, to-do lists, calendar events, end of service information.",
    "Work":  "Emails related to your job or profession, including project updates and meeting invitations.",
    "Spam":  "Unsolicited and irrelevant emails.",
    "Support": "Emails regarding customer support or service inquiries."
  }

# Define the actions to be taken for each category (should be altered as per your requirements)
# ON - Enable the action, OFF - Disable the action
category_actions = {
    "Personal": {
      "auto-delete": "OFF",        # move a mail to bin
      "auto-sort": "ON",           # move a mail to a specific folder
      "remove-after-sort": "ON",   # remove a mail from inbox after sorting(only if auto-sort is ON), recommend ON
      "auto-read": "OFF"           # mark a mail as read
    },
    "Social": {
      "auto-delete": "OFF",
      "auto-sort": "ON",
      "remove-after-sort": "ON",
      "auto-read": "OFF"
    },
    "Promotions": {
      "auto-delete": "OFF",
      "auto-sort": "ON",
      "remove-after-sort": "ON",
      "auto-read": "ON"
    },
    "Finance Promotions": {
      "auto-delete": "OFF",
      "auto-sort": "ON",
      "remove-after-sort": "ON",
      "auto-read": "ON"
    },
    "Verifications": {
      "auto-delete": "OFF",
      "auto-sort": "ON",
      "remove-after-sort": "ON",
      "auto-read": "OFF"
    },
    "Finances": {
        "auto-delete": "OFF",
        "auto-sort": "ON",
        "remove-after-sort": "ON",
        "auto-read": "OFF"
    },
    "Reminders": {
      "auto-delete": "OFF",
      "auto-sort": "ON",
      "remove-after-sort": "ON",
      "auto-read": "OFF"
    },
    "Work": {
      "auto-delete": "OFF",
      "auto-sort": "ON",
      "remove-after-sort": "ON",
      "auto-read": "OFF"
    },
    "Spam": {
      "auto-delete": "OFF",
      "auto-sort": "ON",
      "remove-after-sort": "ON",
      "auto-read": "ON"
    },
    "Support": {
      "auto-delete": "OFF",
      "auto-sort": "ON",
      "remove-after-sort": "ON",
      "auto-read": "OFF"
    }
  }

# Map custom labels with default Gmail labels to avoid redundancy
# You cannot access Categories/Social-Promotions-Updates-Forums as they are not exposed
# to imap so create your own labels with identical names (you cannot use the same name as the default Gmail labels)

# Default Gmail labels that are available by default (do not change)
default_gmail_labels = [
    'INBOX',
    '[Gmail]/All Mail',
    '[Gmail]/Bin',
    '[Gmail]/Drafts',
    '[Gmail]/Important',
    '[Gmail]/Sent Mail',
    '[Gmail]/Spam',
    '[Gmail]/Starred'
]

# Custom labels to be created in  Gmail (should be altered as per your requirements)
custom_labels = [
    "@ Personal",
    "@ Social",
    "@ Promotions",
    "@ Verifications",
    "@ Finances",
    "@ Reminders",
    "@ Work",
    "@ Support"
]

# Define where each category should be moved to
category_mapper = {
    "Personal": "@ Personal",                  # custom label
    "Social":  "@ Social",                     # custom label
    "Promotions":  "@ Promotions",             # custom label
    "Finance Promotions": "@ Promotions",      # custom label
    "Verifications": "@ Verifications",        # custom label
    "Finances": "@ Finances",                  # custom label
    "Reminders": "@ Reminders",                # custom label
    "Work":  "@ Work",                         # custom label
    "Spam":  "[Gmail]/Spam",                   # default label
    "Support": "@ Support"                     # custom label
}

# Test's to check if the categories, category_actions, category_mapper, default_gmail_labels, custom_labels
if __name__ == "__main__":
    # Test whether actions are defined for each category
    assert set(categories.keys()) == set(category_actions.keys()), "Actions are not defined for each category"
    print("Actions are defined for each category")

    # Test whether every category has a target folder
    assert set(categories.keys()) == set(category_mapper.keys()), "Target folder is not defined for some categories"
    print("Target folder is defined for each category")

    # Test whether target folders exist in default Gmail labels or custom labels
    for category, target_folder in category_mapper.items():
        assert target_folder in default_gmail_labels or target_folder in custom_labels, f"Target folder {target_folder} does not exist in default Gmail labels or custom labels"
    print("All target folders found in either in default Gmail labels or custom labels")

    print("All tests passed!")
