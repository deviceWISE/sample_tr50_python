# TR50httpWorker.py

*   [Class Methods](#TR50httpWorker.py-ClassMethods)
    *   [__init__](#TR50httpWorker.py-__init__)
    *   [tr50_date_format](#TR50httpWorker.py-tr50_date_format)
    *   [email_send](#TR50httpWorker.py-email_send)
    *   [locale_get](#TR50httpWorker.py-locale_get)
    *   [locale_list](#TR50httpWorker.py-locale_list)
    *   [locale_set](#TR50httpWorker.py-locale_set)
    *   [location_current](#TR50httpWorker.py-location_current)
    *   [location_decode](#TR50httpWorker.py-location_decode)
    *   [location_encode](#TR50httpWorker.py-location_encode)
    *   [location_publish](#TR50httpWorker.py-location_publish)
    *   [location_speedlimit](#TR50httpWorker.py-location_speedlimit)
    *   [location_weather](#TR50httpWorker.py-location_weather)
    *   [method_exec](#TR50httpWorker.py-method_exec)
    *   [org_find](#TR50httpWorker.py-org_find)
    *   [org_list](#TR50httpWorker.py-org_list)
    *   [property_aggregate](#TR50httpWorker.py-property_aggregate)
    *   [property_current](#TR50httpWorker.py-property_current)
    *   [property_publish](#TR50httpWorker.py-property_publish)
    *   [session_info](#TR50httpWorker.py-session_info)
    *   [session_org_list](#TR50httpWorker.py-session_org_list)
    *   [session_org_switch](#TR50httpWorker.py-session_org_switch)
    *   [thing_def_find](#TR50httpWorker.py-thing_def_find)
    *   [thing_def_list](#TR50httpWorker.py-thing_def_list)
    *   [thing_find](#TR50httpWorker.py-thing_find)
    *   [thing_list](#TR50httpWorker.py-thing_list)
    *   [twilio_sms_send](#TR50httpWorker.py-twilio_sms_send)
    *   [user_find](#TR50httpWorker.py-user_find)
    *   [user_list](#TR50httpWorker.py-user_list)

# Class Methods

## __init__

TR50httpWorker.__init__([options])

Initialize the object, calls the constructor for the super class.

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
      <td>Array </td>
      <td>No</td>
      <td>{ }</td>
      <td>A dictionary key value pairs used to initialize the object.</td>
    </tr>
  </tbody>
</table>

#### options keys

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
      <td>appId</td>
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
      <td>session_id</td>
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

## tr50_date_format

String = TR50httpWorker.tr50_date_format(date_obj)

Convert a date object to TR50 formatted string.

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
      <td>date_obj</td>
      <td>Object</td>
      <td>Yes</td>
      <td></td>
      <td>The date object to reformat.</td>
    </tr>
  </tbody>
</table>

### Return

The date formatted in the style that TR50 requires.

* * *

## email_send

Boolean = TR50httpWorker.email_send(email_to, email_from, email_subject, email_body)

[email.send](https://help.devicewise.com/display/ARG/email.send) sends an email to one or more email addresses from a registered user's email address in the M2M Service.

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
      <td>email_to</td>
      <td>Mixed</td>
      <td>Yes</td>
      <td></td>
      <td>A single email address: 'john.doe@example.com', or an array containing the recipients of the email: ['john.doe@example.com', 'jane.doe@example.com'].</td>
    </tr>
    <tr>
      <td>email_from</td>
      <td>Mixed</td>
      <td>Yes</td>
      <td></td>
      <td>A single email address: `jane.doe@example.com`, or a dict containing an email address indexed by a name of the user to use as the sender of the email: `{'Jane Doe' : 'jane.doe@example.com'}`.</td>
    </tr>
    <tr>
      <td>email_subject</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The subject of the email.</td>
    </tr>
    <tr>
      <td>email_body</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The body of the email.</td>
    </tr>
  </tbody>
</table>

### Return

If the command executes successfully.

* * *

## locale_get

Mixed = TR50httpWorker.locale_get()

[locale.get](https://help.devicewise.com/display/ARG/locale.get) retrieves the current session's locale.

### Parameters

None.

### Return

Returns the dict of the session's locale on success, or the failure code.

* * *

## locale_list

Mixed = TR50httpWorker.locale_list()

[locale.list](https://help.devicewise.com/display/ARG/locale.list) lists supported locales.

### Parameters

None.

### <span>Return</span>

Returns the dict of supported locales on success, or the failure code.

* * *

## locale_set

Boolean = TR50httpWorker.locale_set(locale)

[locale.set](https://help.devicewise.com/display/ARG/locale.set) sets the current session's locale.

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
      <td>locale</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The locale to set.</td>
    </tr>
  </tbody>
</table>

### Return

If the command executes successfully.

* * *

## location_current

Mixed = TR50httpWorker.location_current(thing_key)

[location.current](https://help.devicewise.com/display/ARG/location.current) returns the last reported location for a thing.

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
      <td>thing_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>Identifies the thing associated with the location entry.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of the thing's current location on success, or the failure code.

* * *

## location_decode

Mixed = TR50httpWorker.location_decode(latitude, longitude)

[location.decode](https://help.devicewise.com/display/ARG/location.decode) is used to decode a latitude/longitude pair into an address.

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
      <td>latitude</td>
      <td>Float</td>
      <td>Yes</td>
      <td></td>
      <td>The latitude of the location.</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>Float</td>
      <td>Yes</td>
      <td></td>
      <td>The longitude of the location.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of the address of the latitude/longitude pair on success, or the failure code.

* * *

## location_encode

Mixed = TR50httpWorker.location_encode(location)

[location.encode](https://help.devicewise.com/display/ARG/location.encode) is used to encode a textual location into a latitude/longitude pair.

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
      <td>location</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The textual location to be encoded.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of the latitude/longitude associated with the provided location on success, or the failure code.

* * *

## location_publish

Boolean = TR50httpWorker.location_publish(thing_key, latitude, longitude[, date_obj[, heading[, altitude[, speed[, fix_acc[, fix_type[, corr_id]]]]]]])

[location.publish](https://help.devicewise.com/display/ARG/location.publish) is used to publish the location of a thing.

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
      <td>thing_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The unique identifier of the thing to which the location data is to be associated.</td>
    </tr>
    <tr>
      <td>latitude</td>
      <td>Float</td>
      <td>Yes</td>
      <td></td>
      <td>The latitude for this location publish.</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>Float</td>
      <td>Yes</td>
      <td></td>
      <td>The longitude for this location publish.</td>
    </tr>
    <tr>
      <td>date_obj</td>
      <td>Mixed</td>
      <td>No</td>
      <td>False</td>
      <td>A date object or the string representing the date and time for the location that is being published.</td>
    </tr>
    <tr>
      <td>heading</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>The direction for this location publish (in degrees where 0 is North, 90 is East, 180 is South, and 270 is West).</td>
    </tr>
    <tr>
      <td>altitude</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>The altitude for this location publish.</td>
    </tr>
    <tr>
      <td>speed</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>The speed for this location publish.</td>
    </tr>
    <tr>
      <td>fix_acc</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>The accuracy in meters of the coordinates being published.</td>
    </tr>
    <tr>
      <td>fix_type</td>
      <td>String</td>
      <td>No</td>
      <td>False</td>
      <td>A string describing the location fixation type. Typically "gps", "gnss", "manual", or "m2m-locate".</td>
    </tr>
    <tr>
      <td>corr_id</td>
      <td>String</td>
      <td>No</td>
      <td>False</td>
      <td>A correlation ID that can be used when querying to find related data objects.</td>
    </tr>
  </tbody>
</table>

### Return

If the command executes successfully.

* * *

## location_speedlimit

Mixed = TR50httpWorker.location_speedlimit(latitude, longitude)

[location.speedlimit](https://help.devicewise.com/display/ARG/location.speedlimit) is used to find the speed limit at a specified location.

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
      <td>latitude</td>
      <td>Float</td>
      <td>Yes</td>
      <td></td>
      <td>The latitude being requested.</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>Float</td>
      <td>Yes</td>
      <td></td>
      <td>The longitude being requested.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of the speed limit associated with the provided location on success, or the failure code.

* * *

## location_weather

Mixed = TR50httpWorker.location_weather(latitude, longitude)

[location.weather](https://help.devicewise.com/display/ARG/location.weather) is used to return the weather information at a specified location.

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
      <td>latitude</td>
      <td>Float</td>
      <td>Yes</td>
      <td></td>
      <td>The latitude being requested.</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>Float</td>
      <td>Yes</td>
      <td></td>
      <td>The longitude being requested.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of the weather information associated with the provided location on success, or the failure code.

* * *

## method_exec

Boolean = TR50httpWorker.method_exec(thing_key, method[, singleton[, ack_timeout[, parameters]]])

[method.exec](https://help.devicewise.com/display/ARG/method.exec) is used to execute a method of a thing.

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
      <td>thing_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>Identifies the thing for which the method is executed.</td>
    </tr>
    <tr>
      <td>method</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The method to execute.</td>
    </tr>
    <tr>
      <td>singleton</td>
      <td>Boolean</td>
      <td>No</td>
      <td>False</td>
      <td>Set to true if this call is to be run as a singleton.</td>
    </tr>
    <tr>
      <td>ack_timeout</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>Acknowlege timeout duration in seconds. Default is 30.</td>
    </tr>
    <tr>
      <td>parameters</td>
      <td>Dictionary</td>
      <td>No</td>
      <td>False</td>
      <td>Notification variables or method parameters to be passed to the method.</td>
    </tr>
  </tbody>
</table>

### Return

If the command executes successfully.

* * *

## org_find

Mixed = TR50httpWorker.org_find(org_key)

[org.find](https://help.devicewise.com/display/ARG/org.find) is used to find and return an organization.

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
      <td>org_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The key identifying the organization.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of the organization information on success, or the failure code.

* * *

## org_list

Mixed = TR50httpWorker.org_list([offset[, limit[, can_have_sub_orgs]]])

[org.list](https://help.devicewise.com/display/ARG/org.list) is used to return a list of organizations.

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
      <td>offset</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>The starting list offset, used for pagination, defaults to 0 if not specified.</td>
    </tr>
    <tr>
      <td>limit</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>Limits the number of results returned. Defaults to the maximum configured size.</td>
    </tr>
    <tr>
      <td>can_have_sub_orgs</td>
      <td>Boolean</td>
      <td>No</td>
      <td>False</td>
      <td>Whether to only list organizations that are capable of having child organizations.</td>
    </tr>
  </tbody>
</table>

### Return

Returns a dictionary of organizations on success, or the failure code.

* * *

## property_aggregate

Mixed = TR50httpWorker.property_aggregate(thing_key, property_key, calc, series, start, end[, split])

[property.aggregate](https://help.devicewise.com/display/ARG/property.aggregate) is used to obtain historical property data aggregated over a specified time period for a thing.

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
      <td>thing_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>Identifies the thing to which the property data is to be associated.</td>
    </tr>
    <tr>
      <td>property_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The key for the property that you wish to aggregate.</td>
    </tr>
    <tr>
      <td>calc</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The calculation to use for the aggregation: avg, sum, max, min, count, etc.</td>
    </tr>
    <tr>
      <td>series</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The series to be used when grouping property values to aggregate: 'hour' or 'day'.</td>
    </tr>
    <tr>
      <td>start</td>
      <td>Mixed</td>
      <td>Yes</td>
      <td></td>
      <td>A date object or the string representing the start of the specified time window.</td>
    </tr>
    <tr>
      <td>end</td>
      <td>Mixed</td>
      <td>Yes</td>
      <td></td>
      <td>A date object or the string representing the end of the specified time window.</td>
    </tr>
    <tr>
      <td>split</td>
      <td>Boolean</td>
      <td>No</td>
      <td>False</td>
      <td>Set to true if you want the timestamp and value fields to be split into two arrays.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of property aggregation on success, or the failure code.

* * *

## property_current

Mixed = TR50httpWorker.property_current(thing_key, property_key)

[property.current](https://help.devicewise.com/display/ARG/property.current) is used to retrieve the current value of a property.

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
      <td>thing_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>Identifies the thing to which the property data is associated.</td>
    </tr>
    <tr>
      <td>property_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The key for the property that you wish to retrieve.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of current property on success, or the failure code.

* * *

## property_publish

Boolean = TR50httpWorker.property_publish(thing_key, property_key, value[, date_obj[, corr_id]])

[property.publish](https://help.devicewise.com/display/ARG/property.publish) is used to publish property data (typically sensor data) for a thing.

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
      <td>thing_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>Identifies the thing to which the property data is to be associated.</td>
    </tr>
    <tr>
      <td>property_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The key for the property that you wish to publish.</td>
    </tr>
    <tr>
      <td>value</td>
      <td>Float</td>
      <td>Yes</td>
      <td></td>
      <td>The value to publish.</td>
    </tr>
    <tr>
      <td>date_obj</td>
      <td>Mixed</td>
      <td>No</td>
      <td>False</td>
      <td>A date object or the string representing the date and time the value was recorded.</td>
    </tr>
    <tr>
      <td>corr_id</td>
      <td>String</td>
      <td>No</td>
      <td>False</td>
      <td>A correlation ID that can be used when querying to find related data objects.</td>
    </tr>
  </tbody>
</table>

### Return

If the command executes successfully.

* * *

## session_info

Mixed = TR50httpWorker.session_info()

[session.info](https://help.devicewise.com/display/ARG/session.info) is used to obtain information about the current session.

### Parameters

None.

### Return

Returns the dict of current session on success, or the failure code.

* * *

## session_org_list

Mixed = TR50httpWorker.session_org_list([include_roles])

[session.org.list](https://help.devicewise.com/display/ARG/session.org.list) is used to obtain a list of organizations available to the current session.

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
      <td>include_roles</td>
      <td>Boolean</td>
      <td>No</td>
      <td>False</td>
      <td>Indicate that the available roles are to be returned with the response. Default is false.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of organizations (and roles) on success, or the failure code.

* * *

## session_org_switch

Boolean = TR50httpWorker.session_org_switch(org_key)

[session.org.switch](https://help.devicewise.com/display/ARG/session.org.switch) is used to switch a session between organizations.

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
      <td>org_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The organization key.</td>
    </tr>
  </tbody>
</table>

### Return

If the command executes successfully.

* * *

## thing_def_find

Mixed = TR50httpWorker.thing_def_find(thing_def_key)

[thing_def.find](https://help.devicewise.com/display/ARG/thing_def.find) is used to find an existing thing definition.

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
      <td>thing_def_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The key of the thing definition to find.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of the selected thing definition on success, or the failure code.

* * *

## thing_def_list

Mixed = TR50httpWorker.thing_def_list([offset[, limit]])

[thing_def.list](https://help.devicewise.com/display/ARG/thing_def.list) Acquire the list of Thing Definitions.

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
      <td>offset</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>The starting list offset, used for pagination, defaults to 0 if not specified.</td>
    </tr>
    <tr>
      <td>limit</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>Limits the number of results returned. Defaults to the maximum configured size.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of thing definitions on success, or the failure code.

* * *

## thing_find

Mixed = TR50httpWorker.thing_find(thing_key)

[thing.find](https://help.devicewise.com/display/ARG/thing.find) is used to find and return a thing.

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
      <td>thing_key</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>Identifies the thing.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of the selected thing on success, or the failure code.

* * *

## thing_list

Mixed = TR50httpWorker.thing_list([offset[, limit[, show[, sort[, tags[, keys]]]]]])

[thing.list](https://help.devicewise.com/display/ARG/thing.list) is used to find and return a list of things.

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
      <td>offset</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>The starting list offset, used for pagination. Defaults to 0 if not specified.</td>
    </tr>
    <tr>
      <td>limit</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>Limits the number of results returned. Defaults to the maximum configured size.</td>
    </tr>
    <tr>
      <td>show</td>
      <td>Array</td>
      <td>No</td>
      <td>False</td>
      <td>An array of field names of the data columns to return.</td>
    </tr>
    <tr>
      <td>sort</td>
      <td>String</td>
      <td>No</td>
      <td>False</td>
      <td>A string indicated the direction ("+" for ascending, "-" for descending) and column to sort the results by. To sort by the key descending, use "-key". Defaults to "+name".</td>
    </tr>
    <tr>
      <td>tags</td>
      <td>Array</td>
      <td>No</td>
      <td>False</td>
      <td>If specified, the command will only return things that have all tags in this parameter.</td>
    </tr>
    <tr>
      <td>keys</td>
      <td>Array</td>
      <td>No</td>
      <td>False</td>
      <td>If specified, the command will only return things that have the keys specified in this parameter.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of things on success, or the failure code.

* * *

## twilio_sms_send

Boolean = TR50httpWorker.twilio_sms_send(sms_to, sms_body, sms_from)

[twilio.sms.send](https://help.devicewise.com/display/ARG/twilio.sms.send) Send an SMS message to a phone number.

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
      <td>sms_to</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The recipient's phone number, a comma separated string of phone numbers, or an array of phone numbers.</td>
    </tr>
    <tr>
      <td>sms_body</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The body of the SMS message.</td>
    </tr>
    <tr>
      <td>sms_from</td>
      <td>String</td>
      <td>No</td>
      <td>False</td>
      <td>The sender's phone number.</td>
    </tr>
  </tbody>
</table>

### Return

If the command executes successfully.

* * *

## user_find

Mixed = TR50httpWorker.user_find(email_address)

[user.find](https://help.devicewise.com/display/ARG/user.find) is used to retrieve a user by email address.

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
      <td>email_address</td>
      <td>String</td>
      <td>Yes</td>
      <td></td>
      <td>The email address of the user.</td>
    </tr>
  </tbody>
</table>

### Return

Returns the dict of the user on success, or the failure code.

* * *

## user_list

Mixed = TR50httpWorker.user_list(offset, limit)

[user.list](https://help.devicewise.com/display/ARG/user.list) is used to return a list of users.

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
      <td>offset</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>The starting list offset, used for pagination, defaults to 0 if not specified.</td>
    </tr>
    <tr>
      <td>limit</td>
      <td>Integer</td>
      <td>No</td>
      <td>False</td>
      <td>Limits the number of results returned. Defaults to the maximum configured size.</td>
    </tr>
  </tbody>
</table>

### Return

Returns a dictionary of users on success, or the failure code.
