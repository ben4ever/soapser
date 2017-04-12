Design
======
* Look at ``examples/complex.py``.
* Why does ``_returns=Array(User)`` create 2 elements?
  ::

    <xs:complexType name="list_usersResponse">
      <xs:sequence>
        <xs:element name="list_usersResult0" type="s1:User" minOccurs="0" nillable="true"/>
        <xs:element name="list_usersResult1" type="s1:User" minOccurs="0" nillable="true"/>
      </xs:sequence>
    </xs:complexType>

Testing
=======
* Use ``examples/testing/helloworld_null.py``.

TODO
====
* Implement ``receiveItemMaster``.
* Don't write file every time I run script but only when SOAP server is hit.
  Write to a filename which has timestamp in it for example.
* Using ``_body_style='bare'`` seems to return ``None`` on client side (at least
  within tests). Investigate whether I can maybe use ``_body_style='wrapped'``
  and manually re-organize the XML element scaffolding to receive the same
  result as with ``bare``.
* Implement custom validation with `native validation`_ since ``soft`` or ``lxml``
  validation doesn't work with testing according to `Github issue`_. But before,
  check if `this <https://github.com/plq/neurons>`__ project tests in a maybe
  better way as it utilizes the ``NullServer`` as well.

.. _Github issue: https://github.com/arskom/spyne/issues/318
.. _native validation: http://spyne.io/docs/2.10/manual/05-02_validation.html#a-native-validation-example
