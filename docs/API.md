# **API endpoints**

## GET `/fit`

Updates model within docker container by using data present inside, so no any parameters are required!

## POST `/predict`

Spam prediction endpoint

### **Request body**

```Python
{
    'email_content': 'Hello this is the test message!'
}
```

### **Response body**

```Python
{
    'email_content': 'Hello this is the test message!',
    'is_spam': False
}
```
