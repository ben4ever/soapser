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
* Implement custom validation with `native validation`_ since `soft` or `lxml`
  validation doesn't work with testing according to `Github issue`_.

.. _Github issue: https://github.com/arskom/spyne/issues/318
.. _native validation: http://spyne.io/docs/2.10/manual/05-02_validation.html#a-native-validation-example
