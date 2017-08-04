# Sample Python TR50 HTTP Library

The purpose of this sample Python TR50 HTTP library is show how a Python
developer would rapidly develop web based and command line applications
that communicate with the Telit IoT Portal using the TR50 specification.

To use the library, you must have:
  1. Access to the management portal.
  2. A Python 2.6+ environment.
  3. The httplib2 package.
  4. The simplejson package.

## Installation, Configuration, and Authentication

The `tr50` package must be located in the file system so that the application
can import the modules. Second, the application must import the modules. The
final step before using the features of the library, is to create an object of
the `TR50http` class with the appropriate configuration and authentication
settings.

### Configuration and Authentication

There are two configuration options for authentication in the library. You may
configure the library to authenticate as a user by using a username and
password, the other is to configure the library to authenticate as an
application/thing.

For example, to configure and authenticate as a user:

```python
from tr50 import TR50http
config = {
    "endpoint" : "https://www.example.com/api",
    "username" : "jane.doe@example.com",
    "password" : "thePassword"
}
tr50http = TR50http.TR50http(config)
```

To configure and authenticate as an application/thing:

```python
from tr50 import TR50http
config = {
    "endpoint"  : "https://www.example.com/api",
    "app_id"    : "My Application",
    "app_token" : "abcdef123456wxyz",
    "thing_key" : "theThingKey"
}
tr50http = TR50http.TR50http(config)
```

Once properly configured, the library will automatically authenticate and the
object can be immediately used.

#### User Authentication

This can be used to limit access to an application by forcing a user to
supply this information before using the software. If the application executes
without user intervention or if the user is not required to log in, you should
use application authentication.

The following configuration options are required by the library:
  1. endpoint (the Telit IoT Platform API endpoint)
  2. username (the username/email address of the user)
  3. password (the password of the user)

The Telit IoT Platform API endpoint can be found by logging into the Management
Portal, and clicking on the *Developer* section. There are five endpoints
available. This library can use either the **HTTP** or **HTTPS** endpoint.

The username and password are the credentials used by a user to log into the
management portal.

#### Application/Thing Authentication

The following configuration options are required by the library:
  1. endpoint (the Telit IoT Platform API endpoint)
  2. app_id (the application ID)
  3. app_token (the application token)
  4. thing_key (the thing key)

The Telit IoT Platform API endpoint can be found by logging into the Management
Portal, and clicking on the *Developer* section. There are five endpoints
available. This library can use either the **HTTP** or **HTTPS** endpoint.

The app_id is a unique value that is generated by the device and kept secret.
It is associated with the thing key the first time a device connects and
prevents "spoofing" connections. A good practice is to generate an
application ID the first time a device connects and store the value in
non-volatile memory so it can be re-used. Using a different application ID will
prevent an application from connecting.

The app_token is a string generated by the Telit IoT Platform that identifies
the application to the Telit IoT Platform as being valid. To generate an
app_token, go to the *Developer* section within the management portal and select
the *Applications* option from the left side menu. In the *Applications* screen,
click *New Application*. On the *New application* screen, provide a name for the
application, select the *Auto Registration Thing Definition ID*, and the the
*Role* that the has the permissions the application must have to function
properly for your needs. The other options that are present on the screen are
explained in detail in the *management portal User's and Administrator's Guide*
section within the help documentation. The link to the help documentation would
have been sent to you in the registration completion email and is referenced in
the *Help* section of the management portal. Finally, click *Add* to create the
application. The app_token is alphanumeric string labeled **Token**.

The thing_key is the unique key that associates the application to a particular
thing in the Telit IoT Platform. To get a thing_key, go to the *Things* section
within the management portal and select *New Thing*. On the *Adding thing*
screen, select the *Thing Definition*, enter an alphanumeric string for the
*Key* (this will become the thing_key), enter a name for the application
(this can be the same as the app_id). Finally, click *Add* to create the thing.
The thing_key is the alphanumeric string labeled **Key**.

