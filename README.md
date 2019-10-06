# jwt-ouath-salesforce
The simple python to call jwt beare token between server and salesforce.

# How to Use :hatching_chick:
**1**. To use this script, install PIP **PyJWT** https://pypi.org/project/PyJWT/ and PIP **cryptography** https://pypi.org/project/cryptography/, These libraries are used to create the correct signature between client and server.

**2**. You need connected App in your Salesforce organization and a certification SHA256. upload de certification .cert in you Salesforce connected app and .key is the file to the script to use for signature verification.

**3**. Script result is the output of a Json with authorization code, which can be used in many types API consumptions.

**Example:** :facepunch:

`{"access_token":"00Dxx0000001gPL!AR8AQJXg5oj8jXSgxJfA0lBog.
39AsX.LVpxezPwuX5VAIrrbbHMuol7GQxnMeYMN7cj8EoWr78nt1u44zU31
IbYNNJguseu","scope":"web openid api id","instance_url":"
https://yourInstance.salesforce.com","id":"
https://yourInstance.salesforce.com
/id/00Dxx0000001gPLEAY/005xx000001SwiUAAS","token_type":"Bearer"}`

On some servers, where it is not possible to perform authorization via the web, this authentication model is useful, especially since we do not have to risk exposing user data, such as username, password and token. Example: Continous Integration (Jenkins CI, Travis...etc) :wink:

If you have any suggestions, feel free to comment! :smiley:
