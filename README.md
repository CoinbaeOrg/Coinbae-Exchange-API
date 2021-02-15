# Coinbae Exchange API
## API

[HTTP Protocol](https://github.com/CoinbaeOrg/Coinbae-Exchange-API/HTTP-Protocol.md) and [Websocket Protocol](https://github.com/CoinbaeOrg/Coinbae-Exchange-API/WebSocket-Protocol.md) documents are available in English. 

### Third-party Clients

- [Python3 API realisation](https://github.com/CoinbaeOrg/Coinbae-Exchange-API/python-api)
- [Ruby Gem 💎](https://github.com/CoinbaeOrg/Coinbae-Exchange-API/ruby-api)

## Authorization

The websocket protocol has an authorization method (`server.auth`) which is used to authorize the websocket connection to subscribe to user specific events (trade and balance events).

To use this method you need to get an authorization token:

* method: `auth.login`
* params: 
1. login: user login, String
2. password: user password，String
3. otp: user One Time Password，String

* example: 

```
"id":1
"method": "auth.login"
"params": ["login", "password", "123456"]
```

Example response: 
`{
Result	"Success"
Status	1
Userid	"asd123asd123asd123asd123asd123asd123asd123asd123asd123asd123"
`
