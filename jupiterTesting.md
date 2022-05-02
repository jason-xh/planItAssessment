* Security
    * injection attacks
    * cart page is fine when quantity is tested with payload ` '";<lol/>../—#`ls` `, but when inputting large quantity then putting payload the cart page breaks
* Phone #
    * putting spaces, does the site format it properly?
    * is it restricted to only aus numbers?
    * input a longer phone number, some countries have long numbers
* Unexpected inputs
    * inputting numbers when string expected
    * inputting string/float/negative numbers where integer expected
    * test email regex with odd emails
* Large numbers/strings
    * Large numbers the site should be able to handle
    * test message length