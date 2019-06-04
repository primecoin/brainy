# Brainy

A Primecoin brain wallet adapted from brainwallet.io.

### Installation

```
git clone ssh://git@github.com/primecoin/brainy
cd brainy
pipenv shell
pipenv install zappa flask
pipenv install --dev awscli
```

Test locally:

```
flask run
```

By default the test server is located at `http://localhost:5000/`.

### Deployment

Amazon AWS deployment requires awscli.

```
zappa init
```

Add `certificate_arn` and `domain` settings to `zappa_settings.json`. To deploy the web service:

```
zappa deploy
zappa certify dev
```

To terminate the web service:

```
zappa undeploy
```