## Using the Library

Once the new TR50 library object has been instantiated and configured, it is
now ready to process commands. The primary methods for interacting with this
library are `tr50http.execute()` and `tr50http.get_response()`.

The `tr50http.execute()` method takes two parameters: the command to execute
and (optionally) the parameters to be sent along with the command (if any are
required). Once the method completes, it will return a boolean value of true if
the command was transmitted successfully. The `tr50http.execute()` method
encapsulates the process to create the JSON string that is transmitted to the
Telit IoT Platform API endpoint. The list of available services, commands, and
parameters can be found at
http://help.devicewise.com/display/M2MOpen/M2M+Service+Interface

For example, the following code will send the command to list the first ten
thing definitions:

```python
result = tr50http.execute("thing_def.list", { "offset" : 0, "limit" : 10 });
```

The `tr50http.get_response()` method returns an array of the response to the
last command sent. It will have a success key for the status of the command,
and a key labeled params for the data returned by the command. If the last
command fails to transmit, this method will return a null value.

For example:

```python
response = tr50http.get_response();
```

Additionally, the method `tr50http.debug()` is a useful method that returns
the endpoint used by the library, the JSON string of the last command sent, the
JSON string of the response to the last command sent, and any error messages
returned. The information this method returns can be used for debugging the
connection or configuration, debugging an individual command, or to log/audit
usage (transmissions and responses).

It is also possible to construct and transmit the JSON command to the endpoint
manually. To do so, you would use the `tr50http.post()` method. It takes one
parameter, the JSON string. Using this method, it is possible to send several
M2M Service Interface command methods to the endpoint in one post method call.
The `tr50http.response` attribute will contain an array of the results of all
commands sent in the previous `tr50http.post()`.

## The TR50httpWorker Class

A subclass of the `TR50http` class is also available. It is located in the file
`tr50httpWorker.py`. It provides a compact interface to execute certain M2M
Service Interface command methods encapsulating parameter specification,
variable validation, error handling, and simplification of return structure.

The `TR50httpWorker` class is instantiated in the same manner as the
`TR50http` class (application authentication shown below, user authentication
is also possible):

```python
from tr50 import TR50httpWorker
config = {
    "endpoint"  : "https://www.example.com/api",
    "app_id"    : "My Application",
    "app_token" : "abcdef123456wxyz",
    "thing_key" : "theThingKey"
}
tr50httpWorker = TR50httpWorker.TR50httpWorker(config)
```

In addition to the core functions of the `TR50http` class, the
`TR50httpWorker` class provides methods for the following commonly used
service commands (method in parenthesis):
  * email.send (email_send)
  * locale.get (locale_get)
  * locale.list (locale_list)
  * locale.set (locale_set)
  * location.current (location_current)
  * location.decode (location_decode)
  * location.encode (location_encode)
  * location.publish (location_publish)
  * location.speedlimit (location_speedlimit)
  * location.weather (location_weather)
  * method.exec (method_exec)
  * org.find (org_find)
  * org.list (org_list)
  * property.aggregate (property_aggregate)
  * property.current (property_current)
  * property.publish (property_publish)
  * session.info (session_info)
  * session.org.list (session_org_list)
  * session.org.switch (session_org_switch)
  * thing_def.find (thing_def_find)
  * thing_def.list (thing_def_list)
  * thing.find (thing_find)
  * thing.list (thing_list)
  * twilio.sms.send (twilio_sms_send)
  * user.find (user_find)
  * user.list (user_list)

Although all of these methods are available in the `TR50httpWorker` class, the
software using an instance of this object will be limited to the methods that
the software has access to. If the software is authenticated as a user, the
software will only be able to successfully call methods available to the role
associated with the user. If the software is authenticated as an application,
the software will only be able to successfully call methods available to the
role associated with the application.

# License

The MIT License (MIT)

Copyright 2017 Telit

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
