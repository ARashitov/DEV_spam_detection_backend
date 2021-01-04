# API endpoints:

## **/fit** (GET)

Performs model training and overrides previous one. Uses train and test matrix in data/ project dir.

## **/predict** (POST)

Performs prediction: if email message is spam?

### *NOTE*: Requires field `email_content` in message body

No any additinal parameters!!!
