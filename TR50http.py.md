# TR50http.py

*   [Class Attributes](#Class-Attributes)
*   [Class Methods](#Class-Methods)
  *   [__init__](#__init__)
  *   [app_auth](#app_auth)
  *   [auth](#auth)
  *   [debug](#debug)
  *   [execute](#execute)
  *   [get_options](#get_options)
  *   [get_response](#get_response)
  *   [post](#post)
  *   [set_json_auth](#set_json_auth)
  *   [user_auth](#user_auth)

# Class Attributes

<table>
  <tbody>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>appId</td>
      <td>String</td>
      <td> </td>
      <td>The application identifier you will be using.</td>
    </tr>
    <tr>
      <td>app_token</td>
      <td>String</td>
      <td> </td>
      <td>This application appToken.</td>
    </tr>
    <tr>
      <td>endpoint</td>
      <td>String</td>
      <td> </td>
      <td>The API endpoint for POSTing (e.g. https://www.example.com/api).</td>
    </tr>
    <tr>
      <td>error</td>
      <td>Array</td>
      <td>[ ]</td>
      <td>Holds any error returned by the api.</td>
    </tr>
    <tr>
      <td>last_received</td>
      <td>String</td>
      <td> </td>
      <td>Last JSON string received from the endpoint. Used when debugging.</td>
    </tr>
    <tr>
      <td>last_sent</td>
      <td>String</td>
      <td> </td>
      <td>Last JSON string sent to the endpoint. Used when debugging.</td>
    </tr>
    <tr>
      <td>last_status</td>
      <td>Boolean</td>
      <td>None</td>
      <td>If the last request succeeded or failed.</td>
    </tr>
    <tr>
      <td>password</td>
      <td>String</td>
      <td> </td>
      <td>The password used to connect to the server.</td>
    </tr>
    <tr>
      <td>response</td>
      <td>Dictionary</td>
      <td>[ ]</td>
      <td>Holds the response data from the api call.</td>
    </tr>
    <tr>
      <td>session_id</td>
      <td>String</td>
      <td> </td>
      <td>Holds the current session identifier.</td>
    </tr>
    <tr>
      <td>thing_key</td>
      <td>String</td>
      <td> </td>
      <td>The thing key used to identify the application.</td>
    </tr>
    <tr>
      <td >username</td>
      <td >String</td>
      <td> </td>
      <td>The username used to connect to the server.</td>
    </tr>
  </tbody>
</table>

# Class Methods

## __init__

TR50http.__init__([options])

Initialize the object. Authenticates if no session is defined or if a TR50 diag.ping() test fails.

### Parameters

<table>
  <tbody>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>options</td>
      <td>Dictionary</td>
      <td>No</td>
      <td>{ }</td>
      <td>A dictionary used to initialize the object.</td>
    </tr>
  </tbody>
</table>

#### option keys

<table>
  <tbody>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>endpoint</td>
      <td>String</td>
      <td>No</td>
      <td></td>
      <td>The API endpoint for POSTing (e.g. https://www.example.com/api).</td>
    </tr>
    <tr>
      <td>app_id</td>
      <td>String</td>
      <td>No</td>
      <td></td>
      <td>The application identifier to used when authenticating as an application.</td>
    </tr>
    <tr>
      <td>app_token</td>
      <td>String</td>
      <td>No</td>
      <td></td>
      <td>The application appToken to use when authenticating as an application.</td>
    </tr>
    <tr>
      <td>thing_key</td>
      <td>String</td>
      <td>No</td>
      <td></td>
      <td>The thing key used to identify the application if authenticating as an application.</td>
    </tr>
    <tr>
      <td>username</td>
      <td>String</td>
      <td>No</td>
      <td></td>
      <td>The username used to connect to the server if authenticating as a user.</td>
    </tr>
    <tr>
      <td>password</td>
      <td>String</td>
      <td>No</td>
      <td></td>
      <td>The password used to connect to the server if authenticating as a user.</td>
    </tr>
    <tr>
      <td>sessionId</td>
      <td>String</td>
      <td>No</td>
      <td></td>
      <td>It is possible to reuse sessionIds between executions of the application that uses the library.</td>
    </tr>
  </tbody>
</table>

### Return

None.

* * *

## app_auth

Boolean = TR50http.app_auth(app_id, app_token, thing_key[, update_session_id])

Authenticate the application.

### Parameters

<table>
  <tbody>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>appI_id</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The application ID.</td>
    </tr>
    <tr>
      <td>app_token</td>
      <td>String</td>
      <td>Yes</td>
      <td> </td>
      <td>The application token.</td>
    </tr>
    <tr>
      <td>thing_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The key of the application's thing.</td>
    </tr>
    <tr>
      <td>update_session_id</td>
      <td>Boolean</td>
      <td>No</td>
      <td>True</td>
      <td>Update the object session ID.</td>
    </tr>
  </tbody>
</table>

### Return

Success or failure to authenticate.

* * *

## auth

Boolean = TR50http.auth()

Depending on the configuration, authenticate as an application or as a user. Prefer authentication as an application.

### Parameters

None.

### Return

Success or failure to authenticate.

* * *

## debug

Dictionary = TR50http.debug()

After a command is executed, this method returns an array of debugging information about the object and the last command.

### Parameters

None.

### Return

Returns a dictionary that contains values from the object: endpoint, last_sent, last_received, and error.

* * *

## execute

Boolean = TR50http.execute(command[, params])

Package the command and the params into an array and sends the command to the configured endpoint for processing.

### Parameters

<table>
  <tbody>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>command</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The TR50 command to execute.</td>
    </tr>
    <tr>
      <td>params</td>
      <td>Dictionary</td>
      <td>No</td>
      <td>False</td>
      <td>The array of command parameters.</td>
    </tr>
  </tbody>
</table>

### Return

Success or failure to post.

* * *

## get_options

Dictionary = TR50http.get_options()

Returns a dictionary of the options set in the object. Useful for initializing a new object.

### Parameters

None.

### Return

Returns a dictionary that contains values from the object: endpoint, session_id, app_id, app_token, thing_key, username, and password.

* * *

## get_response

Dictionary = TR50http.get_response()

Return the response data for the last command if the last command was successful.

### Parameters

None.

### Return

The response data for the last command (if the command was successful).

* * *

## post

Boolean = TR50http.post(json_string)

This method sends the TR50 request to the server and parses the response.

### Parameters

<table>
  <tbody>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>json_string</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The JSON command and arguments. This parameter can also be an array that will be converted to JSON.</td>
    </tr>
  </tbody>
</table>

### Return

Success or failure to post.

* * *

## set_json_auth

String = TR50http.set_json_auth(json)

This method checks the JSON command for the auth parameter. If it is not set, it adds it.

### Parameters

<table>
  <tbody>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>json</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>A JSON string or the array representation of JSON.</td>
    </tr>
  </tbody>
</table>

### Return

A JSON string with the auth parameter.

* * *

## user_auth

Boolean = TR50http.user_auth(username, password[, update_session_id])

Authenticate a user.

### Parameters

<table>
  <tbody>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Required</th>
      <th>Default</th>
      <th>Description</th>
  </tr>
  <tr>
    <td>username</td>
    <td>String</td>
    <td>Yes</td>
    <td></td>
    <td>The username used if authenticating as a user.</td>
  </tr>
  <tr>
    <td>password</td>
    <td>String</td>
    <td>Yes</td>
    <td>Y</td>
    <td>The password used if authenticating as a user.</td>
    </tr>
    <tr>
      <td>update_session_id</td>
      <td>Boolean</td>
      <td>No</td>
      <td>True</td>
      <td>Update the object session ID.</td>
    </tr>
  </tbody>
</table>

### Return

Success or failure to authenticate.
